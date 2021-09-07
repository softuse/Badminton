#!/usr/bin/python
# if __name__ := '__main__':

#     print("Hello, World!");

#根据图片识别定位x,y坐标（比较好用）
# locateCenterOnScreen(image, grayscale=False)
# 返回找到的第一个截图Image对象在屏幕上的中心坐标(x, y)，如果没找到返回None

# auto.locateCenterOnScreen('1.png',grayscale=False)

# #  参数grayscale是是否转灰度

# >>> (1441, 582) 

import pyautogui
import time
import os
import cv2
def AutoOpen(Path):
    
 os.startfile(Path) #os.startfile（）打开外部应该程序，与windows双击相同
#  pyautogui.moveTo(409, 139)#pyautogui.moveTo()将鼠标移动到指定位置
#  time.sleep(6)
#  pyautogui.click(clicks=2)#鼠标点击，实现鼠标双击

#获取图片中心位置
def GetPos(m_path):
    #pyautogui.screenshot()
            
    x=pyautogui.locateCenterOnScreen(m_path)
   # print(m_path,'Get--',x)
   
    return x;
#`获取正确位置`
def GetRightPos(point1,point2,point3):
      
    return [[point2.x,point1.y],[point3.x,point1.y]]

def GoToPosAndClick(path):
    pyautogui.screenshot()
    m_point=GetPos(path)
    while(m_point==None):
        #time.sleep(0.1)
        pyautogui.screenshot()
        m_point=GetPos(path)
        
    pyautogui.moveTo(m_point.x,m_point.y)#pyautogui.moveTo()将鼠标移动到指定位置
    pyautogui.click(clicks=1)#鼠标点击，实现鼠标双击

def getRealtimeMouseCoordinates():
    try:
        xOld = 0
        yOld = 0
        while True:
            xNew, yNew = pyautogui.position()
            if 1==1:
            #if xOld != xNew and yOld != yNew:

                xOld = xNew
                yOld = yNew
                screenshot = pyautogui.screenshot()
                color = screenshot.getpixel((xNew, yNew))
                print('X:', '{:>4}'.format(xNew), ', Y:', '{:>4}'.format(yNew), ', RGB:',
                      '({:>3}, {:>3}, {:>3})'.format(color[0], color[1], color[2]))
            time.sleep(0.1)

    except KeyboardInterrupt:
        print('Exit')
