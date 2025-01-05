from evtx.parser import PyEvtxParser


def main():
    parser = PyEvtxParser("./Security.evtx")
    for record in parser.records_json():
        print(f'Event Record ID: {record["event_record_id"]}')
        print(f'Event Timestamp: {record["timestamp"]}')
        print(record['data'])
        print(f'------------------------------------------')