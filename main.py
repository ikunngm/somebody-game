import random
from items import *
from settings import *


while True:
    # 游戏循环
    while True:
        # 金币随机增加
        coin += random.randint(coin_scopes[0], coin_scopes[1])
        # 随机暴击
        crit = random.randint(1, int(1/crit_rate))
        if crit == 1:
            king_xp -= 2 * attack
        # 减少道具冷却
        if basketball_time > 0:
            basketball_time -= 1
        else:
            basketball_time = 0
        # 控制
        print('魔王血量还有' + str(king_xp), 'Enter攻击，伤害为' + str(attack), 'B进入商店，金币剩余' + str(coin), 'I使用道具', 'X试图逃跑')
        put = input()
        # 攻击
        if put == '':
            king_xp -= attack
            if crit == 1:
                king_xp -= attack
                print('暴击!')
        # 商店
        elif put == 'B' or put == 'b':
            while True:
                print('商店', '金币剩余' + str(coin))
                print(basketball, '1购买')
                print('选择你要购买的商品吧', 'X离开商店')
                put_shop = input()
                if put_shop == '1':
                    if basketball_state == 0:
                        if coin >= 1000:
                            coin -= 1000
                            basketball_state = 1
                            print('购买成功')
                        else:
                            print('你是想白嫖吗')
                    else:
                        print('太多了......')
                elif put_shop == 'X' or put_shop == 'x':
                    print('离开商店')
                    break
        # 道具
        elif put == 'I' or put == 'i':
            while True:
                if basketball_state == 1:
                    print(basketball, '冷却剩余' + str(basketball_time), '1发动')
                print('选择你要使用的道具吧', 'X取消使用')
                put_prop = input()
                if put_prop == '1':
                    if basketball_time == 0:
                        # 道具'篮球'
                        print(str(king_xp) + '-5')
                        king_xp -= 5
                        print(str(king_xp) + '-5')
                        king_xp -= 5
                        print(str(king_xp) + '-5')
                        king_xp -= 5
                        print(str(king_xp) + '-5')
                        king_xp -= 5
                        print(str(king_xp) + '-5')
                        king_xp -= 5
                        basketball_time = 15
                    else:
                        print('再等等吧')
                elif put_prop == 'X' or put_prop == 'x':
                    print('取消使用')
                    break
        # 逃跑
        elif put == 'X' or put == 'x':
            print('胆小鬼，你逃离了地下城')
            break
        # 战胜
        if king_xp <= 0:
            print('英雄，你战胜了魔王!!!')
            break
    print('任意键重玩', 'X退出')
    put_exit = input()
    if put_exit == 'X' or put_exit == 'x':
        break
