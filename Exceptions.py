def checkError(a,b):
    try:
        return int(int(a)/int(b))
    except ValueError as e1:
        return "Error Code: " + str(e1)
    except ZeroDivisionError as e2:
        return "Error Code: integer division or modulo by zero"
def main():
    inputs = []
    for i in range(int(input())):
        a,b = input().split(" ")
        inputs.append((a,b))
    
    for i in inputs:
        print(checkError(*i))

if __name__ == "__main__":
    main()