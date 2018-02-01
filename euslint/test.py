from __future__ import print_function

import sys


def test_parenthesis(result, filepath):
    if result['parenthesis_open'] != result['parenthesis_close']:
        print('{0}: parenthesis: # of open/close parenthesises doesn\'t match: {1} != {2}'  # NOQA
            .format(
                filepath, result['parenthesis_open'],
                result['parenthesis_close']),
            file=sys.stderr)
        return 1
    return 0


def test_tab(result, filepath):
    if len(result['tab']) != 0:
        for tab_result in result['tab']:
            print(
                '{0}:{1}: tab: line contains tab'
                .format(filepath, tab_result),
                file=sys.stderr)
        return 1
    return 0


def test_whitespace(result, filepath):
    if len(result['whitespace']) != 0:
        for whitespace_result in result['whitespace']:
            print(
                '{0}:{1}: whitespace: line contains invalid whitespace'
                .format(filepath, whitespace_result),
                file=sys.stderr)
        return 1
    return 0


def test_line_length(result, max_line_length, filepath):
    if len(result['line_length']) != 0:
        for line_length_result in result['line_length']:
            print(
                '{0}:{1}: line_length: line too long ({2} > {3} characters)'
                .format(
                    filepath, line_length_result[0]+1,
                    line_length_result[1], max_line_length),
                file=sys.stderr)
        return 1
    return 0
