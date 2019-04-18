from fractions import gcd

def main():
    num1, num2 = map(int, input().strip().split())
    print(gcd(num1, num2))

main()