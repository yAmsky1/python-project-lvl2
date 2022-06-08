# import pytest
import gendiff
from gendiff import generate_diff, get_format


def test_generate_diff():
    with open('tests/fixtures/test_generate_diff_result') as test:
        result = ''
        for i, line in enumerate(test, 1):
            result += line
    assert generate_diff('tests/fixtures/file1.json', 'tests/fixtures/file2.json') == result


def test_generate_diff2():
    with open('tests/fixtures/test_generate_diff_result2') as test:
        result = ''
        for i, line in enumerate(test, 1):
            result += line
    assert generate_diff('tests/fixtures/file1.json', 'tests/fixtures/file1.json') == result


def test_generate_diff3():
    with open('tests/fixtures/test_generate_diff_result3') as test:
        result = ''
        for i, line in enumerate(test, 1):
            result += line
    assert generate_diff('tests/fixtures/file1.json', 'tests/fixtures/empty.json') == result


def test_generate_diff4():
    with open('tests/fixtures/test_generate_diff_result') as test:
        result = ''
        for i, line in enumerate(test, 1):
            result += line
    assert generate_diff('tests/fixtures/file1.yaml', 'tests/fixtures/file2.yaml') == result


def test_get_format():
    assert get_format('') is None
