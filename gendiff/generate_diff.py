from gendiff.parser import parse_file
from gendiff.diff_finder import check_diff
from gendiff.formatters.formatter import get_formatter


def generate_diff(file_path1: str, file_path2: str, format_style='stylish') -> str:
    file_data1 = parse_file(file_path1)
    file_data2 = parse_file(file_path2)
    diff = check_diff(file_data1, file_data2)
    return get_formatter(diff, format_style)
