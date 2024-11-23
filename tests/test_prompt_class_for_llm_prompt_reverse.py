"""tests/test_prompt_class_for_llm_prompt_reverse.py"""

import pytest

from src.prompt_class_for_llm_prompt_reverse import Prompt


def test_default_prompt():
    """
    デフォルトのプロンプトを生成する際の挙動をテスト。
    """
    prompt = Prompt()
    expected_output = "Reverse the string:\n{string}"
    assert (
        str(prompt) == expected_output
    ), f"Expected: {expected_output}, Got: {str(prompt)}"


@pytest.mark.parametrize(
    "action, target, separator, expected_output",
    [
        ("Reverse", "the string", "\n", "Reverse the string:\n{string}"),
        ("Please reverse", "this string", " ", "Please reverse this string: {string}"),
        ("Flip", "the text", ": ", "Flip the text:: {string}"),
    ],
)
def test_custom_prompt(action, target, separator, expected_output):
    """
    カスタマイズされたプロンプトの生成をテスト。
    """
    prompt = Prompt(action=action, target=target, separator=separator)
    assert (
        str(prompt) == expected_output
    ), f"Expected: {expected_output}, Got: {str(prompt)}"


def test_partial_customization():
    """
    一部の引数だけをカスタマイズした場合の挙動をテスト。
    """
    prompt = Prompt(action="Please reverse")
    expected_output = "Please reverse the string:\n{string}"
    assert (
        str(prompt) == expected_output
    ), f"Expected: {expected_output}, Got: {str(prompt)}"

    prompt = Prompt(target="this text")
    expected_output = "Reverse this text:\n{string}"
    assert (
        str(prompt) == expected_output
    ), f"Expected: {expected_output}, Got: {str(prompt)}"

    prompt = Prompt(separator=" ")
    expected_output = "Reverse the string: {string}"
    assert (
        str(prompt) == expected_output
    ), f"Expected: {expected_output}, Got: {str(prompt)}"
