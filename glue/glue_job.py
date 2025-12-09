import json
from datetime import datetime
from pathlib import Path

DATA_FILE = Path(__file__).parent.parent / "data" / "events.json"

def load_events(path: Path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def transform_events(raw_events):
    transformed = []
    for evt in raw_events:
        user_id = evt.get("user_id")
        event_name = evt.get("event")
        feature_name = evt.get("feature")
        ts_str = evt.get("timestamp")

        # basic validation
        if not user_id or not event_name or not ts_str:
            continue

        # parse timestamp
        event_ts = datetime.fromisoformat(ts_str.replace("Z", "+00:00"))

        row = {
            "USER_ID": user_id,
            "EVENT_NAME": event_name,
            "FEATURE_NAME": feature_name,
            "EVENT_TS": event_ts.isoformat(),
            "RAW_PAYLOAD": evt  # full original event as JSON
        }
        transformed.append(row)
    return transformed

def main():
    print(f"Loading events from: {DATA_FILE}")
    raw_events = load_events(DATA_FILE)
    print(f"Loaded {len(raw_events)} raw events")

    transformed = transform_events(raw_events)
    print(f"Transformed into {len(transformed)} rows:")

    for row in transformed:
        print(row)

if __name__ == "__main__":
    main()

