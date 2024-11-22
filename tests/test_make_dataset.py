"""tests/test_make_dataset.py"""

import os

import pandas as pd

from src.make_dataset import generate_dataset, make_string, save_dataset


def test_make_string():
    """
    `make_string` 関数が指定された長さのランダムな文字列を生成できることを確認します。
    """
    string_length = 10
    string = make_string(string_length)
    assert isinstance(string, str), "生成された値が文字列でない"
    assert len(string) == string_length, "生成された文字列の長さが一致しない"
    assert all(
        c.islower() and c.isalpha() for c in string
    ), "生成された文字列に英小文字以外が含まれる"


def test_generate_dataset():
    """
    `generate_dataset` 関数が正しいデータセットを生成することを確認します。
    """
    n_strings = 5
    string_length = 8
    seed = 0

    dataset = generate_dataset(n_strings, string_length, seed)
    assert isinstance(dataset, pd.DataFrame), "生成されたデータがDataFrameでない"
    assert list(dataset.columns) == ["original", "reversed"], "カラム名が一致しない"
    assert len(dataset) == n_strings, "生成された文の数が一致しない"

    for _, row in dataset.iterrows():
        assert (
            row["original"] == row["reversed"][::-1]
        ), "逆順文字列が正しく生成されていない"


def test_save_dataset(tmp_path):
    """
    `save_dataset` 関数がデータセットを正しくCSVに保存できることを確認します。
    """
    dataset = pd.DataFrame({"original": ["abc", "def"], "reversed": ["cba", "fed"]})
    save_path = tmp_path / "test.csv"

    save_dataset(dataset, save_path)

    assert os.path.exists(save_path), "CSVファイルが正しく保存されていない"
    loaded_dataset = pd.read_csv(save_path)
    pd.testing.assert_frame_equal(
        dataset,
        loaded_dataset,
        check_dtype=True,
        obj="保存されたデータセットが一致しない",
    )


def test_integration(tmp_path):
    """
    全体的な統合テストとして、`generate_dataset` と `save_dataset` を組み合わせた動作を確認します。
    """
    n_strings = 10
    string_length = 6
    seed = 42
    save_path = tmp_path / "integrated_test.csv"

    dataset = generate_dataset(n_strings, string_length, seed)
    save_dataset(dataset, save_path)

    loaded_dataset = pd.read_csv(save_path)
    pd.testing.assert_frame_equal(
        dataset,
        loaded_dataset,
        check_dtype=True,
        obj="統合テスト: 保存されたデータセットが一致しない",
    )
