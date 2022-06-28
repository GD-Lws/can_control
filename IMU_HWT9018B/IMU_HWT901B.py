import datetime
import math
import struct

import time

from Can_Derive import Can_Derive


# 16 to ieee float
def hex_to_short(raw_data):
    return list(struct.unpack("hhhh", bytearray(raw_data)))


def receive_data_pro(data_L, data_H):
    PN_flag = -1
    if data_H > 127:
        PN_flag = 1
    ans = data_L + data_H * 256
    if PN_flag == 1:
        return 65535 - ans + 1
    else:
        return ans


class HWT901B_CAN(Can_Derive):
    def __init__(self, can_id_array, win_linux=1):
        Can_Derive.__init__(self, win_linux=win_linux)
        self.imu_num = len(can_id_array)
        self.__HWT901B_array = []
        self.__can_id_array = can_id_array
        for i in range(0, self.imu_num):
            self.__HWT901B_array.append(HWT901B(can_id_array[i]))

    # receive_date decode
    # 0x51 AC 0x52 EC 0x53 AG
    def receiving_msg_processing(self, vci_can_obj):
        print("can_id: ", vci_can_obj.ID)
        print("data_array: ")
        print(list(vci_can_obj.Data))
        if self.__can_id_array.count(vci_can_obj.ID) != 0:
            id_index = self.__can_id_array.index(vci_can_obj.ID)
            if vci_can_obj.Data[1] == 0x51:
                self.__HWT901B_array[id_index].imu_set_ac(data=list(vci_can_obj.Data))
            elif vci_can_obj.Data[1] == 0x52:
                self.__HWT901B_array[id_index].imu_set_angular_v(data=list(vci_can_obj.Data))
            elif vci_can_obj.Data[1] == 0x53:
                self.__HWT901B_array[id_index].imu_set_euler(data=list(vci_can_obj.Data))
        else:
            self.__can_id_array.append(vci_can_obj.ID)
            self.__HWT901B_array.append(HWT901B(vci_can_obj.ID))
            print("new_can_id_append :", vci_can_obj.ID)

    def get_imu_euler(self, can_id):
        if self.__can_id_array.count(can_id) != 0:
            id_index = self.__can_id_array.index(can_id)
            return self.__HWT901B_array[id_index].imu_get_euler()
        else:
            print("This ", can_id, " is NULL")
            return None

    def get_imu_ac(self, can_id):
        if self.__can_id_array.count(can_id) != 0:
            id_index = self.__can_id_array.index(can_id)
            return self.__HWT901B_array[id_index].imu_get_ac()
        else:
            print("This ", can_id, " is NULL")
            return None

    def get_imu_angle_v(self, can_id):
        if self.__can_id_array.count(can_id) != 0:
            id_index = self.__can_id_array.index(can_id)
            return self.__HWT901B_array[id_index].imu_get_angle_v()
        else:
            print("This ", can_id, " is NULL")
            return None


class HWT901B:
    def __init__(self, can_id):
        self.__can_id = can_id
        self.__euler_roll_pitch_yaw = [0, 0, 0]
        self.__angular_v = [0, 0, 0]
        self.__ac = [0, 0, 0]
        print("imu_create ,can_id: ", self.__can_id)

    def imu_set_ac(self, data):
        self.__ac = [hex_to_short(data)[i] / 32768.0 * 16 * 9.8 for i in range(1, 4)]
        print(str(datetime.datetime.now()), "  ", self.__can_id, " acceleration: ")
        print(self.__ac)

    def imu_set_euler(self, data):
        self.__euler_roll_pitch_yaw = [hex_to_short(data)[i] / 32768.0 * 180 for i in range(1, 4)]
        print(str(datetime.datetime.now()), "  ", self.__can_id, " euler: ")
        print(self.__euler_roll_pitch_yaw)

    def imu_set_angular_v(self, data):
        self.__angular_v = [hex_to_short(data)[i] / 32768.0 * 2000 * math.pi / 180 for i in range(1, 4)]
        print(str(datetime.datetime.now()), "  ", self.__can_id, " angularVelocity: ")
        print(self.__angular_v)

    def imu_get_euler(self):
        return self.__euler_roll_pitch_yaw

    def imu_get_angle_v(self):
        return self.__angular_v

    def imu_get_ac(self):
        return self.__ac


if __name__ == "__main__":
    imu_id_array = [0x50, 0x51, 0x52, 0x53]
    imu_receive = HWT901B_CAN(imu_id_array)
    imu_receive.can_init()
    imu_receive.can_channel_open()
    for i in range(0, 100):
        imu_receive.can_receive_msg_2()
    imu_receive.can_close()
