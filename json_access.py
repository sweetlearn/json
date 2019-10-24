import json

# a Python object (dict):
dict = {
    "name": "John",
    "age": 30,
    "married": True,
    "divorced": False,
    "children": ("Ann", "Billy"),
    "pets": None,
    "cars": [
        {"model": "BMW 230", "mpg": 27.5},
        {"model": "Ford Edge", "mpg": 24.1}
    ]
}

# Convert dictionary into JSON:
y = json.dumps(dict, indent=4)

# the result is a JSON string:
print(type(y))
print(dict["cars"][0]['model'])

z = dict["cars"]

print(z)

for i in z:
    print('The Car :', i)