#.capitalize() and .title() : It is taking user details displaying them 

name = input("What is your name: ").capitalize()
age = input("How old are you: ")
village = input("What is the name of your village: ").capitalize()
state = input("What is the name of your state: ").title()
pin = input("What is your pincode: ")

print("\n" + "=" * 30)
print("          USER DETAILS           ")
print("=" * 30)
print(f"Name           : {name}")
print(f"Age            : {age}")
print(f"Village        : {village}")
print(f"State          : {state}")
print(f"Pincode        : {pin}")
print("=" * 30)
