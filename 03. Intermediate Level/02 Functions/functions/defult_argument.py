# =================== what is function default argument ===================
# default argument is a value that is assigned to a parameter
# it's optional argument 

def person(name, age=18):
    print(name, age)

person("John")
person("John", 25)


def add(a, b=10):
    return a + b

print(add(5))
print(add(5, 15))