from itertools import permutations

def anagram(word, length):
    return sorted(list(set(permutations(word, length))))

def main():
    word = input().strip()
    length = len(word)

    if length <= 1:
        print(word)
    else:
        a = anagram(word, length)
        for x in a:
            print("{0}".format(''.join(x)))

main()