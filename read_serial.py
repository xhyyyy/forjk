import serial,struct,sys,glob
import func_timeout
from func_timeout import func_set_timeout
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QWidget

#读取系统当前可用串口
def useful_ports():
    """ Lists serial port names

        :raises EnvironmentError:
            On unsupported or unknown platforms
        :returns:
            A list of the serial ports available on the system
    """
    if sys.platform.startswith('win'):
        ports = ['COM%s' % (i + 1) for i in range(256)]
    elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
        # this excludes your current terminal "/dev/tty"
        ports = glob.glob('/dev/tty[A-Za-z]*')
    elif sys.platform.startswith('darwin'):
        ports = glob.glob('/dev/tty.*')
    else:
        raise EnvironmentError('Unsupported platform')

    result = []
    for port in ports:
        try:
            s = serial.Serial(port)
            s.close()
            result.append(port)
        except (OSError, serial.SerialException):
            pass
    return result



def crc16_ccitt(strings):  # kermit  初始值0x0000 多项式0x1021 低位在前高位在后，输入输出字节取反
    bytes = bytearray.fromhex(strings)
    crc = 0x0000  # CRC寄存器初始值
    for pos in bytes:
        crc = crc ^ pos  # CRC与第一字节异或
        for i in range(8):  # 按规则循环8次
            if (crc & 1) == 1:  # crc的规则  如果右移位为1
                crc >>= 1  # 右移一位
                crc = crc ^ 0x8408  # 多项式为0x1021 0001 0000 0010 0001 输入取反异或 则为1000 0100 0000 1000 0x 8408
            else:
                crc >>= 1
    crc = crc ^ 0x0000  # 结果与0x0000异或
    return crc





class Read_serial(QWidget):
    serial_signal =pyqtSignal(str)





    def __init__(self,framelist,parent=None):
        super(Read_serial, self).__init__(parent)
        self.framelist =framelist


    def start_read_serial(self):
        try:

            self.the_com = serial.Serial('com4', 115200)
        except Exception  as e:
            self.serial_signal.emit(f"遇到了串口打开错误，错误信息如下{e}\n----------开始尝试其他可用串口------\n")
            port_list = useful_ports()
            for port in port_list:
                try:
                    self.tryserial(port)
                    break
                except func_timeout.exceptions.FunctionTimedOut:
                    print(f"{port}串口不是摇杆")

            self.the_com = serial.Serial(port, 115200)


        print('这一步了')

    @func_set_timeout(0.3)
    def tryserial(self,port_in):
        thecom = serial.Serial(port_in, 115200)
        while 1:
            if thecom.read(1).hex() == 'aa' and thecom.read(1).hex() == '55':
                self.serial_signal.emit(f"识别到帧头，{port_in}可能是摇杆所在串口!!!!测试一下\n如果能正常控制，请修改此串口到com4")
                thecom.close()
                break



    def start_read(self):
        readnum = 0
        while 1:
            while True:
                if self.the_com.read(1).hex() == 'aa' and self.the_com.read(1).hex() == '55':
                    data = 'aa55' + self.the_com.read(30).hex()
                    crc16 = crc16_ccitt(data[0:60])
                    crc16 = format(((crc16 & 0xff) << 8) + (crc16 >> 8), '04x')  # 按16进制小端显示
                    crc_in = data[60:64]
                    # print(crc_in,crc16)
                    if crc16 == crc_in:
                        keys, ledstatus, L1Y, L1X, R1Y, R1X, L2Y, L2X,R2Y,R2X,L3Y,L3X, ROLL = struct.unpack(
                            '<2H11h',
                            bytearray.fromhex(data[8:60]))  # 2个unsigned short 范围是0-65535 解析前8字节，11个short,解析后端字节小端

                        readnum += 1
                        self.framelist.append([keys, ledstatus, L1Y, L1X, R1Y, R1X, L2Y, L2X ,R2Y,R2X,L3Y,L3X,readnum,ROLL])

                        if len(self.framelist) > 86400:
                            self.framelist.clear()
                    else:
                        pass



