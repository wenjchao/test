while 'TRUE':
    a = 0
    print("請輸入五個數字")
    num = list()
    for i in  range(5):
        temp = input("")
        num.append(temp)
    num.sort()
    for j in range(4):
        if num[j] == num[j+1]:
            a = 1
    if a == 1:
        break
    print("第二大的數是：", num[3] ,"第二小的數是：", num[1])
print("你的數字重複了喔")
