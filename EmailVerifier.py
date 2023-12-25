import re
def fun(s):
    if matches := re.search(r"^([A-Za-z0-9\_\-])+@([A-Za-z0-9])+\.([a-zA-Z]){1,3}$",s):
        return True
    else:
        False

def filter_mail(emails):
    filtered = filter(fun,emails)
    return filtered

def get_num():
    while True:
        try:
            n = int(input())
            return n
        except ValueError:
            pass

def main():
    n = get_num()
    emails = []
    for _ in range(n):
        email = input()
        emails.append(email)
    print(sorted(filter_mail(emails)))

if __name__ == "__main__":
    main()