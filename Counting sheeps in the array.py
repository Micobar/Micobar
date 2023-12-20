def count_sheeps(sheep):
    sheeps = sheep.count(True)

    return sheeps
    
sheep_number = [
    True,  True,  True,  False,
  True,  True,  True,  True ,
  True,  False, True,  False,
  True,  False, False, True ,
  True,  True,  True,  True ,
  False, False, True,  True
]

print(count_sheeps(sheep_number))