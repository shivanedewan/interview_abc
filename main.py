
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
        self.acess = raw_data["Acess"]

    def __str__(self):
        return f"User -> {self.name}"

    # def update_user()

options = [
"addAccess READ",
"addAccess WRITE",
"addResource IMAGE",
"addAccessOnResource READ IMAGE",
"addActionOnResource WRITE IMAGE",
# addRole ADMIN
# addAccessOnResourceToRole READ IMAGE ADMIN
# addUser ADMINUSER
]
options = {i:o for i,o in enumerate(options)}


def choose_action(action: str, user, user_id):
    user_data = data[user_id]
    # 1st 3 done
    if action.startswith("addAccess "):
        role = action.split()[-1]
        if role not in user.acess:
            # user.acess.append(role)
            user_data["Acess"].append(role)
            

        else: 
            print(f"already a {role}")
        
    elif action.startswith("addResource IMAGE"):
        # user.image = action.split()[-1]
        user_data["image"] = action.split()[-1]
    
    elif action.startswith("addAccessOnResource"):
        user_data["image_acess"].append(action.split()[-2])


    change_user_data(user_data, user_id)


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