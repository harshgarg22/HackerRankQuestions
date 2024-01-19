def main():
    n = int(input())
    student_marks = dict()
    for _ in range(n):
        name, *mark = input().split(" ")
        marks = list(map(float, mark))
        student_marks[name] = marks

    query = input()
    query_marks = student_marks[query]
    sum = 0
    for i in query_marks:
        sum += i
    
    avg = sum/len(query_marks)
    print(f"{avg:.2f}")
if __name__ == "__main__":
    main()