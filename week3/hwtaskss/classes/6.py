def isPrime(n): 
    if n <= 1: return False
    for i in range(2, n): 
        if n % i == 0: 
            return False; 
            break
  
    return True

def primes_filter(list):
    primes = []
    for l in range(len(list)):
        if isPrime(list[l]):
            primes.append(list[l])
    return primes

x = [int(s) for s in input().split()]
print(primes_filter(x))