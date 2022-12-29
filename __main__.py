from arguments_parser import parse_arguments
from fault_codes_lister import fault_codes_lister
from file_reader import read_file

args = parse_arguments()
# print(args.file_path)

file_data = read_file(args.file_path)
fault_codes = fault_codes_lister(file_data)

