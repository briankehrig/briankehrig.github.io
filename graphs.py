from sympy import isprime
import matplotlib.pyplot as plt

def centPrimes(x):
    return sum(isprime(n) for n in range(x,x+100))

def graph1(n):
    x = [centPrimes(y*100) for y in range(0,n)]
    #fig, ax = plt.subplots()
    
    plt.grid(True, 'major', 'y')
    bars = plt.bar(range(len(x)), x, color='#20b020')
    for i in range(n):
        if i%20 >= 10:
            bars[i].set_color('#1090d0')
    plt.xticks(range(0,n+1,2))
    plt.tick_params(axis='both', which='major', labelsize=16)
    plt.xlabel('Century', fontsize=20)
    plt.ylabel('# of primes', fontsize=20)
    plt.show()

graph1(10)
