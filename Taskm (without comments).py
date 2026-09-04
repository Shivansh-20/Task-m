import sys
import json
from datetime import datetime

if sys.argv[1].strip().lower() == "welcome":
    print("""Weclome, command words for input
-- for adding task -> "add" ,"task detail"
-- for checking tasks -> "list"  as action - > payload accepted ->  "done" and -> "not done"
-- for  printing all tasks -> use only "list"
-- To delete a task - >"delete" "task ID as payload" """)
action = sys.argv[1].strip().lower()
print(f"Action -> {action}")
payload = " ".join(sys.argv[2:]).strip().lower()
print("Payload is", payload or None)
with open("data.txt", "r") as file:
    data = json.load(file)

def add_task(data,payload):
    if data:
        max_id = max(item['id']for item in data)
        new_id = max_id + 1
    else: new_id = 1
    new_task = {
        "id":new_id,
        "task":payload,
        "created at":datetime.now().isoformat(),
        "status": "not done"
    }
    data.append(new_task)
    with open("data.txt" , "w") as file:
        json.dump(data, file, indent = 4)

def delete_tasks(data,payload):
    task_id = int(payload)
    for i, item in enumerate(data):
        if item["id"] == task_id:
            data.pop(i)
            print("deleted successfully")
            break
    else:
            print("Task not found")
    with open("data.txt", "w") as file:
        json.dump(data,file,indent=4)

if action == "add":
    add_task(data,payload)
    print("task added successfully")
elif action == "list":
    if len(sys.argv) > 2:
        if payload == "done":
            print([items for items in data if items.get("status")== "done"] or None)
        elif payload == "not done":
            print([items for items in data if items.get("status")== "not done"] or None)
    elif not payload:
        if data:
            for item in data:
                print(item)
        else:
            print("nothing to show")
elif action == "delete":
    delete_tasks(data,payload)
