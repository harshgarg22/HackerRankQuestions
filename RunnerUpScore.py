def main():
    n = int(input()) #number of elements
    arr = map(int, input().split()) #list from the user
    arr = sorted(arr, reverse= True)
    print(runner(arr,n))

def runner(arr,n):
    for i in range(n-1):
        for j in range(1,n):
            if arr[i] != arr[j]:
                return arr[j]

if __name__ == "__main__":
    main()