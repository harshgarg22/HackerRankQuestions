def main():
    l1 = list()
    scores = list()
    names = list()
    for i in range(int(input())):
        name = input()
        score = float(input())
        l1.append([name,score])
        scores.append(score)
    for i in l1:
        if i[1] == secondLowest(scores):
            names.append(i[0])
    for i in sorted(names):
        print(i)


def secondLowest(scores):
    scores = sorted(scores)
    for i in range(len(scores)-1):
        for j in range(1,len(scores)):
            if scores[i] != scores[j]:
                return scores[j]
    
if __name__ == "__main__":
    main()