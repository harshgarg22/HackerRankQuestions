def get_year():
    while True: #Inducing an infinite loop
        year = int(input("Please enter the year:\t"))
        if(1900 <= year <= 100000): #Checking the range of year
            return year
        else:
            print("Enter an year between", str(1900), "and", str(10**5))
            continue

def is_leap(year):
    if((((year % 4) == 0) & (year % 100 !=0))|(year % 400 == 0)):#Leap Year Check
        return True
    else:
        return False

def main():
    year = get_year()
    print(str(is_leap(year)))

main()