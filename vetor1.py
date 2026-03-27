
v = [1,2,3,4,5,6,7,8,9]
v.insert(2,5)

print(v[4])
print(v[-1])
print(v[0])
print(v[-2])

for r in v:
    print(v)

for i in range(len(v)):
    print(i,v[i])

c = ["jhon","Porc","is","calling","you","acept?"]

print(c[4])
print(c[-1])
print(c[0])
print(c[-2])

for r in c:
    print(c)

for i in range(len(c)):
    print(i,v[i])

del c[1]
print(c[1])

len(c)

notas = [7.5,6.8,9,10]
media = sum(notas)/len(notas)
print("Média da truma: ", media)
