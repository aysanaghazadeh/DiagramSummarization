import shutil, os


with open('/Users/aysanaghazadeh/University/Pitt/Research/Malihe/ai2d-rst-v1-1/json/ai2d-rst/file_names.txt') as f:
    lines = f.readlines()

filenames = []
for l in lines:
    new_l = l.split('\n')
    filenames.append(new_l[0])

for filename in filenames:
    shutil.copy('/Users/aysanaghazadeh/University/Pitt/Research/Malihe/ai2d/images/'+filename, '/Users/aysanaghazadeh/University/Pitt/Research/Malihe/ai2d-rst-v1-1/images')

