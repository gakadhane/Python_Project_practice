dict1 = {"name": "John", "age": 30}
print(dict1)
print(dict1.get("name"))
print(dict1.get("gender"))
print(dict1.items())
print(dict1.keys())
print(dict1.values())

value = dict1.pop("age")
print(value)  # Output: 30
print(dict1)  # Output: {"name": "John"}

item = dict1.popitem()
print(item)  # Output: ('age', 30)
print(dict1)  # Output: {"name": "John"}

dict3 = {"name": "John", "age": 30}
dict2 = {"gender": "Male", "city": "New York"}
dict3.update(dict2)
print(dict3)

dict1 = {"name": "John", "age": 30}
value = dict1.setdefault("gender", "Unknown")
print(value)  # Output: "Unknown"
print(dict1)  # Output: {"name": "John", "age": 30, "gender": "Unknown"}

