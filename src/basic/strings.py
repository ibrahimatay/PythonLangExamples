welcomeMessage = "Welcome to my python learn"
print(welcomeMessage) # Welcome to my python learn

print("varible type is {}".format(type(welcomeMessage))) # varible type is <class 'str'>

editorMessage = "This is \"Visual Studio Code\" maybe you can use this editor"
print(editorMessage) # This is "Visual Studio Code" maybe you can use this editor

template = "Python"
print("2 index character: {}".format(template[2])) # 2 index character: t

print(template[1:3]) # yt
print(template[:2])  # Py
print(template[2:])  # thon
print(template[::])  # Python

words = welcomeMessage.split()
print(words) # ['Welcome', 'to', 'my', 'python', 'learn']

message = "Vale1=1;Value2=2"
config = message.split(";")
print(config) # ['Vale1=1', 'Value2=2']

message = message.replace(";",",")
print(message) # Vale1=1,Value2=2

priceOfString = "$123"
priceOfString = priceOfString.replace("$","")
print(priceOfString)

if priceOfString is int:
    print("Price value: {}".format(priceOfString)) # No

price = int(priceOfString)

if price is int:
    print("Price value: {}".format(price)) # 123

hello = "Hello"
world = "word"

newMessage = hello.join(world)
print(newMessage)

print(hello.center(15,"*")) # *****Hello*****

print(hello.find("e")) # e -> 1
print(hello.find("o")) # o -> 4
print(hello.find("w")) # w -> -1

myMessage = "           Hello learner      "
print(myMessage.strip()) # Hello learner