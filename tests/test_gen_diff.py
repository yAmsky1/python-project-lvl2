from gendiff import generate_diff
import pytest


@pytest.fixture()
def paths_json():
    return './tests/fixtures/file1.json', './tests/fixtures/file2.json'


@pytest.fixture()
def paths_yaml():
    return './tests/fixtures/file1.yaml', './tests/fixtures/file2.yaml'


@pytest.fixture()
def paths_mix():
    return './tests/fixtures/file1.json', './tests/fixtures/file2.yaml'


@pytest.fixture()
def result_stylish():
    with open('./tests/fixtures/result_stylish.txt') as res_file:
        return res_file.read()


@pytest.fixture()
def result_plain():
    with open('./tests/fixtures/result_plain.txt') as res_file:
        return res_file.read()


# @pytest.fixture()
# def result_json():
#     with open('./tests/fixtures/result_json.txt') as res_file:
#         return res_file.read()


def test_gen_diff_stylish(paths_json, paths_yaml, paths_mix, result_stylish):
    assert generate_diff(*paths_json) == result_stylish
    assert generate_diff(*paths_yaml) == result_stylish
    assert generate_diff(*paths_mix) == result_stylish


def test_gen_diff_plain(paths_json, paths_yaml, paths_mix, result_plain):
    assert generate_diff(*paths_json, form='plain') == result_plain
    assert generate_diff(*paths_yaml, form='plain') == result_plain
    assert generate_diff(*paths_mix, form='plain') == result_plain


# def test_gen_diff_json(paths_json, paths_yaml, paths_mix, result_json):
#     assert generate_diff(*paths_json, form='json') == result_json
#     assert generate_diff(*paths_yaml, form='json') == result_json
#     assert generate_diff(*paths_mix, form='json') == result_json
