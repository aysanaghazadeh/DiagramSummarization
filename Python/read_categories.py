import json
import random
import pandas as pd

file = open('/Users/aysanaghazadeh/University/Pitt/Research/Malihe/ai2d-rst-v1-1/json/categories_ai2d-rst.json')
category_map = json.load(file)
print(len(set(category_map.values())))
categories = {}
images = []
keys = list(category_map.keys())      # Python 3; use keys = d.keys() in Python 2
random.shuffle(keys)
for i in keys:
    if category_map[i] in categories:
        if categories[category_map[i]] < 1:
            categories[category_map[i]] += 1
            images.append(i)
    else:
        categories[category_map[i]]= 1
        images.append(i)

print(categories)
df = pd.DataFrame(images, columns=['image_url'])
print(df)
df.to_csv("/Users/aysanaghazadeh/University/Pitt/Research/Malihe/ai2d-rst-v1-1/image_files.csv", index=False)



