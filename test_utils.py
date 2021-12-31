import utils


def test_replace_leading_spaces_with_asterisks():
    assert utils.replace_leading_spaces_with_asterisks("str") == "str"
    assert utils.replace_leading_spaces_with_asterisks("  str") == "*str"
    assert utils.replace_leading_spaces_with_asterisks("    str") == "**str"