def getRealtimeMouseCoordinates1():
    
    try:
       
        xOld = 0
        yOld = 0
        tmpNum=0
        tmpList=[[908,603],[991,598],[913,558],[983,565],[914,526],[984,526],[911,489],[987,484],[903,434],[997,446]]
        #其他移动的位置
        tmpList1=[[952,737],[1183,813],[1151,258],[1097,186]]
        tmpList.reverse()
        tmpList1.reverse()
        l_Original=len(tmpList1)
        #xNew, yNew = pyautogui.position()
        while(len(tmpList1)>0):
                l=len(tmpList1)
                xNew=tmpList1[l-1][0]
                yNew=tmpList1[l-1][1]
            
                print('X:', xNew, ', Y:', yNew)
                pyautogui.moveTo(xNew, yNew)#pyautogui.moveTo()将鼠标移动到指定位置
                #获取颜色，用于对比
                screenshot = pyautogui.screenshot()
                color = screenshot.getpixel((xNew, yNew))
                print(color)
               
                pyautogui.click(clicks=1)#鼠标点击，实现鼠标双击
                #获取颜色，用于对比
                color1 = screenshot.getpixel((xNew, yNew))
                print('12',color)
                #time.sleep(3)
                while(color[0]==color1[0]):
                    #pyautogui.click(clicks=1)#鼠标点击，实现鼠标双击
                    if l==l_Original:
                        pyautogui.moveTo(1183, 813)
                        color1 =screenshot.getpixel((1183, 813))
                        if color1[0]==90:
                            print('1',color1[0])
                            time.sleep(2.5)
                            break;
                    elif l==l_Original-1:
                        pyautogui.moveTo(1151, 258)

                        color1 =screenshot.getpixel((1151, 258))
                        print('c1',color1[0])
                        if color1[0]!=90:
                            
                            print('c',color1[0])
                            time.sleep(2.3)
                            break;
                    elif l==l_Original-2:
                        print('c2',color1[0])
                        time.sleep(2)
                        break
                    else :
                        print('c3',color1[0])
                        time.sleep(0.5)
                        break;
                    # elif l==l_Original-2:
                    #     color1 ==screenshot.getpixel((904, 299))
                    #     if color1[0]==68:
                    #         print('d',color[0])
                    #         break;
                    print('1321',color1[0])
                    #time.sleep(10.5)
                    #pyautogui.click(clicks=1)#鼠标点击，实现鼠标双击
                 
                    
                    print(color)
                print('121',color1)
                tmpList1.pop() #移除第一个元素

        time.sleep(1)
        pyautogui.moveTo(728, 828)#pyautogui.moveTo()将鼠标移动到指定位置
            
        pyautogui.click(clicks=1)#鼠标点击，实现鼠标双击

        pyautogui.moveTo(908, 603)#pyautogui.moveTo()将鼠标移动到指定位置

        
        pyautogui.scroll(-10000)
        time.sleep(2)
        
        while (tmpNum<3 and len(tmpList)>0) :
            
            #开始抢票
            #l=len(tmpList)
            a=tmpList.pop()
            xNew=a[0]
            yNew=a[1]
            pyautogui.moveTo(xNew, yNew)#pyautogui.moveTo()将鼠标移动到指定位置
            
            screenshot = pyautogui.screenshot()
            color = screenshot.getpixel((xNew, yNew))

            print('123',color)
            
            print('X:', xNew, ', Y:', yNew)
          
            if ( (color[0]==224 and color[1]==224) or (color[0]==224 and color[2]==224) or (color[1]==224 and color[2]==224) ) :
                #tmpList.pop();
                continue
            else:
                '''点击抢单'''
                pyautogui.moveTo(xNew, yNew)#pyautogui.moveTo()将鼠标移动到指定位置
                time.sleep(0.1)
                pyautogui.click(clicks=1)#鼠标点击，实现鼠标双击
                tmpNum=tmpNum+1;
                # if ( (color[0]==224 and color[1]==224) or (color[0]==224 and color[2]==224) or (color[1]==224 and color[2]==224) ) :
                #      ++tmpNum;
                     #tmpList.pop();


            # xNew=tmpList1[0][0]
            # yNew=tmpList1[0][1]
            # print('执行第二部','X:', xNew, ', Y:', yNew)


            # screenshot = pyautogui.screenshot()
            #color = screenshot.getpixel((xNew, yNew))
            # print('X:', '{:>4}'.format(xNew), ', Y:', '{:>4}'.format(yNew), ', RGB:',
            #             '({:>3}, {:>3}, {:>3})'.format(color[0], color[1], color[2]))
            time.sleep(0.1)
            # if ( (color[0]==224 and color[1]==224) or (color[0]==224 and color[2]==224) or (color[1]==224 and color[2]==224) ) :
            #     tmpList.pop();
            #   else
            #      '''点击抢单'''
            #     pyautogui.moveTo(xNew, yNew)#pyautogui.moveTo()将鼠标移动到指定位置
            
            #     pyautogui.click(clicks=1)#鼠标点击，实现鼠标双击
            
            #   if ( (color[0]==224 and color[1]==224) or (color[0]==224 and color[2]==224) or (color[1]==224 and color[2]==224) ) :
            #     ++tmpNum;
            #     tmpList.pop();

            if tmpNum==2:
               
                '''点击提交订单'''
                pyautogui.moveTo(990, 877)#pyautogui.moveTo()将鼠标移动到指定位置
            
                pyautogui.click(clicks=1)#鼠标点击，实现鼠标双击
                 
                pyautogui.moveTo(987, 642)#pyautogui.moveTo()将鼠标移动到指定位置
                time.sleep(4.5)
                pyautogui.click(clicks=1)#鼠标点击，实现鼠标双击
                
                
                pyautogui.moveTo(957, 480)#pyautogui.moveTo()将鼠标移动到指定位置
                time.sleep(3)
                pyautogui.click(clicks=1)#鼠标点击，实现鼠标双击
                break;
        if tmpNum==1:
                '''点击提交订单'''
                pyautogui.moveTo(990, 877)#pyautogui.moveTo()将鼠标移动到指定位置
            
                pyautogui.click(clicks=1)#鼠标点击，实现鼠标双击
                
                pyautogui.moveTo(987, 642)#pyautogui.moveTo()将鼠标移动到指定位置
                time.sleep(4.5)
                pyautogui.click(clicks=1)#鼠标点击，实现鼠标双击
                
                
                pyautogui.moveTo(957, 480)#pyautogui.moveTo()将鼠标移动到指定位置
                time.sleep(3)
                pyautogui.click(clicks=1)#鼠标点击，实现鼠标双击
               
        if(tmpNum==0):
            print('sorry, 未抢到票')   
        elif tmpNum==1:
            print('sorry, 抢到一张票')   
        else:
            print('抢到票啦')   
    except KeyboardInterrupt:
        print('Exit')
