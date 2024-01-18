def main():
    n = int(input().strip())
    if (n%2 != 0) or (n%2 == 0 and 6<=n<=20):
        print("Weird")
    elif (n%2 == 0 and 2<=n<=5) or (n%2 == 0 and n>20):
        print("Not Weird")

if __name__ == "__main__":
    main()