# hushh_mcp/agents/calendar_agent/index.py
from hushh_mcp.consent.token import validate_token
from hushh_mcp.constants import ConsentScope
from hushh_mcp.operons.check_conflict import check_calendar_conflicts

class HushhCalendarAgent:
    required_scope = ConsentScope.CUSTOM_CALENDAR_WRITE

    def __init__(self, agent_id="calendar_agent"):
        self.agent_id = agent_id

    def create_event(self, user_id: str, token_str: str, proposed_time: str, existing: list[str]):
        is_valid, _, token = validate_token(token_str, expected_scope=self.required_scope)
        if not is_valid or token.user_id != user_id:
            raise PermissionError("❌ Invalid calendar token")

        if check_calendar_conflicts(existing, proposed_time):
            return {"status": "conflict", "slot": proposed_time}

        return {"status": "created", "event_id": "123", "start_time": proposed_time}
