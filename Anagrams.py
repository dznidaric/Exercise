import sys

def main(w):
    f = open("wl50.txt", "r")
    w = "".join(sorted(w))
    L = []
    x = 0

    for row in f:
        r = row.replace("\n", "")
        L.append(r)

    
    for el in L:
        if (len(el) == len(w)):
            w2 = "".join(sorted(el))
            if(w == w2):
                x += 1
    
    print(x)

    f.close()

if __name__ == '__main__':
    main(sys.argv[1:])