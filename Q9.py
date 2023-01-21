lst = []
count = 0
while True:
    x = input("Enter the word: ")
    lst.append(x)
    i = input("Do you want to continue?[Y/N]: ")
    if i.upper() == "N":
        break
len = len(lst)
for i in lst:
    for _ in range(len):
        if i == lst[_]:
            count += 1
    print(i, "occurs", count, "times")
    count = 0