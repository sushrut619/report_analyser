"""Function to parse command line arguments"""
import argparse

def parse_arguments():
    """Function to parse command line arguments"""
    parser = argparse.ArgumentParser("Fault codes lister")
    parser.add_argument(
        "file_path",
        help =
            "path to the report input file"
    )
    args = parser.parse_args()
    return args
