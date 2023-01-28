def calculatePrime(a,b):
    count = 0
    for i in range(a,b+1):
        if i > 1:
            for j in range(2,i):
                if (i % j) == 0:
                    break
            else:
                count += 1
    return count

a = input()
b = input()

print(calculatePrime(a,b))