import datetime
import math
import time

from Can_Derive import Can_Derive


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
    def __init__(self, win_linux=0, imu_num=10, ros_publisher = rospy.Publisher('ros_imu', Imu, queue_size=10)):
        Can_Derive.__init__(self, win_linux=win_linux)
        self.__imu_num = imu_num
        self.ros_publisher = ros_publisher
        self.__can_id_list = []
        self.__imu_date_list = []
        for index in range(0, imu_num):
            self.__can_id_list[index] = 0
            for index_0 in range(0, 9):
                self.__imu_date_list.append(0)

    # receive_date decode
    # 0x51 AC 0x52 EC 0x53 AG
    def receiving_msg_processing(self, vci_can_obj):
        print("can_id: ", vci_can_obj.ID)
        print("data_array: ")
        print(list(vci_can_obj.Data))
        temp_can_id = vci_can_obj.ID - 0x50
        if temp_can_id + 1 > self.__imu_num:
            self.__imu_num = temp_can_id + 1
            while len(self.__can_id_list) < self.__imu_num:
                self.__can_id_list.append(0)
            while len(self.__imu_date_list) < self.__imu_num * 9:
                self.__imu_date_list.append(0)
            print("Add new can_id")
            print("Now can_id_list len", len(self.__can_id_list))

        if self.__can_id_list[temp_can_id] == 0:
            self.__can_id_list[temp_can_id] = 1
        elif self.__can_id_list[temp_can_id] == 3:
            imu_msg = IMU()
            self.ros_publisher

        if vci_can_obj.Data[1] == 0x51:
            # AC
            self.__imu_date_list[temp_can_id*9 + 0] =
            self.__imu_date_list[temp_can_id*9 + 1] =
            self.__imu_date_list[temp_can_id*9 + 2] =
        elif vci_can_obj.Data[1] == 0x52:
            # EC
            self.__imu_date_list[temp_can_id*9 + 3] =
            self.__imu_date_list[temp_can_id * 9 + 4] =
            self.__imu_date_list[temp_can_id * 9 + 5] =
        elif vci_can_obj.Data[1] == 0x53:
            # AG
            self.__imu_date_list[temp_can_id*9 + 6] =
            self.__imu_date_list[temp_can_id * 9 + 7] =
            self.__imu_date_list[temp_can_id * 9 + 8] =


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
        self.__angular_v = [0, 0, 0, 0]
        self.__ac = [0, 0, 0, 0]
        print("imu_create ,can_id: ", self.__can_id)

    def imu_set_ac(self, data):
        AxL = data[2]
        AxH = data[3]
        Ax = receive_data_pro(AxL, AxH)
        AyL = data[4]
        AyH = data[5]
        Ay = receive_data_pro(AyL, AyH)
        AzL = data[6]
        AzH = data[7]
        Az = receive_data_pro(AzL, AzH)
        self.__ac[0] = float(Ax / 32768.0 * 16 * 9.8)
        self.__ac[1] = float(Ay / 32768.0 * 16 * 9.8)
        self.__ac[2] = float(Az / 32768.0 * 16 * 9.8)
        print(str(datetime.datetime.now()), "  ", self.__can_id, " acceleration: ")
        print(self.__ac)

    def imu_set_euler(self, data):
        RollL = data[2]
        RollH = data[3]
        Roll = receive_data_pro(RollL, RollH)
        PitchL = data[4]
        PitchH = data[5]
        Pitch = receive_data_pro(PitchL, PitchH)
        YawL = data[6]
        YawH = data[7]
        Yaw = receive_data_pro(YawL, YawH)
        self.__euler_roll_pitch_yaw[0] = float(Roll / 32768 * 180)
        self.__euler_roll_pitch_yaw[1] = float(Pitch / 32768 * 180)
        self.__euler_roll_pitch_yaw[2] = float(Yaw / 32768 * 180)
        print(str(datetime.datetime.now()), "  ", self.__can_id, " euler: ")
        print(self.__euler_roll_pitch_yaw)

    def imu_set_angular_v(self, data):
        WxL = data[2]
        WxH = data[3]
        Wx = receive_data_pro(WxL, WxH)
        WyL = data[4]
        WyH = data[5]
        Wy = receive_data_pro(WyL, WyH)
        WzL = data[6]
        WzH = data[7]
        Wz = receive_data_pro(WzL, WzH)
        self.__angular_v[0] = float(Wx / 32768 * 2000 * math.pi / 180)
        self.__angular_v[1] = float(Wy / 32768 * 2000 * math.pi / 180)
        self.__angular_v[2] = float(Wz / 32768 * 2000 * math.pi / 180)
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
