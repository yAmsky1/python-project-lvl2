from gendiff.file_handler.parser import parse_file
from gendiff.file_handler.loader import get_data_from_file, get_file_extension
from gendiff.diff_finder import check_diff
import gendiff.formatters.formatter as formatter


def generate_diff(file_path1, file_path2, format_style=formatter.STYLISH):
    file_data1 = get_data_from_file(file_path1)
    file_data2 = get_data_from_file(file_path2)
    file_extension1 = get_file_extension(file_path1)
    file_extension2 = get_file_extension(file_path2)
    deserialized_data1 = parse_file(file_data1, file_extension1)
    deserialized_data2 = parse_file(file_data2, file_extension2)
    diff = check_diff(deserialized_data1, deserialized_data2)
    return formatter.get_formatter(diff, format_style)
