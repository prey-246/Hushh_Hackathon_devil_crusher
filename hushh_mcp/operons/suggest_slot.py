def suggest_alternate_slots(unavailable: list[str]) -> list[str]:
    default_slots = [
        "2025-07-23T10:00:00Z",
        "2025-07-23T14:00:00Z",
        "2025-07-24T09:00:00Z"
    ]
    return [slot for slot in default_slots if slot not in unavailable]
