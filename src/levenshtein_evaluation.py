"""src/levenshtein_evaluation.py"""

import Levenshtein
import numpy as np
import pandas as pd


def calculate_levenshtein_distance(
    true_strings: list[str], pred_strings: list[str]
) -> float:
    """
    2つの文リストを比較し、平均Levenshtein距離を計算します。

    Args:
        true_strings (list[str]): 正解文のリスト。
        pred_strings (list[str]): 予測文のリスト。

    Returns:
        float: 平均Levenshtein距離。
    """
    if len(true_strings) != len(pred_strings):
        raise ValueError("`true_strings`と`pred_strings`の長さが一致しません。")

    distances = [
        Levenshtein.distance(true, pred)
        for true, pred in zip(true_strings, pred_strings)
    ]
    return np.mean(distances)


def load_strings(file_path: str, column_name: str) -> list[str]:
    """
    CSVファイルから指定カラムの文リストを読み込みます。

    Args:
        file_path (str): CSVファイルのパス。
        column_name (str): 読み込み対象のカラム名。

    Returns:
        list[str]: 文のリスト。
    """
    df = pd.read_csv(file_path)
    if column_name not in df.columns:
        raise ValueError(f"指定されたカラム名 '{column_name}' が存在しません。")
    return df[column_name].tolist()


def main():
    """
    テスト用データを読み込み、Levenshtein距離を計算します。
    """
    # ファイルパスとカラム名の設定
    true_file_path = "input/llm-prompt-reverse/train.csv"
    pred_file_path = "input/llm-prompt-reverse/test.csv"
    column_name = "reversed"

    # データ読み込み
    true_strings = load_strings(true_file_path, column_name)
    pred_strings = load_strings(pred_file_path, column_name)

    # Levenshtein距離の計算
    try:
        score = calculate_levenshtein_distance(true_strings, pred_strings)
        print(f"Levenshtein distance: {score:.4f}")
    except ValueError as e:
        print(f"エラー: {e}")


if __name__ == "__main__":
    main()
