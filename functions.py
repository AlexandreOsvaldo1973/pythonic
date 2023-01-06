# Funções

def simple():
    return "First function"

print(simple())
    

def plus_ten(a):
    result = a + 10
    print ("Outcome")
    return result

print (plus_ten(2))

def wage(w_hours): # salario
    return w_hours * 25

def with_bonus(w_hours):
    return wage(w_hours) + 50

print(wage(8), with_bonus(8))

def add_10(m):
    if m >= 100:
        m = m + 10
        return m
    else:
        return "save more"

print(add_10(110))
print(add_10(50))

def subtract_bc(a,b,c):
    result = a - b * c
    print ('Parameter a equals', a)
    print ('Parameter b equals', b)
    print ('Parameter c equals', c)
    return result

print(subtract_bc(10,3,2))
print(subtract_bc(a=5,b=3,c=2))

#Funções matemáticas

#def list_n(a,b,c):
    #max(list)
    #result1 = min(list)
    #result1 = sum(list)
    #round(3.555,2)
    #pow(2,3)
    #len('Mathematics')
    #return max
#list_n(1, 2, 3)
