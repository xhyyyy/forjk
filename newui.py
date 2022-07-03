from PyQt5.QtGui import *
from PyQt5.QtWidgets import QWidget,QLCDNumber,QLabel
from PyQt5.QtCore import *


class DrawingUI(QWidget):

    def __init__(self,parent=None):
        super(DrawingUI,self).__init__(parent)
        self.resize(250, 250)
        self.the_star = Drawing_star(self)
        #放置靶星 移动速度默认为2
        self.the_star_move_speed = 2
        self.the_star_x = 95
        self.the_star_y = 95
        self.move_star()
        self.LED_init()


    def LED_init(self):
        self.led_1 = QLCDNumber(self)
        self.led_1.setDigitCount(5)
        self.led_1.setSegmentStyle(QLCDNumber.Flat)
        self.led_1.setStyleSheet("color: green;")
        self.led_1.display(-1000)
        self.led_1.move(40,210)

        self.led_2 = QLCDNumber(self)
        self.led_2.setDigitCount(5)
        self.led_2.setSegmentStyle(QLCDNumber.Flat)
        self.led_2.setStyleSheet("color: green;")
        self.led_2.display(-1000)
        self.led_2.move(140,210)

        self.txt_x = QLabel(self)
        self.txt_x.setFont(QFont("Roman times",10))
        self.txt_x.resize(40,20)
        self.txt_x.setText('X轴：')
        self.txt_x.setStyleSheet("color: green;")
        self.txt_x.move(0,215)

        self.txt_y = QLabel(self)
        self.txt_y.resize(40,20)
        self.txt_y.setText('Y轴：')
        self.txt_y.setStyleSheet("color: green;")
        self.txt_y.move(100,215)


    def paintEvent(self,event):
        #初始化绘图工具
        qp=QPainter()
        #开始在窗口绘制
        qp.setRenderHints(QPainter.Antialiasing | QPainter.TextAntialiasing)
        qp.begin(self)
        #自定义画点方法
        self.drawPoints(qp)
        #结束在窗口的绘制
        qp.end()

    #GUI绘制
    def drawPoints(self,qp):
        pen = QPen(Qt.green, 1, Qt.DotLine)
        qp.setPen(pen)
        #虚线画圆
        startx = 0
        starty = 0
        the_long = 200
        qp.drawEllipse(startx,starty,the_long,the_long)
        # 虚线画长方形
        qp.drawRect(startx, starty, the_long, the_long)
        pen = QPen(Qt.green, 1, Qt.SolidLine)
        qp.setPen(pen)
        #实线画线
        qp.drawLine(startx+the_long/2, starty, startx+the_long/2, starty+the_long)
        qp.drawLine(startx, starty+the_long/2, startx+the_long, starty+the_long/2)
        #短线 X轴
        qp.drawLine(startx + the_long / 2 - 5, starty + (the_long / 2) * 1 / 3, startx + the_long / 2 + 5,
                    starty + (the_long / 2) * 1 / 3)
        qp.drawLine(startx+the_long/2-5, starty+(the_long/2)*2/3, startx+the_long/2+5, starty+(the_long/2)*2/3)
        qp.drawLine(startx + the_long / 2 - 5, starty + (the_long / 2) * 4 / 3, startx + the_long / 2 + 5,
                    starty + (the_long / 2) * 4 / 3)
        qp.drawLine(startx + the_long / 2 - 5, starty + (the_long / 2) * 5 / 3, startx + the_long / 2 + 5,
                    starty + (the_long / 2) * 5 / 3)
        # 短线 Y轴
        qp.drawLine(startx + (the_long / 2) * 1 / 3, starty + the_long / 2 - 5,startx + (the_long / 2) * 1 / 3, starty + the_long / 2 + 5)
        qp.drawLine(startx + (the_long / 2) * 2 / 3, starty + the_long / 2 - 5,startx + (the_long / 2) * 2 / 3, starty + the_long / 2 + 5)
        qp.drawLine(startx + (the_long / 2) * 4 / 3, starty + the_long / 2 - 5,startx + (the_long / 2) * 4 / 3, starty + the_long / 2 + 5)
        qp.drawLine(startx + (the_long / 2) * 5 / 3, starty + the_long / 2 - 5,startx + (the_long / 2) * 5 / 3, starty + the_long / 2 + 5)

        brush = QBrush(Qt.SolidPattern)
        brush.setColor(QColor(255,0,0))
        qp.setBrush(brush)
        qp.drawEllipse(startx+the_long/2-2, starty+the_long/2-2, 4, 4)

    def move_star(self):
        self.the_star.move(self.the_star_x, self.the_star_y)

    def move_star_up(self):
        if self.the_star_y >-5:
            self.the_star_y -=  self.the_star_move_speed
            self.move_star()

    def move_star_down(self):
        if self.the_star_y <195:
            self.the_star_y +=  self.the_star_move_speed
            self.move_star()

    def move_star_left(self):
        if self.the_star_x >-5:
            self.the_star_x -=  self.the_star_move_speed
            self.move_star()

    def move_star_right(self):
        if self.the_star_x <195:
            self.the_star_x +=  self.the_star_move_speed
            self.move_star()

    def move_by_serial(self,y,x):
        # y,x -1000~1000
        #print(f"收到的参数{x},{y}")
        self.the_star_y = 100 - (y / 10)-5
        self.the_star_x = 100 + (x / 10)-5
        self.move_star()



