#adding item to dict
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "r"
print(thisdict)


thisdict.update({"color": "red"})
print(thisdict)


#remove item from dict
thisdict.pop("model")
print(thisdict)

thisdict.popitem()
print(thisdict)

del thisdict["brand"]
print(thisdict)