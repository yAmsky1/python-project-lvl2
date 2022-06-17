from gendiff.parser import parse_file
from gendiff.diff_finder import check_diff
import gendiff.formatters.formatter as formatter


def generate_diff(file_path1, file_path2, format_style=formatter.STYLISH):
    file_data1 = parse_file(file_path1)
    file_data2 = parse_file(file_path2)
    diff = check_diff(file_data1, file_data2)
    return formatter.get_formatter(diff, format_style)
