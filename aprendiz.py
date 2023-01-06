# Area de aprendizagem do Python
x = 1

if x > 3:
    print ("case 1")
else:
    print ("case 2")

def compare_to_five(y): # A SEQUENCIA É IMPORTANTE
    if y > 5:
        return "greater" #  -10 > 5 = não
    elif y < 0:
        return "negative" # -10 < 0 = sim -> fim do código
    elif y < 5:
        return "less" # 10 < 5 = sim
    else:
        return "equal" # -10 = 5 = não

print (compare_to_five(-10))


    
