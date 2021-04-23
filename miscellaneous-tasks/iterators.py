"""A look into Python iterators""" 

week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
semana = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta"]

# iter()
i = iter(week)
print(i)
print(next(i))

# .readline
with open("textfile.txt", "r") as file:
    for line in iter(file.readline, ''):
        print(line)

    
# range(len)

# enumerate() 
# zip()