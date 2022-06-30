import serial,struct


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


class Read_serial:

    def __init__(self,framelist):
        try:

            self.the_com = serial.Serial('com12', 115200)
        except Exception  as e:
            print(e)
            return None
        self.framelist =framelist
        self.start_read()


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
                        keys, ledstatus, L1Y, L1X, R1Y, R1X, L2Y, L2X, ROLL = struct.unpack(
                            '<2H7h',
                            bytearray.fromhex(data[8:44]))  # 2个unsigned short 范围是0-65535 解析前8字节，7个short,解析中间14字节小端

                        readnum += 1
                        self.framelist.append([keys, ledstatus, L1Y, L1X, R1Y, R1X, L2Y, L2X, ROLL, readnum])
                        #1print(L1Y, L1X, R1Y, R1X, L2Y, L2X, ROLL)
                        if len(self.framelist) > 86400:
                            self.framelist.clear()
                    else:
                        pass




if __name__ == '__main__':
    test = Read_serial()