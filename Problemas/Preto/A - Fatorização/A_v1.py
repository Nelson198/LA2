def fatoriza(n):
    a = 2
    while n > 1 and n < 1000000000:
        while a <= n:
            if n % a == 0:
                print(a)
                n = n // a
            else:
                a += 1

def main():
    n = int(input().strip())
    fatoriza(n)

main()