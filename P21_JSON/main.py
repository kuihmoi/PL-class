import json

json_string = '{"project": "WebApp", "version": "1.0.0", "description": "A sample web application", "dependencies":["requests", "flask"]}'
data = json.loads(json_string)
print(data)

# access it and print the project name
print(data["project"])
print(data["dependencies"][1])

# saving data into a json file
with open("config.json","w") as file:
    json.dump(data,file,indent=4)
    print("Data written to config.json")

# how to read from a json file
with open("config.json","r") as file:
    data = json.load(file)
print(data)

data = {"compiler": "gcc", "version": "9.3.0", "flags": ["-O2", "-Wall"]}
json_string = json.dumps(data, indent=4)
print(json_string)

# how to handle json errors
try:
    invalid_json = '{"compiler": "gcc", version:11.2}' #missing quotation as error
    data = json.loads(invalid_json)
except json.JSONDecodeError as e:
    print(f"JSONDecodeError: {e}")

# correct version to show
try:
    invalid_json = '{"compiler": "gcc", "version":"11.2"}' #missing quotation as error
    data = json.loads(invalid_json)
    print(data)
except json.JSONDecodeError as e:
    print(f"JSONDecodeError: {e}")

# parse a json string for server configuration
json_string ='''
{
    "server": "API Server",
    "port": 8000,
    "endpoints": ["users", "products"],
    "settings":{
        "ssl": true,
        "timeout": 30
    }
}
'''

data =  json.loads(json_string)
print("Server Name:", data["server"])

print("First Endpoint:", data['endpoints'][0])

print("SSL Enabled:", data["settings"]["ssl"])

# next eg: create and read json file for python package dependencies

data = {
    "package": "my_app",
    "version": "1.0.0",
    "dependencies": [
        {"name": "requests", "version": "2.25.1"},
        {"name": "flask", "version": "1.1.2"},
    ]
}

with open("requirements.json", "w") as file:
    json.dump(data, file, indent=4)

with open("requirements.json", "r") as file:
    requirements = json.load(file)
    print(json.dumps(requirements, indent=4))

# next eg: parse a json for code repositories with nested commits
json_string = '''
    {
        "repo": "python-tool",
        "branch": "main",
        "commits": [
            {"id": "123", "author": "dev1", "details": {"date": "2023-10-01", "message": "Initial commit"}},
            {"id": "456", "author": "dev2", "details": {"date": "2023-10-02", "message": "Added feature X"}}
            ]
    }
'''

data = json.loads(json_string)
print("Repository:", data["repo"])

for commit in data['commits']:
    print(f"Commit {commit['id']} by {commit['author']} on {commit['details']['date']}:")

# last eg: handling json data sets of system logs 
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