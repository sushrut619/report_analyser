"""Process events"""
from event_validator import validate_event_type, validate_imei
from counter import Counter

def parse_events(word_matrix) -> dict:
    """Segregate events into valid and invalid events"""
    all_events = {
        "invalid_events": {
            "invalid_type": set(),
            "invalid_imei": set(),
        },
        "valid_events": Counter()
    }

    for line in word_matrix:
        # if the line contains event details
        if len(line) == 3:
            event_type = line[0]
            imei = line[1]
            sku = line[2]
            is_valid_event = True

            is_valid_event_type = validate_event_type(event_type)
            is_valid_imei = validate_imei(imei)
            if not is_valid_event_type:
                all_events["invalid_events"]["invalid_type"].add(sku)
                is_valid_event = False
            if not is_valid_imei:
                all_events["invalid_events"]["invalid_imei"].add(sku)
                is_valid_event = False
            if is_valid_event:
                if event_type in ["SHIP", "SEND"]:
                    all_events["valid_events"][sku] -= 1
                    all_events["valid_events"][sku] = min(0, all_events["valid_events"][sku])
                else:
                    all_events["valid_events"][sku] += 1
            
    return all_events
            

        