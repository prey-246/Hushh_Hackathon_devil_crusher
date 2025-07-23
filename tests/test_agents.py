# # tests/test_agents.py
from hushh_mcp.agents.schedule_agent.index import HushhScheduleAgent
from hushh_mcp.consent.token import issue_token

def test_schedule_token_valid():
    agent = HushhScheduleAgent()
    token_obj = issue_token("user_abc", "schedule_agent", "schedule.manage")
    trust_link = {
        "delegator": "schedule_agent",
        "delegate": "calendar_agent",
        "scope": "calendar.write",
        "signature": "abc123",
        "expires_at": 9999999999
    }
    result = agent.initiate_scheduling(user_id="user_abc", token_str=token_obj.token, trust_link=trust_link)
    assert result["status"] == "pass"


