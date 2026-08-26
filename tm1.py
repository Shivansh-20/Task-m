import sys
import json


action = sys.argv[1]
#payload = sys.argv[2]
print(f"Action ->", {action})

payload = " ".join(sys.argv[2:])
print("Payload is", payload)

with open("data.txt", "r") as file:
    data = json.load(file)

def read_name(data):
    print(data["name"])

def read_age():
    with open("data.txt", "r") as file:
        data = json.load(file)
    print(data["age"])

def change_name(data,new):
    data["name"] = new
    with open("data.txt", "w") as file:
        json.dump(data,file)




#change_name(data,"SH")
def add_task(data,payload):
    ids = []
    if data:
        max_id = max(item['id']for item in data)
        new_id = max_id + 1
    else: new_id = 1
    new_task = {
        "id":new_id,
        "task":payload
    }
    data.append(new_task)
    with open("data.txt" , "w") as file:
        json.dump(data, file, indent = 4)

if action == "add":
    add_task(data,payload)


