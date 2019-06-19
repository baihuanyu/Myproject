# 小游戏 用户猜数字
import random
secret = random.randint(1,10)
# 初始化 可用次数
times = 3
while times :
    num = input('你猜猜我心里想的什么数字？：')
    #isdigit() 表示的是数字
    if num.isdigit():
        num = int(num)
        if num == secret :
            print('你是我肚子里的蛔虫吗？ 这都被你猜对了')
            print('哼哼， 猜对了也没有奖励！')
            break
        elif num > secret :
            print('哎呀！ 大了打了！！')
            times = times -1
        else:
            print('小了小了！！')
            times -=1
    else:
        print('叫你输入数字!')
print('不玩啦 游戏结束！')
