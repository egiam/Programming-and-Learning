
#Second

meal = ["pizza","burger","spaghetti"]
drink = ["water","juice","cola"]
dessert = ["cake","chips","ice cream"]

for m in meal:
    for d in drink:
        for p in dessert:
            print(f"I will have {m} as a meal, {d} for drink and {p} for dessert.")



#First

password = "pass123"
answer = ""
number_try = 0
max_try = 8
maxTry = "Not reached"

while answer != password and maxTry != "Reached":
    if number_try < max_try:
        answer = input("Password: ")
        number_try += 1
    else:
        maxTry = "Reached"

if maxTry == "Reached":
    print("Account blocked")
else:
    print("Access granted")

