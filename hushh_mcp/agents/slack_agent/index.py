# # hushh_mcp/agents/slack_agent/index.py
from hushh_mcp.consent.token import validate_token
from hushh_mcp.constants import ConsentScope

class HushhSlackAgent:
    required_scope = ConsentScope.CUSTOM_SLACK_SEND

    def __init__(self, agent_id="slack_agent"):
        self.agent_id = agent_id

    def send_dm(self, user_id: str, token_str: str, msg: str) -> dict:
        is_valid, _, token = validate_token(token_str, expected_scope=self.required_scope)
        if not is_valid or token.user_id != user_id:
            raise PermissionError("🚫 Invalid Slack token")

        print(f"📨 [Slack Message to {user_id}]: {msg}")
        return {"status": "sent"}

