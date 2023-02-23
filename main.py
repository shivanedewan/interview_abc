
import json
import argparse

with open("db.json", "r") as fhand:
    data = json.load(fhand)

def return_user(ID): 
    return data[ID]

def change_user_data(user_data, ID):
    data[ID] = user_data
    update_data()

def update_data():
    with open("db.json", "w") as fhand:
        json.dump(data, fhand, indent=2)


class User:
    def __init__(self, user_raw_data):
        self.read_raw_data(user_raw_data)
        self.raw_data = user_raw_data

    def read_raw_data(self, raw_data):
        self.name = raw_data["Name"]
        self.access = raw_data["Acess"]
        self.image = raw_data.get("image", None)
        self.image_access = raw_data.get("image_access", [])

    def __str__(self):
        return f"User -> {self.name}"

    def update_user(self):
        data[self.raw_data["ID"]] = self.raw_data
        update_data()

    def addRole(self, role):
        if role not in self.access:
            self.access.append(role)
            self.raw_data["Acess"] = self.access
            self.update_user()
        else:
            print(f"{self.name} already has the role {role}")

    def addAccessOnResourceToRole(self, access, resource, role):
        if role in self.access:
            resource_access = self.raw_data.get(f"{resource}_access", [])
            if access not in resource_access:
                resource_access.append(access)
                self.raw_data[f"{resource}_access"] = resource_access
                self.update_user()
            else:
                print(f"{access} access already exists for {resource} resource and {role} role")
        else:
            print(f"{self.name} doesn't have the {role} role")


options = [
    "addAccess READ",
    "addAccess WRITE",
    "addResource IMAGE",
    "addAccessOnResource READ IMAGE",
    "addActionOnResource WRITE IMAGE",
    "quit",
]
options = {i:o for i,o in enumerate(options)}

def addUser(name):
    user_id = len(data)
    user_data = {"ID": user_id, "Name": name, "Acess": []}
    data.append(user_data)
    update_data()
    return user_id



def choose_action(action: str, user, user_id):
    user_data = data[user_id]

    if action.startswith("addAccess "):
        role = action.split()[-1]
        if role not in user.access:
            user_data["Acess"].append(role)
        else: 
            print(f"{user.name} already has the {role} role")
        
    elif action.startswith("addResource IMAGE"):
        user_data["image"] = action.split()[-1]
    
    elif action.startswith("addAccessOnResource"):
        resource = action.split()[-1]
        access = action



if __name__ =="__main__":
    user_id = input("Enter Login ID: ") # str
    user_raw_data = return_user(user_id)
    i_user = User(user_raw_data)
   
    if "ADMIN" not in i_user.acess:
        print("YOU DONT HAvE PERM")
        quit()
    while 1:
        c_user_id = input("Enter User ID: ")
        c_user = User(return_user(c_user_id))
        print("Choose an Option:")
        print(options)
        option_chosen=int(input("Choose num: "))
        action = options[option_chosen]
        choose_action(action, c_user, c_user_id)
        print(f"Performed {action}")