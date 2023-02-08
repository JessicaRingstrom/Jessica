import random
num1, num2 = 30, 50
for i in range(0,10) :
    print (random.randrange(num1, num2))

import random
x = random.random()
for i in range(1,10) :
    print(random.random())

import random
def trunc_gauss(mu, sigma, bottom, top):
    a = random.gauss(mu,sigma)
    while (bottom <= a <= top) == False:
        a = random.gauss(mu,sigma)
    return a

n=1
while n<=100:
    print(n)
    n=n+1
    if n==50:
        break
        print(n)
        print("finished with first example")

x = input("skriv ett djur: ")
y = int(input("skriv ett tal: "))
try:
    print(x + y)

