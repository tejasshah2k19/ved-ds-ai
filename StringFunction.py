import numpy as np 


names = np.array(["ram","shyAm","GanShyam","royal edu"])

print(names)

print(np.char.upper(names))
print(np.char.lower(names))
print(np.char.capitalize(names))
print(np.char.title(names))
print(np.char.swapcase(names))
print(  np.char.add(np.char.add(names," "),names))

print(np.char.multiply(names,3))

print(np.char.join("-",names))

print(np.char.count(names,"a"))


a =np.strings.multiply(names,3)
print(a)