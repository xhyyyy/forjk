import sys,datetime
import time

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import qdarkstyle
from read_serial import Read_serial


from newui import DrawingUI,Drawing_star,The_three_body,The_user_keys
class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.framelist = []
        self.initUI()



    def initUI(self):
        self.resize(1550, 843.75)
        self.the_LONG = 100
        self.widget_list = []
        self.setFixedSize(self.width(), self.height())
        self.setWindowTitle('测试UI')
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.the_new = DrawingUI(self)
        star_x = 50
        self.the_new.move(star_x,200)
        self.widget_list.append(self.the_new)
        self.the_new2 = DrawingUI(self)
        self.the_new2.move(star_x+250, 200)
        self.widget_list.append(self.the_new2)
        self.the_new3 = DrawingUI(self)
        self.the_new3.move(star_x+500, 200)
        self.widget_list.append(self.the_new3)
        self.the_new4 = DrawingUI(self)
        self.the_new4.move(star_x+750, 200)
        self.widget_list.append(self.the_new4)
        self.the_new5 = DrawingUI(self)
        self.the_new5.move(star_x+1000, 200)
        self.widget_list.append(self.the_new5)
        self.the_new6 = DrawingUI(self)
        self.the_new6.move(star_x+1250, 200)
        self.widget_list.append(self.the_new6)



        # #日字形按钮
        # self.button_myself = The_three_body(self)
        # self.button_myself.move(200, 100)


        #标签文字
        self.the_text_1 = QLabel(self)
        self.the_text_1.setStyleSheet("font-weight: bold;color:green")
        self.the_text_1.resize(400,100)
        self.the_text_1.setText("当前按键的值：   0  ")
        self.the_text_1.move(500,700)


        self.the_text_2 = QLabel(self)
        self.the_text_2.setStyleSheet("font-weight: bold;color:green")
        self.the_text_2.resize(400, 50)

        self.the_text_2.move(500, 50)

        #下拉菜单
        self.the_down_box = QComboBox(self)
        self.the_down_box.addItem('16按键')
        self.the_down_box.addItem('24按键')
        self.the_down_box.currentIndexChanged.connect(self.the_down_box_change)
        self.the_down_box.move(100,50)
        #按键
        self.init_key()

        #self.grabKeyboard()
        self.btn = QPushButton('关闭', self)
        self.btn.clicked.connect(QCoreApplication.instance().quit)
        self.btn.move(1520,0)
        self.task_2 = Thread_serial(self.framelist)
        self.task_2.the_out_signal.connect(self.show_head)
        self.task_2.start()
        self.task_3 = Thread_move_by_serial()
        self.task_3.the_signal.connect(self.move_by_serial)
        self.task_3.start()

        self.show()

    def show_head(self,str):

        self.the_text_2.setText(f'提示信息： {str}')


    def init_key(self):
        self.key_list_16 = []
        for i in range(0, 16):
            key = The_user_keys(self)
            key.label_key.setText(f'KEY {i + 1}')
            key.move(i * 90 + 50, 500)
            self.key_list_16.append(key)
        self.key_list_24 =[]
        for i in range(0,24):
            key = The_user_keys(self)
            key.label_key.setText(f'KEY {i + 1}')
            if i <12:
                key.move(i * 90 + 50, 1800)
            else:
                key.move((i-12)*90 +50,1800 )
            self.key_list_24.append(key)



    def the_down_box_change(self):
        if self.the_down_box.currentIndex() == 0:
            for widget in self.key_list_24:
                widget.move(1800, 1800)


            for i,key_16 in enumerate(self.key_list_16):
                key_16.move(i * 90 + 50, 500)

        #添加24按键切换逻辑
        else:
            for widget in self.key_list_16:
                widget.move(1800,1800)

            for i,key_24 in enumerate(self.key_list_24):
                if i <12:
                    key_24.move(i * 90 + 240, 500)
                else:
                    key_24.move((i-12)*90+240,600)




    def move_by_serial(self):

        # 补充逻辑
        #摇杆、旋钮逻辑
        for n,w in enumerate(self.widget_list):
            try:
                w.move_by_serial(self.framelist[-1][2 * n + 2], self.framelist[-1][2 * n + 3])
                w.led_1.display(self.framelist[-1][2 * n + 3])
                w.led_2.display(self.framelist[-1][2 * n + 2])

            except Exception as e:
                pass
                #print(e)
        # 按键的逻辑

        if self.the_down_box.currentIndex() == 0:
            try:
                keys = format(self.framelist[-1][0],"#018b")
                self.show_key_value(keys, self.framelist[-1][0])
                #print(keys)
                for i in range(0,16):
                    #i+2是因为#o18b  ob 10000
                    self.key_list_16[i].key_down(keys[i+2])

            except Exception as e:
                pass
                #print(e)
        else:
            try:
                key_value_24 = int(self.framelist[-1][14],16)
                keys = format(key_value_24,"#026b")
                #print(f'24按键:值{ self.framelist[-1][14]},{format(key_value_24,"#026b")}')
                self.show_key_value(keys, key_value_24)
                for i in range(0,24):
                    self.key_list_24[i].key_down(keys[i + 2])

            except Exception as e:
                pass




    def show_key_value(self,value,hexvalue):
        self.the_text_1.setText(f"当前按键的值(二进制)：    {value}\n"
                                f"\n"
                                f"当前按键的值（十六进制）: {hex(hexvalue)} ")

    #键盘逻辑 可删除 留作参考
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
    the_out_signal = pyqtSignal(str)
    def __init__(self,framelist,):
        super(Thread_serial,self).__init__()
        self.framelist = framelist
    def run(self):
        the_task = Read_serial(self.framelist)
        the_task.serial_signal.connect(self.show_text)
        the_port = the_task.start_read_serial()
        if  the_port !=None:
            the_task.start_read(the_port)

        print('读取串口报错了')

    def show_text(self,text):
        self.the_out_signal.emit(text)



class Thread_move_by_serial(QThread):
    the_signal = pyqtSignal()
    def __init__(self,):
        super(Thread_move_by_serial,self).__init__()

    def run(self):
        while 1:
            self.the_signal.emit()
            # fps 66帧 windows平台1/0.15
            time.sleep(0.01)



if __name__ == '__main__':
    app=QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    demo = Example()
    sys.exit(app.exec_())