import json
logs = {
    "system": "web_server",
    "logs": [
        {"id": i, "event": f"request-{i}", "timestamp": f"2025-01-01T{i:02d}:00:00", "status": "success" if i % 2 == 0 else "error"}
        for i in range(50)
    ]   
}

with open ("logs.json", "w") as f:
    json.dump(logs, f, indent=4)

with open("logs.json", "r") as f:
    data = json.load(f)
    error_logs = [log for log in data["logs"] if log["status"] == "error"]
    print(f"Error Logs: {len(error_logs)}")
    print(json.dumps(error_logs, indent=4))