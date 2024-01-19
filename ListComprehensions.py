def main():
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    l1 = [[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1)]
    l2 = list()
    
    for _ in l1:
        if checkSum(_,n):
            l2.append(_)

    print(l2)

def checkSum(l,n):
    return l[0] + l[1] + l[2] != n

if __name__ == "__main__":
    main()