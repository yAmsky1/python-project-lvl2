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
def result():
    with open('./tests/fixtures/result.txt') as res_file:
        return res_file.read()


def test_gen_diff(paths_json, paths_yaml, paths_mix, result):
    assert generate_diff(*paths_json) == result
    assert generate_diff(*paths_yaml) == result
    assert generate_diff(*paths_mix) == result
