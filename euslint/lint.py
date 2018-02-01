from euslint.parse import parse
from euslint.test import test_line_length
from euslint.test import test_parenthesis
from euslint.test import test_tab
from euslint.test import test_whitespace


def lint(filepath, ignore_list, max_line_length):
    source_code = open(filepath).read()
    result = parse(source_code, max_line_length)

    test_list = []
    if 'parenthesis' not in ignore_list:
        test_list.append(test_parenthesis(result, filepath))
    if 'line_length' not in ignore_list:
        test_list.append(test_line_length(result, max_line_length, filepath))
    if 'tab' not in ignore_list:
        test_list.append(test_tab(result, filepath))
    if 'whitespace' not in ignore_list:
        test_list.append(test_whitespace(result, filepath))

    return sum(test_list)
