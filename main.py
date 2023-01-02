"""Run various scripts to generate the final report"""
from arguments_parser import parse_arguments
from fault_codes_lister import fault_codes_lister
from report_parser import read_file, parse_lines, build_word_matrix

args = parse_arguments()
# print(args.file_path)

file_data = read_file(args.file_path)
text_lines = parse_lines(file_data)
word_matrix = build_word_matrix(text_lines)

fault_codes = fault_codes_lister(word_matrix)
print("Fault code mapping:")

for fault in fault_codes:
    print(f"{fault.value} {fault.name}")

