
m = 1000
ordmax = 30
primes = [0 for i in range(m + 1)]
mult = [0 for i in range(ordmax + 1)]
j = 1
k = 1
primes[1] = 2
ord = 2
square = 9

while k < m:
    j += 2

    if j == square:
        ord += 1
        square = primes[ord] ** 2
        mult[ord - 1] = j

    n = 2
    jprime = True

    while n < ord and jprime:
        while mult[n] < j:
            mult[n] = mult[n] + 2 * primes[n]

        if mult[n] == j:
            jprime = False

        n += 1

    if jprime:
        k += 1
        primes[k] = j

print(primes)
input()
