"""Run various scripts to generate the final report"""
from arguments_parser import parse_arguments
from fault_codes_lister import fault_codes_lister
from report_parser import read_file, parse_lines, build_word_matrix
from event_processor import parse_events

args = parse_arguments()
# print(args.file_path)

file_data = read_file(args.file_path)
text_lines = parse_lines(file_data)
word_matrix = build_word_matrix(text_lines)

fault_codes = fault_codes_lister(word_matrix)
print("Fault code mapping:")

for fault in fault_codes:
    print(f"{fault.value} {fault.name}")

processed_events = parse_events(word_matrix)
print("processed event: ", processed_events)

invalid_imei_count = len(processed_events["invalid_events"]["invalid_imei"])
invalid_type_count = len(processed_events["invalid_events"]["invalid_type"])

print(f"Invalid records:  {invalid_imei_count} Invalid IMEI, {invalid_type_count} Invalid event")

