# hushh_mcp/agents/schedule_agent/index.py
from hushh_mcp.consent.token import validate_token
from hushh_mcp.trust.link import verify_trust_link, create_trust_link
from hushh_mcp.types import UserID
from hushh_mcp.constants import ConsentScope

class HushhScheduleAgent:
    required_scope = ConsentScope.CUSTOM_SCHEDULE_MANAGE

    def __init__(self, agent_id="schedule_agent"):
        self.agent_id = agent_id

    def initiate_scheduling(self, user_id: UserID, token_str: str, trust_link: dict) -> dict:
        is_valid, reason, token = validate_token(token_str, expected_scope=self.required_scope)
        if not is_valid or token.user_id != user_id:
            raise PermissionError("❌ Consent validation failed.")

        trust_ok, reason = verify_trust_link(trust_link, delegator=self.agent_id, delegate="calendar_agent")
        if not trust_ok:
            raise PermissionError("🚫 TrustLink invalid.")

        return {
            "status": "pass",
            "message": "Delegated to calendar agent",
            "user": user_id,
        }

    def issue_trust_link_to_calendar_agent(self, user_id: UserID):
        
        trust_link = create_trust_link(
            from_agent=self.agent_id,
            to_agent="calendar_agent",
            scope="calendar.write",
            signed_by_user=user_id,
        )
        print(f"✅ TrustLink created: {trust_link.signature[:8]}... (expires at {trust_link.expires_at})")
        return trust_link.dict()

