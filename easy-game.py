"""
透過while 和 if 
A=0
在迴圈中
輸入數字
並判斷
A和輸入的數字大小
並印出結果
一直重複此迴圈
直到
輸入的數字大小等於A
才離開迴圈
"""
print("練習題5")
while True:

    num = input("A的數字: 按下q 就結束迴圈 結束遊戲\n")
    if num=="q":
        break
    num = int(num)                                # 終極密碼的數字
    start = 0                                     # 最小的變數數字
    end = 99                                      # 最大的變數數字
    while True:
        str1= "要猜的數字"+ str(start) +"~"+ str(end)+"的數字:\n"
        num1 = input(str1)
        num1 = int(num1)
        if num ==num1:
            print("答對了")
            break
        if num1<num:                            # 猜的數字 小於 終極密碼的數字
            start=num1                            # 修改 最小的變數數字
            print("比猜的數字在大")
        if num1>num:                            # 猜的數字 大於 終極密碼的數字
            end=num1                              # 修改 最大的變數數字
            print("比猜的數字在小")
"""
6..)  
透過while 和 if 
在迴圈中
輸入數字
如果此次輸入的數字大於上次輸入的數字，就繼續迴圈，
但如果這次的數字小餘上次的數字，就離開迴圈
"""
print("練習題7")
num = input("輸入終極密碼的數字: 按下q 就結束迴圈 結束遊戲\n")
start = 0  # 最小的變數數字
end = 99  # 最大的變數數字
while True:

    str1 = "要猜的數字" + str(start) + "~" + str(end) + "的數字:\n"
    num1 = input(str1)
    num1 = int(num1)
    if num==num1:
        break

    num = int(num)                                # 終極密碼的數字
    if num1<num:                            # 猜的數字 小於 終極密碼的數字
        start=num1                            # 修改 最小的變數數字
        print("比猜的數字在大")
    if num1>num:                            # 猜的數字 大於 終極密碼的數字
        end=num1                              # 修改 最大的變數數字
        print("比猜的數字在小")
print("猜對了")
"""
7..)  
透過while 和 if 
做一個猜0~99數字的遊戲
例如： 
未知數為=66
輸入:
B=50 
印出
 未知數在 50~99 之間
再輸入
B=77
印出
 未知數在 50~77 之間
再輸入
B=60
印出
 未知數在 60~77 之間
再輸入
B=70
印出
 未知數在 60~70 之間
再輸入
B=66
印出
 猜對了
"""
print("練習題7")
num = input("輸入終極密碼的數字: 按下q 就結束迴圈 結束遊戲\n")
start = 0  # 最小的變數數字
end = 99  # 最大的變數數字
while True:

    str1 = "要猜的數字" + str(start) + "~" + str(end) + "的數字:\n"
    num1 = input(str1)
    num1 = int(num1)
    if num==num1:
        break

    num = int(num)                                # 終極密碼的數字
    if num1<num:                            # 猜的數字 小於 終極密碼的數字
        start=num1                            # 修改 最小的變數數字
        print("比猜的數字在大")
    if num1>num:                            # 猜的數字 大於 終極密碼的數字
        end=num1                              # 修改 最大的變數數字
        print("比猜的數字在小")
print("猜對了")