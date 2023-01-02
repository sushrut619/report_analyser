def parse_events(word_matrix):
    all_event = {
        "valid_events": [],
        "invalid_events": []
    }
    for line in word_matrix:
        if len(line) == 3:
            event_type = line[0]
            imei = line[1]
            sku = line[2]
        is_valid_event = check_event_validity(event_type, imei, sku)

        