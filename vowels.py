vowels_and_constants=['a','e','i','o','u','r','t','w','A','P','X','O','U']
vowels=['a','e','i','o','u']
vowels_list=[]
constant_list=[]
for i in vowels_and_constants:
    i=i.lower()
    if i in vowels:
        vowels_list.append(i)
    else:
        constant_list.append(i)
print(vowels_list)
print(constant_list)