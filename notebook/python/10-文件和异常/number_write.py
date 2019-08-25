import json

numbers = [2,5,4,12,123,4,2]
filename = 'name.json'
user_name = input("What's you name: ")


with open(filename, 'w') as f_obj:
    json.dump(user_name, f_obj)


with open(filename) as f_obj:
    number2 = json.load(f_obj)

print(number2)