# # hushh_mcp/agents/conflict_resolver/index.py
from hushh_mcp.consent.token import validate_token
from hushh_mcp.operons.suggest_slot import suggest_alternate_slots
from hushh_mcp.constants import ConsentScope

class HushhConflictResolverAgent:
    required_scope = ConsentScope.CUSTOM_SCHEDULE_SUGGEST

    def __init__(self, agent_id="conflict_resolver"):
        self.agent_id = agent_id

    def suggest_alternatives(self, user_id: str, token_str: str, unavailable: list[str]):
        is_valid, _, token = validate_token(token_str, expected_scope=self.required_scope)
        if not is_valid or token.user_id != user_id:
            raise PermissionError("❌ Invalid token")

        alternatives = suggest_alternate_slots(unavailable)
        return {"suggested_slots": alternatives}

