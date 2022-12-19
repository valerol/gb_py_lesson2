# Извините, но видимо я не поняла задачу. 
# Как в результате выражения с одним неизвестным (n) может получиться несколько чисел?
# P:S: объяснили в чате :) Либо я непроницательная, либо задача сформулирована нечетко
def setN():
    inputN = input("Enter n ")
    try:
        return int(inputN)
    except: "Enter correct number "
    setN()

n = setN()
resList = []
resSum = 0

for i in range(1, n+1):
    print(str(i))
    currentRes = (pow((1 + 1/i), i))
    resList.append(round(currentRes, 2))
    resSum +=currentRes

print("Resulting list: " + str(resList))
print("Resulting sum: " + str(round(resSum, 2)))