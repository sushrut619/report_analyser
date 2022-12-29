"""Read and parse input report file"""
def read_file(input_file):
    """Open and read the report file"""
    with open(input_file, encoding="utf-8") as report_file:
        read_data = report_file.read()

    return read_data

# file_txt = read_file(args.file_path)
