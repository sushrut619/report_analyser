"""Module to check event validity"""

valid_event_types = ["SHIP", "SEND", "RECV"]

def validate_event_type(event_type):
    """Check if event type is valid"""
    return event_type in valid_event_types

def validate_imei(imei):
    """Check if IMEI is valid"""
    if len(imei) != 15:
        return False
    checksum = 0
    for index in range(14):
        digit = int(imei[index])
        if (index % 2 == 1):
            double_digit = 0
            if digit >= 5:
                double_digit = 1 + (digit - 5) * 2
            else:
                double_digit = digit * 2
            checksum += double_digit
        else:
            checksum += digit
    # print("checkSum: ", checksum)
    checksum += int(imei[14])

    return checksum % 10 == 0

def check_event_validity(event_type):
    pass


