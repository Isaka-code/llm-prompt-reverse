"""tests/test_levenshtein_evaluation.py"""

import pandas as pd
import pytest

from src.levenshtein_evaluation import (
    calculate_levenshtein_distance,
    load_strings,
    main,
)


def test_calculate_levenshtein_distance():
    """
    `calculate_levenshtein_distance` 関数が正しい平均Levenshtein距離を計算できるかをテスト。
    """
    true_strings = ["hello", "world", "test"]
    pred_strings = ["h3llo", "worlt", "test"]

    # 期待値: Levenshtein距離の平均
    expected_distance = (1 + 1 + 0) / 3
    result = calculate_levenshtein_distance(true_strings, pred_strings)
    assert result == pytest.approx(
        expected_distance
    ), f"期待値: {expected_distance}, 実際: {result}"

    # 長さが異なる場合の例外
    with pytest.raises(
        ValueError, match="`true_strings`と`pred_strings`の長さが一致しません。"
    ):
        calculate_levenshtein_distance(["hello"], ["world", "test"])


def test_load_strings(tmp_path):
    """
    `load_strings` 関数がCSVから指定カラムの文リストを正しく読み込むかをテスト。
    """
    # テスト用のデータフレーム作成
    test_data = pd.DataFrame({"original": ["abc", "def"], "reversed": ["cba", "fed"]})
    test_file = tmp_path / "test.csv"
    test_data.to_csv(test_file, index=False)

    # 正常系
    result = load_strings(str(test_file), "original")
    expected = ["abc", "def"]
    assert result == expected, f"期待値: {expected}, 実際: {result}"

    # 異常系: 存在しないカラム
    with pytest.raises(
        ValueError, match="指定されたカラム名 'nonexistent' が存在しません。"
    ):
        load_strings(str(test_file), "nonexistent")


def test_main_integration(tmp_path, monkeypatch):
    """
    `main` 関数の全体的な動作を確認する統合テスト。
    """
    # テスト用データ作成
    train_data = pd.DataFrame({"original": ["abc", "def"], "reversed": ["cba", "fed"]})
    test_data = pd.DataFrame({"original": ["cba", "fed"], "reversed": ["abc", "def"]})

    input_dir = tmp_path / "input" / "llm-prompt-reverse"
    input_dir.mkdir(parents=True)
    train_file = input_dir / "train.csv"
    test_file = input_dir / "test.csv"
    train_data.to_csv(train_file, index=False)
    test_data.to_csv(test_file, index=False)

    # パスをモック
    monkeypatch.setattr("builtins.input", lambda _: str(train_file))
    monkeypatch.setattr("builtins.input", lambda _: str(test_file))

    # 実行
    monkeypatch.setattr("src.levenshtein_evaluation.main", main)
    main()


if __name__ == "__main__":
    pytest.main()
