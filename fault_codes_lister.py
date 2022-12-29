"""This module parses the input text and returns a enum with all fault codes"""
from enum import Enum

def fault_codes_lister(text):
    """List fault codes as enum"""
    text_lines = text.split("\n")
    fault_codes_mapping = {}
    for line in text_lines:
        words = line.split()
        if len(words) > 0 and words[0].isnumeric():
            code_num = int(words[0])
            code_desc = words[1].upper()
            fault_codes_mapping[code_desc] = code_num
    
    FaultCodes = Enum("FaultCodes", fault_codes_mapping)
    print("FaultCodes enum: ", list(FaultCodes))

    return FaultCodes