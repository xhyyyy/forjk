from PyQt5.QtGui import *
from PyQt5.QtWidgets import QWidget,QPushButton
from PyQt5.QtCore import *


class DrawingUI(QWidget):

    def __init__(self,parent=None):
        super(DrawingUI,self).__init__(parent)
        self.resize(201, 201)
        self.the_star = Drawing_star(self)
        #放置靶星 移动速度默认为2
        self.the_star_move_speed = 2
        self.the_star_x = 95
        self.the_star_y = 95
        self.move_star()


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










