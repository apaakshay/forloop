dict={1:"you",2:"me",3:"she",4:"he"}
dict.update({4:"aloy"})
print(dict)

dict["5"]="adgha"
print(dict)

dict.pop(1)
print(dict)

dict.popitem()
print(dict)

del dict[2]
print(dict)

dict.clear()
print(dict)