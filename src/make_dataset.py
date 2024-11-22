"""src/make_dataset.py"""

import numpy as np
import pandas as pd


def make_string(n: int) -> str:
    """
    指定された長さのランダムな英小文字の文字列を生成します。

    Args:
        n (int): 生成する文字列の長さ。

    Returns:
        str: 生成されたランダムな文字列。
    """
    return "".join(np.random.choice(list("abcdefghijklmnopqrstuvwxyz"), n))


def generate_dataset(n_strings: int, string_length: int, seed: int) -> pd.DataFrame:
    """
    ランダムな文字列とその逆順文字列を含むデータセットを生成します。

    Args:
        n_strings (int): 生成する文の数。
        string_length (int): 各文の長さ。
        seed (int): 乱数シード。

    Returns:
        pd.DataFrame: データセット（オリジナル文と逆順文）。
    """
    np.random.seed(seed)
    original_strings = [make_string(string_length) for _ in range(n_strings)]
    reversed_strings = [string[::-1] for string in original_strings]
    return pd.DataFrame({"original": original_strings, "reversed": reversed_strings})


def save_dataset(dataset: pd.DataFrame, path: str) -> None:
    """
    データセットをCSVファイルに保存します。

    Args:
        dataset (pd.DataFrame): 保存するデータセット。
        path (str): 保存先のファイルパス。
    """
    dataset.to_csv(path, index=False)


def main():
    """
    データセットを生成し、指定されたパスに保存します。
    """
    # パラメータ設定
    output_dir = "input/llm-prompt-reverse/"
    train_path = f"{output_dir}train.csv"
    test_path = f"{output_dir}test.csv"

    # データセット生成と保存
    train_dataset = generate_dataset(n_strings=10, string_length=10, seed=0)
    save_dataset(train_dataset, train_path)

    test_dataset = generate_dataset(n_strings=10, string_length=10, seed=1)
    save_dataset(test_dataset, test_path)


if __name__ == "__main__":
    main()
