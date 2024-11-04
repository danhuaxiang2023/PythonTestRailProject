class person:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    def __str__(self) -> str:
        return f"{self.name}:{self.age}"
    
p1 = person('John', 56)    
print(p1)
print(p1.name)