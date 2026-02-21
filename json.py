#1
import json

# some JSON:
x = '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])

#30


#2
import json

# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)

#{"name": "John", "age": 30, "city": "New York"}


#3
import json

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)

#{"name": "John", "age": 30, "married": true, "divorced": false, "children": ["Ann","Billy"], "pets": null, "cars": [{"model": "BMW 230", "mpg": 27.5}, {"model": "Ford Edge", "mpg": 24.1}]}


#4
import json

print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))

#{"name": "John", "age": 30}
#["apple", "bananas"]
#["apple", "bananas"]
#"hello"
#42
#31.76
#true
#false
#null


#5
import json

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

# sort the result alphabetically by keys:
print(json.dumps(x, indent=4, sort_keys=True))

#{
#    "age": 30,
#    "cars": [
#        {
#            "model": "BMW 230",
#            "mpg": 27.5
#        },
#        {
#            "model": "Ford Edge",
#            "mpg": 24.1
#        }
#    ],
#    "children": [
#        "Ann",
#        "Billy"
#    ],
#    "divorced": false,
#    "married": true,
#    "name": "John",
#    "pets": null
#}


# JSON (JavaScript Object Notation) is a lightweight data format for storing and exchanging data.
# json.loads() converts a JSON string into a Python object (dict, list, etc.).
# json.dumps() converts a Python object into a JSON string.
# JSON can represent objects (dict), arrays (list/tuple), strings, numbers, booleans, and null (None in Python).
# You can write JSON to files and read JSON from files to work with structured data.
# Indentation and sort_keys parameters in json.dumps() help make the JSON readable and ordered.
