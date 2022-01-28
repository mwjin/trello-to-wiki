from trello_to_wiki.utils import replace_leading_spaces_with_asterisks


def test_replace_leading_spaces_with_asterisks():
    assert replace_leading_spaces_with_asterisks("str") == "str"
    assert replace_leading_spaces_with_asterisks("  str") == "*str"
    assert replace_leading_spaces_with_asterisks("    str") == "**str"

