import sys,math,datetime
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import qdarkstyle
from read_serial import Read_serial


from newui import DrawingUI,Drawing_star,The_three_body
class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()
        self.framelist = []
        self.task_2 = Thread_serial(self.framelist)
        self.task_2.start()
        self.task_3 = Thread_move_by_serial(self.framelist)
        self.task_3.start()


    def initUI(self):
        self.resize(1500, 843.75)
        self.the_LONG = 100
        self.widget_list = []
        self.setFixedSize(self.width(), self.height())
        self.setWindowTitle('测试UI')
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.the_new = DrawingUI(self)
        self.the_new.move(200,200)
        self.widget_list.append(self.the_new)
        self.the_new2 = DrawingUI(self)
        self.the_new2.move(450, 200)
        self.widget_list.append(self.the_new2)


        #日字形按钮
        self.button_myself = The_three_body(self)
        self.button_myself.move(200, 100)



        self.grabKeyboard()
        self.btn = QPushButton('关闭', self)
        self.btn.clicked.connect(QCoreApplication.instance().quit)
        self.btn.move(1470,0)

        self.show()

    def keyPressEvent(self, QKeyEvent):


        if QKeyEvent.key()==Qt.Key_Down:
            print('按了下')
            #print(self.framelist[-1])
            for w in self.widget_list:
                w.move_star_down()
            self.button_myself.down_move()
        if QKeyEvent.key()==Qt.Key_Up:
            print('按了上')
            for w in self.widget_list:
                w.move_star_up()
            self.button_myself.up_move()
        if QKeyEvent.key()==Qt.Key_Left:
            for w in self.widget_list:
                w.move_star_left()
        if QKeyEvent.key()==Qt.Key_Right:
            for w in self.widget_list:
                w.move_star_right()




class Thread_serial(QThread):

    def __init__(self,framelist):
        super(Thread_serial,self).__init__()
        self.framelist = framelist
    def run(self):
        the_task = Read_serial(self.framelist)
        print('读取串口报错了')


class Thread_move_by_serial(QThread):


    def __init__(self,joystick_list):
        super(Thread_move_by_serial,self).__init__()
        self.timer = QTimer()
        self.timer.timeout.connect(self.move_by_serial)
        self.joystick_list = joystick_list


    def run(self):
        the_task = self.send_signal()
        print('跑了一次读串口线程')



    def send_signal(self):

        self.timer.setTimerType(Qt.PreciseTimer)

        self.timer.start(1000)




    def move_by_serial(self):
        print('1')
        print(f"{datetime.datetime.now()}接收到串口移动指令\n")
        #补充逻辑


if __name__ == '__main__':
    app=QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    demo = Example()
    sys.exit(app.exec_())