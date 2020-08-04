'''
Author: MulaRoakee
Date: 2020-08-04 06:23:05
LastEditTime: 2020-08-04 10:28:39
LastEditors: MulaRoakee
Description: 自动刷魂能脚本儿 硬要求高 自娱自乐型 泛用性差
'''
       
import pyautogui as au
import time

# FIXME: 自动识别闪退重开游戏（23333

active_reward = 'active_reward.png'
fight = 'fight.png'
arrow1 = 'arrow1.png'
arrow2 = 'arrow2.png'
see_ghost = 'see_ghost.png'
challenge = 'challenge.png'
five = 'five.png'

'''
description: 这个就厉害了（不是）
             在界面找到对应的图并进行（偏差）点击
param 图片（路径？ 
return 无
'''
def find_and_click(image):

    # 刚开始先看看是不是见鬼了
    if_see_ghost()

    # 刚开始先点一下活动奖励下面一些（即聚焦游戏窗口
    if image == active_reward:
        try:
            x, y = au.locateCenterOnScreen(image,confidence=0.9)
            au.click(x, y+200)
            print("click {0} {1}".format(x,y))
        except:
            print("没找到图片")
    
    elif image == arrow1:
        try:
            x, y = au.locateCenterOnScreen(image,confidence=0.6)
            print("down {0} {1}".format(x,y))
            au.mouseDown(x+20, y+300)
            time.sleep(6)
            au.mouseUp()
            
        except:
            print("没找到图片")
    elif image == challenge:
        try:
            x, y = au.locateCenterOnScreen(image,confidence=0.9)
            au.click(x, y)
            print("click {0} {1}".format(x,y))

            show_count_down(5)
            au.click(x,y-300)
        except:
            print("没找到图片")

    elif image == fight:
        try:
            x, y = au.locateCenterOnScreen(five,confidence=0.9)
            au.click(x,y)
            print("click {0} {1}".format(x,y))
            show_count_down(5)
        finally:
            try:
                x, y = au.locateCenterOnScreen(image,confidence=0.9)
                au.click(x, y)
                print("click {0} {1}".format(x,y))
            except:
                print("没找到图片")

    else:
        try:
            x, y = au.locateCenterOnScreen(image,confidence=0.9)
            au.click(x, y)
            print("click {0} {1}".format(x,y))
        except:
            print("没找到图片")

        
'''
description: 从挑战列表开始 （直接点击的开战
param 无
return 无
'''
def from_list_begin():

    find_and_click(active_reward)

    show_count_down(1)
    find_and_click(fight)# 点一下出战 ...woc 没加confidence找不到


    show_count_down(5)
    find_and_click(fight)# 再点一下出战
    au.move(0,-300)

    show_count_down(15)
    find_and_click(arrow1)# 等完缓冲向前走 打第一波怪

    show_count_down(15)
    find_and_click(arrow1)# 打第二波怪

    show_count_down(15)
    find_and_click(arrow1)# 打第三波怪

    show_count_down(20)
    find_and_click(arrow2)# 结算界面退出

    show_count_down(10)
     
'''
description: 延时的时候在cmd显示倒计时。。。
param x:时间
return 无
'''
def show_count_down(x:int):
    print("In count down: ",end = '')
    while x > 0 :
        print(x,end=' ')
        x -= 1
        time.sleep(1)
    print()
    
'''
description: 触发这个函数说明见鬼了（游戏闪退
param 无
return true：游戏闪退
       false: 游戏正常
'''  
def if_see_ghost():
    try:
        x, y = au.locateCenterOnScreen(see_ghost,confidence=0.9)
        au.click(x, y)
        show_count_down(40)
        au.click(x,y)

        show_count_down(40)
        find_and_click(challenge)
        show_count_down(10)

        while 1:
            from_list_begin()
        
    except:
        return
     
    
if __name__ == "__main__":
    while 1:
        from_list_begin()