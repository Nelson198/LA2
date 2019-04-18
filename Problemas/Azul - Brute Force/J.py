import sys

def main():
    items = []
    cap_saco = int(sys.stdin.readline().rstrip())
    for x in sys.stdin:
        items.append(int(x.rstrip()))
    
    soma = sum(items)
    print(soma//cap_saco)

main()