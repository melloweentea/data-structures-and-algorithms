mydict = {
    "name": "Pam",
    "age": 19,
    "gender": "female",
    "myopic": True
}

listtest = {
    "1": [[], []],
    "1": [[], []],
}
# check for presence of items by:
if "name" in mydict:
    print(mydict["name"])

#iterating through dict
for key, val in mydict.items():
    print(key, val)

for key in mydict.keys():
    print(key)

for val in mydict.values():
    print(val)