def getRealtimeMouseCoordinates2(arg=0):
    try:
       
        tmpNum=0
        tmpList=[r'.\a\pyto\19.png',r'.\a\pyto\18.png',r'.\a\pyto\17.png',r'.\a\pyto\16.png',r'.\a\pyto\15.png',r'.\a\pyto\14.png',r'.\a\pyto\13.png']
        #其他移动的位置
        tmpList1=[r'.\a\pyto\1.png',r'.\a\pyto\2.png',r'.\a\pyto\A.png',r'.\a\pyto\top.png']
        agree=r'.\a\pyto\agree.png'
        xiala=r'.\a\pyto\xiala.png'
        price=r'.\a\pyto\30y.png'
        price2=r'.\a\pyto\50y.png'

        nine2ten=r'.\a\pyto\9.png'
        ten2eleven=r'.\a\pyto\10.png'
        seven2eight=r'.\a\pyto\19.png'
        eight2nine=r'.\a\pyto\20.png'

        commit=r'.\a\pyto\commit.png'
        confirm=r'.\a\pyto\confirm.png'
        pay=r'.\a\pyto\pay.png'

        begin=r'.\a\pyto\11.png'


        tmpList.reverse()
        tmpList1.reverse()
        l_Original=len(tmpList1)
        #xNew, yNew = pyautogui.position()
        while(len(tmpList1)>0):
                l=len(tmpList1)
                path=tmpList1.pop()
                screenshot = pyautogui.screenshot()
                m_point=GetPos(path)
                m_point2=GetPos(begin)
                while(m_point==None and m_point2==None):
                    time.sleep(0.1)
                    m_point=GetPos(path)
                    if(m_point!=None):
                        break;
                    m_point2=GetPos(begin)
                    if(m_point2!=None):
                        m_point=m_point2
                        break;
                    print(path,'None')
                
                if m_point==None:
                    m_point=m_point2
                xNew=m_point.x
                yNew=m_point.y
                if l!=1:
                    pyautogui.moveTo(m_point.x,m_point.y)#pyautogui.moveTo()将鼠标移动到指定位置
                    print('move',m_point)
                else:
                    pyautogui.moveTo(m_point.x,m_point.y+25)#pyautogui.moveTo()将鼠标移动到指定位置
                    print('move',m_point)
              
                # #获取颜色，用于对比
                
                # color = screenshot.getpixel((xNew, yNew))
                
                pyautogui.click(clicks=1)#鼠标点击，实现鼠标双击
                #获取颜色，用于对比
                color1 = screenshot.getpixel((xNew, yNew))
                

        time.sleep(1)
        #先选中同意
        screenshot = pyautogui.screenshot()
        m_point=GetPos(agree)
        while(m_point==None):
            time.sleep(0.1)
            m_point=GetPos(agree)
        xNew=m_point.x
        yNew=m_point.y
        pyautogui.moveTo(m_point.x,m_point.y)#pyautogui.moveTo()将鼠标移动到指定位置
        pyautogui.click(clicks=1)#鼠标点击，实现鼠标双击

        #选中中间部分，下拉
        
        m_point=GetPos(xiala)
        while(m_point==None):
            time.sleep(0.1)
            m_point=GetPos(xiala)
        xNew=m_point.x
        yNew=m_point.y
        pyautogui.moveTo(m_point.x,m_point.y)#pyautogui.moveTo()将鼠标移动到指定位置
        
        pyautogui.scroll(-10000)
        #time.sleep(2)
        if arg==0:

            m_point1=GetPos(nine2ten)
            while(m_point1==None):
                time.sleep(0.1)
                m_point1=GetPos(nine2ten)
            m_point2=GetPos(ten2eleven)
            while(m_point2==None):
                time.sleep(0.1)
                m_point2=GetPos(ten2eleven)

        else:
            #右拉
            pyautogui.press('right',interval=1.5)
            m_point1=GetPos(seven2eight)
            while(m_point1==None):
                time.sleep(0.1)
                m_point1=GetPos(seven2eight)
            m_point2=GetPos(eight2nine)
            while(m_point2==None):
                time.sleep(0.1)
                m_point2=GetPos(eight2nine)

        while (tmpNum<3 and len(tmpList)>0) :
            
            #开始抢票
            #l=len(tmpList)
            screenshot = pyautogui.screenshot()
            path=tmpList.pop()
            m_point=GetPos(path)
            while(m_point==None):
                time.sleep(0.1)
                m_point=GetPos(path)
            fruits=GetRightPos(m_point,m_point1,m_point2)
            #print(fruits)
            for m_point in fruits:
                xNew=m_point[0]
                yNew=m_point[1]
                pyautogui.moveTo(xNew, yNew)#pyautogui.moveTo()将鼠标移动到指定位置
            
                color = screenshot.getpixel((xNew, yNew))
               
                if ( (color[0]==224 and color[1]==224) or (color[0]==224 and color[2]==224) or (color[1]==224 and color[2]==224) ) :
              
                # if (GetPos(price)==None and GetPos(price2)==None) :
                    #tmpList.pop();
                    continue
                else:
                    '''点击抢单'''
                
                    time.sleep(0.1)
                    pyautogui.click(clicks=1)#鼠标点击，实现鼠标双击
                    tmpNum=tmpNum+1;
              
            if tmpNum==2:
               
                '''点击提交订单'''
               
                GoToPosAndClick(commit)
                GoToPosAndClick(confirm)
                GoToPosAndClick(pay)
                
                break;
        if tmpNum==1:
            '''点击提交订单'''
            GoToPosAndClick(commit)
            GoToPosAndClick(confirm)
            GoToPosAndClick(pay)
               
        if(tmpNum==0):
            print('sorry, 未抢到票')   
        elif tmpNum==1:
            print('sorry, 抢到一张票')   
        else:
            print('抢到票啦')   
    except KeyboardInterrupt:
        print('Exit')

