import json

data = json.load(open('myfile.json'))

print(data)
print(type(data))

quiz = data["quiz"]
print(type("quiz"))
print(quiz)
