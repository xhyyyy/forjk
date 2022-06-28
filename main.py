import sys,math
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import qdarkstyle

from newui import DrawingUI,Drawing_star,The_three_body
class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.resize(1500, 843.75)
        self.the_LONG = 100
        self.setFixedSize(self.width(), self.height())
        self.setWindowTitle('测试UI')
        self.setWindowFlags(Qt.FramelessWindowHint)


        self.the_new = DrawingUI(self)
        self.the_new.move(200,200)
        self.the_new2 = DrawingUI(self)
        self.the_new2.move(450, 200)
        #日字形按钮
        self.button_myself = The_three_body(self)
        self.button_myself.move(200, 100)




        self.grabKeyboard()
        self.btn = QPushButton('关闭', self)
        self.btn.clicked.connect(QCoreApplication.instance().quit)
        self.btn.move(1470,0)
        self.show()

    def keyPressEvent(self, QKeyEvent):
        the_speed =2
        self.the_star_x = 95
        self.the_star_y = 95
        if QKeyEvent.key()==Qt.Key_Down:
            print('按了下')
            self.the_star_y +=the_speed
            self.the_new.the_star.move(self.the_star_x, self.the_star_y)
            self.the_new2.the_star.move(self.the_star_x, self.the_star_y)
            self.button_myself.down_move()
        if QKeyEvent.key()==Qt.Key_Up:
            print('按了上')
            self.the_star_y -=the_speed
            self.the_new.the_star.move(self.the_star_x, self.the_star_y)
            self.the_new2.the_star.move(self.the_star_x, self.the_star_y)
            self.button_myself.up_move()
        if QKeyEvent.key()==Qt.Key_Left:
            self.the_star_x -=the_speed
            self.the_new.the_star.move(self.the_star_x, self.the_star_y)
            self.the_new2.the_star.move(self.the_star_x, self.the_star_y)
        if QKeyEvent.key()==Qt.Key_Right:
            self.the_star_x +=the_speed
            self.the_new.the_star.move(self.the_star_x, self.the_star_y)
            self.the_new2.the_star.move(self.the_star_x, self.the_star_y)

if __name__ == '__main__':
    app=QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    demo = Example()
    sys.exit(app.exec_())