         #012345678901234
parrot = "Norwegian Blue"
# Slicing

print(parrot[0:6])      #Norweg
print(parrot[-14:-8])   #Norweg

print(parrot[0:9])      #Norwegian
print(parrot[-14:-5])   #Norwegian

print(parrot[-4:-2])    #Bl
print(parrot[-4:12])    #Bl

print()

#Using Step in slice
print(parrot[0:6:2])    #Nre
print(parrot[0:6:3])    #Nw

number = "9,223;372:036 854,775;807"
separators = number[1::4]

values = "".join(char if char not in separators else " " for char in number).split()
print([int(val) for val in values])
 