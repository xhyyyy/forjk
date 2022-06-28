from PyQt5.QtGui import *
from PyQt5.QtWidgets import QWidget,QPushButton
from PyQt5.QtCore import *


class DrawingUI(QWidget):

    def __init__(self,parent=None):
        super(DrawingUI,self).__init__(parent)
        self.resize(400, 400)


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
        qp.drawEllipse(100,100,200,200)
        # 虚线画长方形
        qp.drawRect(100, 100, 200, 200)
        pen = QPen(Qt.green, 1, Qt.SolidLine)
        qp.setPen(pen)
        #实线画线
        qp.drawLine(200, 100, 200, 300)
        qp.drawLine(100, 200, 300, 200)
        #短线 X轴
        qp.drawLine(195, 167, 205, 167)
        qp.drawLine(195, 134, 205, 134)
        qp.drawLine(195, 233, 205, 233)
        qp.drawLine(195, 266, 205, 266)
        # 短线 Y轴
        qp.drawLine(134, 195, 134, 205)
        qp.drawLine(167, 195, 167, 205)
        qp.drawLine(233, 195, 233, 205)
        qp.drawLine(266, 195, 266, 205)

        brush = QBrush(Qt.SolidPattern)
        brush.setColor(QColor(255,0,0))
        qp.setBrush(brush)
        qp.drawEllipse(198, 198, 4, 4)

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




