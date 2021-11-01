import pandas as pd

# read contents of csv file
file = pd.read_csv("/Users/aysanaghazadeh/University/Pitt/Research/Malihe/ai2d-rst-v1-1/files.csv")
print("\nOriginal file:")
print(file.columns)

# adding header
headerList = ['image_url']

# converting data frame to csv
file.to_csv("/Users/aysanaghazadeh/University/Pitt/Research/Malihe/ai2d-rst-v1-1/urls.csv", header=headerList, index=False)

