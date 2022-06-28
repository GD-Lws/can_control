import ctypes

from Can_Derive import Can_Derive


class Motor_Myactuator(Can_Derive):
    def __init__(self, win_linux=1, send_id=0x141):
        Can_Derive.__init__(self, win_linux=1)
        # self.can_init()
        # self.can_channel_open()
        self.__send_id = send_id
        self.__current = -1
        self.__temp = -1
        self.__speed = -1
        self.__single_coil_encoder = -1
        self.__multi_turn_encoder = 0
        self.__motor_status = -1
        self.__receive_index = 0
        self.__send_index = 0

    # 电机运行
    def motor_enable(self):
        enable_array = ctypes.c_ubyte * 8
        enable_data = enable_array(0x88, 0, 0, 0, 0, 0, 0, 0)
        self.change_send_data(enable_data)
        send_status = self.can_send_msg(send_id=self.__send_id)
        return send_status

    # 电机停止
    def motor_stop(self):
        stop_array = ctypes.c_ubyte * 8
        stop_data = stop_array(0x81, 0, 0, 0, 0, 0, 0, 0)
        self.change_send_data(stop_data)
        send_status = self.can_send_msg(send_id=self.__send_id)
        return send_status

    # 多圈编码器获取
    def motor_multi_decode(self):
        multi_decode_array = ctypes.c_ubyte * 8
        multi_decode_data = multi_decode_array(0x61, 0, 0, 0, 0, 0, 0, 0)
        self.change_send_data(multi_decode_data)
        send_status = self.can_send_msg(send_id=self.__send_id)
        return send_status

    # 接收解码
    def receiving_msg_processing(self, vci_can_obj):
        print("receive_data_" + str(self.__receive_index) + ": ")
        print(list(vci_can_obj.Data))
        self.__receive_index = self.__receive_index + 1
        if vci_can_obj.ID == self.__send_id:
            if vci_can_obj.Data[0] == 0xA2:
                receive_data = motor_velocity_decode(vci_can_obj.Data)
                self.__single_coil_encoder = receive_data[3]
                self.__temp = receive_data[0]
                self.__current = receive_data[1]
                self.__speed = receive_data[2]
                print("receive_msg from speed control")
            elif vci_can_obj.Data[0] == 0x88:
                self.__motor_status = 1
                print("receive_msg from enable_status control")
            elif vci_can_obj.Data[0] == 0x81:
                self.__motor_status = 0
                print("receive_msg from stop_status control")
            elif vci_can_obj.Data[0] == 0x61:
                self.__multi_turn_encoder = motor_multi_turn_decode(vci_can_obj.Data)
        return vci_can_obj

    # 速度环发送速度
    # 速度单位0.01dps/LSB 度/秒 -》100-》1度/s
    def motor_speed_ring(self, speed):
        speed_array = ctypes.c_ubyte * 8
        speed_data = speed_convert(speed)
        send_data = speed_array(0xA2, 0, 0, 0, speed_data[0], speed_data[1], speed_data[2], speed_data[3])
        self.change_send_data(send_data)
        send_status = self.can_send_msg(send_id=self.__send_id)
        return send_status

    # 获取电机状态
    def get_motor_status(self):
        print(self.__motor_status)
        return self.__motor_status

    def get_motor_single_encode(self):
        print("now_single_encode " + str(self.__single_coil_encoder))
        return self.__single_coil_encoder

    def get_motor_multi_encode(self):
        print("now_single_encode " + str(self.__multi_turn_encoder))
        return self.__multi_turn_encoder

    def get_motor_speed(self):
        return self.__speed


# 速度转换输出为一个list
def speed_convert(speed):
    temp_data = abs(speed)
    if speed < 0:
        # 速度为负输出补码
        temp_data = 4294967295 - temp_data + 1
    send_data = []
    for i in range(0, 4):
        temp_1 = temp_data % 256
        send_data.append(temp_1)
        temp_data = int(temp_data / 256)
    return send_data


# 电机速度环接收解码
def motor_velocity_decode(data):
    msg_feedback = []
    if len(data) == 8:
        # 电机温度
        msg_feedback.append(data[1])
        # 转矩电流
        current_now = data[2] + data[3] * 256
        msg_feedback.append(current_now)
        # 电机速度
        motor_speed_now = data[4] + data[5] * 256
        msg_feedback.append(motor_speed_now)
        # 编码器位置
        motor_encode_now = data[6] + data[7] * 256
        msg_feedback.append(motor_encode_now)
    else:
        print("接收数据长度有误")
    return msg_feedback


# 多圈编码器数值
def motor_multi_turn_decode(data):
    decode_data = -1
    if len(data) == 8:
        decode_data = data[4] + data[5] * 256 + data[6] * 256 * 256 + data[7] * 256 * 256 * 256
    return decode_data
