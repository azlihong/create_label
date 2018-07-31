#coding:utf-8
import cv2
import os
for i in range(100,101):
    i=str(i)
    p=i+'.mp4'
    m=i+'mp4'
    l=os.path.join('vio',p)
    k=os.path.join('images',m)
    print l
    print k

    vc = cv2.VideoCapture(l) #读入视频文件
    c=0
    rval=vc.isOpened()
    timeF = 1  #视频帧计数间隔频率
    while rval:   #循环读取视频帧
        c = c + 1
        rval, frame = vc.read()
        if(c%timeF== 0): #每隔timeF帧进行存储操作
            if(c%5==0):
                cv2.imwrite(k+str(c) + '.jpg', frame)
                cv2.waitKey(1)
                print(c)
            #存储为图像
        #if rval:
           # cv2.imwrite('driveway-320x240/driveway-320x240'+str(c).zfill(8) + '.jpg', frame) #存储为图像
            #cv2.waitKey(1)
        else:
            break
    vc.release()

