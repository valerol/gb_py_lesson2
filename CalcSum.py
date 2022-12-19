# Task 1
numberChars = list(input('Enter number '))
res = 0

for char in numberChars:
    try:
        res += int(char)
    except:
        continue

print("Sum = " + str(res))
