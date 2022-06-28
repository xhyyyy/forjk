import sys,math
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import qdarkstyle

from newui import DrawingUI,Drawing_star
class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.resize(1500, 843.75)
        self.setFixedSize(self.width(), self.height())
        self.setWindowTitle('测试UI')
        self.setWindowFlags(Qt.FramelessWindowHint)


        self.the_new = DrawingUI(self)
        self.the_new.move(200,200)
        self.the_new2 = DrawingUI(self)
        self.the_new2.move(450, 200)
        self.the_2 = Drawing_star(self)
        self.the_2_x = 195
        self.the_2_y = 195
        self.the_2.move(self.the_2_x, self.the_2_y)

        self.setWindowTitle('test')
        self.grabKeyboard()
        self.btn = QPushButton('关闭', self)
        self.btn.clicked.connect(QCoreApplication.instance().quit)
        self.btn.move(1470,0)
        self.show()

    def keyPressEvent(self, QKeyEvent):
        if QKeyEvent.key()==Qt.Key_Down:
            print('按了下')
            self.the_2_y +=5
            self.the_2.move(self.the_2_x, self.the_2_y)
        if QKeyEvent.key()==Qt.Key_Up:
            print('按了上')
            self.the_2_y -=5
            self.the_2.move(self.the_2_x, self.the_2_y)
        if QKeyEvent.key()==Qt.Key_Left:

            self.the_2_x -=5
            self.the_2.move(self.the_2_x, self.the_2_y)
        if QKeyEvent.key()==Qt.Key_Right:

            self.the_2_x +=5
            self.the_2.move(self.the_2_x, self.the_2_y)

if __name__ == '__main__':
    app=QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    demo = Example()
    sys.exit(app.exec_())