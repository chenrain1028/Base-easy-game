print("Game1")
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
