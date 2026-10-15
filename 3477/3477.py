"""pad thai"""

allowed = {
    "Pad Thai Sauce", "Tofu", "Pickle Turnip", "Shrimp",
    "Bean Sprouts", "Noodle", "Chives", "Lime",
    "Egg", "Oil", "Peanuts"
}
required_flavs = {"Sweet", "Sour", "Salty"}

ing = []
while True:
    s = input().strip()
    if s == "Cook":
        break
    if s:
        ing.append(s)

flav = []
while True:
    s = input().strip()
    if s == "End":
        break
    if s:
        flav.append(s)

ing_set = set(ing)
flav_set = set(flav)

if not ing_set.issubset(allowed):
    print("This is not Pad Thai!!!")

elif ing_set != allowed:
    print("This is bad!")

elif flav_set == required_flavs:
    print("Delicious!")

else:
    print("Not Bad...")