#检查是否存在于列表中
def CheckIfExist(list,item):
    for i in list:
        if i==item:
            return True
    return False


def quickRun(num=2,arg=0,count=0):
    '''
     #arg是右拉 ，num是抢场地数量
    
    '''
    
    #直接打开页面不停刷新
    
    tmpNum=0 
    if(num==1): #如果抢一个场地，场地数量起始数量为1，到2停止
        tmpNum=1 
    tmpList=[r'.\a\pyto\19.png',r'.\a\pyto\18.png',r'.\a\pyto\17.png',r'.\a\pyto\16.png',r'.\a\pyto\15.png',r'.\a\pyto\14.png',r'.\a\pyto\13.png',r'.\a\pyto\30.png',r'.\a\pyto\29.png',r'.\a\pyto\28.png',r'.\a\pyto\27.png',r'.\a\pyto\26.png',r'.\a\pyto\25.png']
    #其他移动的位置
    tmpList1=[r'.\a\pyto\1.png',r'.\a\pyto\2.png',r'.\a\pyto\A.png',r'.\a\pyto\top.png']
    agree=r'.\a\pyto\agree.png'
    xiala=r'.\a\pyto\xiala.png'
    price=r'.\a\pyto\30y.png'
    price2=r'.\a\pyto\50y.png'

    nine2ten=r'.\a\pyto\9.png'
    ten2eleven=r'.\a\pyto\10.png'
    seven2eight=r'.\a\pyto\19.png'
    eight2nine=r'.\a\pyto\20.png'

    commit=r'.\a\pyto\commit.png'
    confirm=r'.\a\pyto\confirm.png'
    pay=r'.\a\pyto\pay.png'

    begin= r'.\a\pyto\top.png'
   
    test= r'.\a\pyto\test.png'

    tmpList.reverse()
    tmpList1.reverse()
    l_Original=len(tmpList1)

    #如果到12点 开始点击
    t=time.strftime("%H", time.localtime()) 

    while(t!='12'):
        time.sleep(1)
        t=time.strftime("%H", time.localtime()) 


    m_point=GetPos(begin)
    while(m_point==None):
        #time.sleep(0.1)
        m_point=GetPos(begin)

    pyautogui.moveTo(m_point.x,m_point.y+35)#pyautogui.moveTo()将鼠标移动到指定位置
    print('move',m_point)
    pyautogui.click(clicks=1)#鼠标点击，实现鼠标双击


    
    time.sleep(0.5)
    #先选中同意
    #screenshot = pyautogui.screenshot()
    m_point=GetPos(agree)
    while(m_point==None):
        #time.sleep(0.1)
        m_point=GetPos(agree)
    xNew=m_point.x
    yNew=m_point.y
    pyautogui.moveTo(m_point.x,m_point.y)#pyautogui.moveTo()将鼠标移动到指定位置
    pyautogui.click(clicks=1)#鼠标点击，实现鼠标双击

    #选中中间部分，下拉
    
    m_point=GetPos(xiala)
    while(m_point==None):
        #time.sleep(0.1)
        m_point=GetPos(xiala)
    xNew=m_point.x
    yNew=m_point.y
    pyautogui.moveTo(m_point.x,m_point.y)#pyautogui.moveTo()将鼠标移动到指定位置
    
    pyautogui.scroll(-400)
    directory=0;
    if arg==0: #上午场

        m_point1=GetPos(nine2ten)
        while(m_point1==None):
            #time.sleep(0.1)
            m_point1=GetPos(nine2ten)
        m_point2=GetPos(ten2eleven)
        while(m_point2==None):
            #time.sleep(0.1)
            m_point2=GetPos(ten2eleven)

    else:
        #右拉
        pyautogui.press('right',interval=1.5)
        m_point1=GetPos(seven2eight)
        while(m_point1==None):
                time.sleep(0.1)
                m_point1=GetPos(seven2eight)
        m_point2=GetPos(eight2nine)
        while(m_point2==None):
            #time.sleep(0.1)
            m_point2=GetPos(eight2nine)
    
    positionList=[]
    tmpCount=0
    while (tmpNum<3 and len(tmpList)>0) :
        
        #开始抢票
        #l=len(tmpList)
        screenshot = pyautogui.screenshot()
        path=tmpList.pop()
        m_point=GetPos(path)
        while(m_point==None):
            
            
            if directory==0:
                pyautogui.scroll(400)
                directory=1
            else:
                pyautogui.scroll(-400)
                directory=0
            time.sleep(0.1)
            m_point=GetPos(path)
            

            
        fruits=GetRightPos(m_point,m_point1,m_point2)
        #print(fruits)
        for m_point in fruits:
            xNew=m_point[0]
            yNew=m_point[1]
            
            color = screenshot.getpixel((xNew, yNew))
            
            if ( (color[0]==224 and color[1]==224) or (color[0]==224 and color[2]==224) or (color[1]==224 and color[2]==224) ) :
            
            # if (GetPos(price)==None and GetPos(price2)==None) :
                #tmpList.pop();
                continue
            else:

                '''点击抢单'''
                print('点击抢单',m_point)
                
                if CheckIfExist(positionList,xNew):
                    continue
                
                pyautogui.moveTo(xNew, yNew)#pyautogui.moveTo()将鼠标移动到指定位置
                positionList.append(xNew)
                
                pyautogui.click(clicks=1)#鼠标点击，实现鼠标双击
                tmpNum=tmpNum+1;
            
        if tmpNum==2:
            
            '''点击提交订单'''
            
            GoToPosAndClick(commit)
            GoToPosAndClick(confirm)
            GoToPosAndClick(pay)
            
            break;
        if tmpNum==1:
            '''点击提交订单'''
            GoToPosAndClick(commit)
            GoToPosAndClick(confirm)
            GoToPosAndClick(pay)

    if(tmpNum==0 and count<3):
        #如果没订到票，则刷新，重新走一遍
        
        count+=1
        
        quickRun(num,arg,count)
        
       
    elif tmpNum==1:
        print('sorry, 抢到一张票')   

    elif tmpNum==0:   
        print('sorry, 未抢到票')
        #刷新
    else:
        print('抢到票啦')   
    count=0   
    


