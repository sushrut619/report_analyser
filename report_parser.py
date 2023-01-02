"""Read and parse input report file"""
def read_file(input_file):
    """Open and read the report file"""
    with open(input_file, encoding="utf-8") as report_file:
        read_data = report_file.read()

    return read_data

def parse_lines(text):
    """parse text into separate lines"""
    text_lines = text.split("\n")
    return text_lines
# file_txt = read_file(args.file_path)

def build_word_matrix(text_lines):
    """build 2D word matrix from list of strings"""
    word_matrix = []
    for line in text_lines:
        line_words = line.split()
        word_matrix.append(line_words)

    return word_matrix

