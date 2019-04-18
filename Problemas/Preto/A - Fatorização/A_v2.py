def fatoriza(n):
    while n % 2 == 0: 
        print(2)
        n = n // 2

    for i in range(3, int(n**0.5) + 1, 2): 
        while n % i == 0: 
            print(i)
            n = n // i 
              
    # n is a prime number greater than 2 
    if n > 2: 
        print(n)

def main():
    n = int(input().strip())
    if n > 1 and n < 1000000000:
        fatoriza(n)

main()