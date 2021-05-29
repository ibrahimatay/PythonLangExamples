import os

os.environ.setdefault('PORT', '3306')
os.environ.setdefault('HOST','localhost')


print(os.environ.get('PORT'))
print(os.environ.get('HOST'))