class Drawing_star(QWidget):

    def __init__(self,parent=None):
        super(Drawing_star,self).__init__(parent)
        self.resize(20,20)

    def paintEvent(self,event):
        #初始化绘图工具
        qp=QPainter()
        #开始在窗口绘制
        qp.setRenderHints(QPainter.Antialiasing | QPainter.TextAntialiasing)
        qp.begin(self)
        #自定义画点方法
        self.drawPoints(qp)
        #结束在窗口的绘制
        qp.end()

    #GUI绘制
    def drawPoints(self,qp):

        brush = QBrush(Qt.SolidPattern)
        brush.setColor(QColor(0,255,0,100))
        qp.setBrush(brush)
        qp.drawEllipse(0, 0, 10, 10)


class The_three_body(QWidget):
    def __init__(self, parent=None):
        super(The_three_body, self).__init__(parent)
        self.resize(21, 61)
        self.obj = The_three_body_obj(self)
        self.obj_begin_x = 0
        self.obj_begin_y = 20
        self.obj.move(self.obj_begin_x,self.obj_begin_y)


    def paintEvent(self, event):
        qp=QPainter()
        qp.begin(self)
        self.drawPoints(qp)
        qp.end()

    def drawPoints(self, qp):
        pen = QPen(Qt.green, 1, Qt.SolidLine)
        qp.setPen(pen)
        qp.drawRect (0,0,20,60)
        qp.drawLine(0,20,20,20)
        qp.drawLine(0, 40, 20, 40)

    def up_move(self):
        if self.obj_begin_y >19:
            self.obj_begin_y -= 20
            self.obj.move(self.obj_begin_x, self.obj_begin_y)

    def down_move(self):
        if self.obj_begin_y <40:
            self.obj_begin_y += 20
            self.obj.move(self.obj_begin_x, self.obj_begin_y)




class The_three_body_obj(QWidget):

    def __init__(self,parent=None):
        super(The_three_body_obj,self).__init__(parent)
        self.resize(20,20)

    def paintEvent(self,event):
        #初始化绘图工具
        qp=QPainter()
        #开始在窗口绘制
        qp.setRenderHints(QPainter.Antialiasing | QPainter.TextAntialiasing)
        qp.begin(self)
        #自定义画点方法
        brush = QBrush(Qt.SolidPattern)
        brush.setColor(QColor(0,255,0))
        qp.setBrush(brush)
        qp.drawRect(0, 0, 20, 20)
        #结束在窗口的绘制
        qp.end()


class The_user_keys(QWidget):
    def __init__(self,parent=None,):
        super(The_user_keys,self).__init__(parent)
        self.resize(63, 63)
        self.label_key = QLabel(self)

        self.label_key.move(10,22)
        self.down_obj = The_user_key_obj(self)
        self.down_obj.move(100,100)


    def paintEvent(self,event):
        #初始化绘图工具
        qp=QPainter()
        #开始在窗口绘制
        qp.setRenderHints(QPainter.Antialiasing | QPainter.TextAntialiasing)
        qp.begin(self)
        #自定义画点方法

        pen = QPen(Qt.green, 1, Qt.SolidLine)
        qp.setPen(pen)
        qp.drawRect(0, 0, 62, 62)
        qp.drawRect(6, 6, 50, 50)
        #结束在窗口的绘制
        qp.end()

    #按下变亮 传入值需要是1 int类型
    def key_down(self,the_value):
        if the_value == '1':
            self.down_obj.move(8,8)
        else:
            self.down_obj.move(100, 100)


class The_user_key_obj(QWidget):

    def __init__(self,parent=None):
        super(The_user_key_obj,self).__init__(parent)
        self.resize(44,44)

    def paintEvent(self,event):
        #初始化绘图工具
        qp=QPainter()
        #开始在窗口绘制
        qp.setRenderHints(QPainter.Antialiasing | QPainter.TextAntialiasing)
        qp.begin(self)
        #自定义画点方法
        brush = QBrush(Qt.SolidPattern)
        brush.setColor(QColor(0,255,0))
        qp.setBrush(brush)
        qp.drawRect(1, 1, 42, 42)
        #结束在窗口的绘制
        qp.end()









