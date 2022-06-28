import sys

from PyQt5.QtCore import QObject, QTimer, pyqtSignal
from PyQt5.QtWidgets import QApplication, QMainWindow
from qt_can_imu import Ui_MainWindow
from IMU_HWT901B import HWT901B_CAN


class IMU_Receive:
    def __init__(self, can_id_array):
        self.imu_can = HWT901B_CAN(can_id_array=can_id_array)
        self.can_id_array = can_id_array
        self.can_oc_flag = -1
        app = QApplication(sys.argv)
        MainWindow = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(MainWindow)
        self.ui_button_init()
        self.timer_imu_receive = QTimer()
        QObject.connect(self.timer_imu_receive, pyqtSignal("timeout()"), self.imu_receive_msg)
        MainWindow.show()
        if app.exec_() == 0:
            self.imu_can.can_close()
        sys.exit(app.exec_())

    def ui_button_init(self):
        self.ui.pushButton_start_can.clicked.connect(self.ui_can_open)
        self.ui.pushButton_stop_can.clicked.connect(self.ui_can_close)
        self.ui.pushButton_stop_receive.clicked.connect(self.imu_receive_stop)
        self.ui.pushButton_start_receive.clicked.connect(self.imu_receive_start)

    def ui_can_open(self):
        print("click open can")
        can_init_status = self.imu_can.can_init()
        can_channel_status = self.imu_can.can_channel_open()
        if can_channel_status == 1 and can_init_status == 1:
            self.can_oc_flag = 1
        else:
            self.can_oc_flag = -1

    def ui_can_close(self):
        can_close_status = self.imu_can.can_close()
        if can_close_status == 1:
            self.can_oc_flag = -1
        else:
            self.can_oc_flag = 1

    def imu_receive_start(self):
        self.timer_imu_receive.start(1)

    def imu_receive_stop(self):
        self.timer_imu_receive.stop()

    def imu_receive_msg(self):
        receive_status = self.imu_can.can_receive_msg_2()

    def imu_fresh_edit(self):
        for imu_deriver_id in self.can_id_array:
            imu_angularVelocity_array = self.imu_can.get_imu_angle_v(imu_deriver_id)
            imu_acceleration_array = self.imu_can.get_imu_ac(imu_deriver_id)
            imu_euler_array = self.imu_can.get_imu_euler(imu_deriver_id)


if __name__ == "__main__":
    imu_id_array = [0x50, 0x51, 0x52, 0x53, 0x54]
    imu_receive = IMU_Receive(imu_id_array)