def  T(arg=1):
    try:
        print(arg)
        xOld = 0
        yOld = 0
        return True
        if 1==1:
        #if xOld != xNew and yOld != yNew:

            
            yOld
            screenshot = pyautogui.screenshot()
            s=r'.\a\pyto\1.png'
            x=pyautogui.locateCenterOnScreen(s,grayscale=False)
            print(x)
            print(x.x)
            color = screenshot.getpixel((xOld, yOld))
            print('X:', '{:>4}'.format(xOld), ', Y:', '{:>4}'.format(yOld), ', RGB:',
                    '({:>3}, {:>3}, {:>3})'.format(color[0], color[1], color[2]))
        time.sleep(0.1)
    
    except KeyboardInterrupt:
        print('Exit')
if __name__ == '__main__':
 Path=r'C:\Users\Bill\Desktop\苏州奥体中心SZOSC+'

 t=time.strftime("%H", time.localtime()) 
 t2=time.strftime("%H %M", time.localtime()) 
 
 if('2'<'3'):
     print(True)
 print('Fal')
 while t!='11':
    
    time.sleep(1)
    t=time.strftime("%H", time.localtime()) 


t3=time.strftime("%M", time.localtime()) 
while t3<'58':
    
    time.sleep(1)
    t3=time.strftime("%M", time.localtime()) 

AutoOpen(Path)
time.sleep(5.6)
 #getRealtimeMo
#  x=T(2);
#  if(T()):

#     print(x)
quickRun()
t=time.strftime("%H", time.localtime()) 
print(t)
if t=='20':
    print(201)
#getRealtimeMouseCoordinates2()
#T()
#  while True:
#     print("当前鼠标的坐标为：") ;print(pyautogui.position())
#     time.sleep(1)#设置打印的时间间隔


eight2nine=r".\a\pyto\9.PNG"
#s=pyautogui.screenshot()
#print(s)
t=pyautogui.locateCenterOnScreen(eight2nine)
print(t)
pyautogui.moveTo(t.x,t.y)#pyautogui.moveTo()将鼠标移动到指定位置
#GoToPosAndClick(eight2nine)
# m_point2=GetPos(eight2nine)
# while(m_point2==None):
#     time.sleep(0.1)
#     m_point2=GetPos(eight2nine)