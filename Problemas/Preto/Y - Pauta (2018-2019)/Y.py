import sys

def main():
    d = {}
    for x in sys.stdin:
        l = x.strip().split()
        if len(l) >= 1:
            if l[0] == '-':
                break
            numero = l[0]
            nome = ' '.join(l[1:])
            if numero not in d:
                d[numero] = [nome]
    
    for x in sys.stdin:
        l = x.strip().split()
        if len(l) >= 1:
            numero = l[0]
            nota = float(l[1])
            if nota - int(float(l[1])) >= 0.5:
                nota = int(float(l[1])) + 1
            else:
                nota = int(float(l[1]))

            if numero in d:
                d[numero].append(nota)

    d_ord = sorted(d, key=lambda x: d[x][0])
    
    for x in d_ord:
        if len(d[x]) == 1:
            print("{0} {1} : {2}".format(x, d[x][0], 'F'))
        else:
            if d[x][1] < 10:
                print("{0} {1} : {2}".format(x, d[x][0], 'R'))
            else:
                print("{0} {1} : {2}".format(x, d[x][0], d[x][1]))

main()