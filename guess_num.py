# 產生一個'隨機整數'1~100(不要印出來)
# 讓使用者重複輸入數字去猜
# 猜對的話 印出 "終於猜對了!"
# 猜錯的話 要告訴他 比答案大/小

import random

start_num = input('請決定隨機數字範圍開始值')
end_num = input('請決定隨機數字範圍結束值')
start_num = int(start_num)
end_num = int(end_num)

r = random.randint(start_num, end_num)
guess_times = 0
while True:
    num = input('請猜數字: ')
    num = int(num)
    guess_times += 1 # guess_times = guess_times + 1 意思一樣
    if num != r:
        if num > r:
            print('比答案大')
        elif num < r:
            print('比答案小')
    else:
        print('終於猜對了!')
        print('共猜了', guess_times, '次! ')
        break
    print('這是你猜第', guess_times, '次')

