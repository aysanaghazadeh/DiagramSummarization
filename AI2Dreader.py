import json

f = open("/Users/aysanaghazadeh/PycharmProjects/DiagramSummarization/ai2d/categories.json",)


# returns JSON object as
# a dictionary
categories = json.load(f)

print(len(set(categories.values())))
print(set(categories.values()))