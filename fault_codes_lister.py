"""This module parses the input text and returns a enum with all fault codes"""
from enum import Enum

def fault_codes_lister(word_matrix):
    """List fault codes as enum"""
    fault_codes_mapping = {}
    for line in word_matrix:
        if len(line) > 0 and line[0].isnumeric():
            code_num = int(line[0])
            code_desc = line[1].upper()
            fault_codes_mapping[code_desc] = code_num

    FaultCodes = Enum("FaultCodes", fault_codes_mapping)
    # print("FaultCodes enum: ", list(FaultCodes))

    return FaultCodes