# hushh_mcp/agents/schedule_agent/manifest.py

manifest = {
    "id": "schedule_agent",
    "description": "Schedules meetings via Google Calendar and Slack. Delegates to calendar_agent and slack_agent.",
    "scopes": ["schedule.manage"],
    "version": "0.1.0"
}