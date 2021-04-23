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
for n in range(len(week)):
    print(n+1, week[n])
print("---------------")
 
# enumerate() 
for n, day in enumerate(week, 1):
    print(n, day)

# zip()
for day in zip(week, semana):
    print(day)