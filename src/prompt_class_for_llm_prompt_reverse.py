"""src/prompt_class_for_llm_prompt_reverse.py"""


class Prompt:
    """
    プロンプトを要素に分割し、構成可能にするクラス。
    Optunaなどで各要素を最適化する際に利用。
    """

    def __init__(
        self,
        action: str = "Reverse",
        target: str = "the string",
        separator: str = "\n",
    ):
        """
        Args:
            action (str): プロンプトの動詞部分。例: "Reverse"
            target (str): プロンプトの目的語部分。例: "the string"
            separator (str): 改行文字や区切り文字。例: "\n"
        """
        self.action = action
        self.target = target
        self.separator = separator

    def __str__(self) -> str:
        """
        プロンプトの文字列表現を生成します。

        Returns:
            str: プロンプトの文字列表現。
        """
        return f"{self.action} {self.target}:{self.separator}{{string}}"


# 使用例
if __name__ == "__main__":
    # デフォルト設定でプロンプトを生成
    default_prompt = Prompt()
    print(str(default_prompt))

    # カスタマイズされたプロンプト
    custom_prompt = Prompt(action="Please reverse", target="this string", separator=" ")
    print(str(custom_prompt))
