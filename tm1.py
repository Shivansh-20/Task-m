import sys
import json
'''print(sys.argv)

action = sys.argv[1]
payload = sys.argv[2]
print(f"Action ->", {action})
print("Payload is", payload)

#payload = " ".join(sys.argv[2:])
'''
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


change_name(data,"SH")





