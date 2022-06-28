import datetime
import sys
import threading
from asyncio import as_completed
from concurrent.futures import ThreadPoolExecutor

from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication, QMainWindow


from Motor_Myactuator import Motor_Myactuator
from qt_can_motor import Ui_MainWindow


# 毫秒延时,精度为0.001s
def time_ms_delay(time_data):
    delay_mark = datetime.time.time()
    while True:
        offset = datetime.time.time() - delay_mark
        if offset > 0.0001 * time_data:
            break


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass

    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass

    return False


class Myactuator_Control:
    def __init__(self):
        self.multi_code = -1
        self.single_code = -1
        self.can_send_flag = -2
        self.ui_pid = [0, 0, 0]
        self.ui_speed = 0
        self.motor = Motor_Myactuator()
        self.can_oc_flag = -1
        app = QApplication(sys.argv)
        MainWindow = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(MainWindow)
        self.ui_button_init()
        self.timer_multi_encode = QTimer()
        self.timer_continue_speed = QTimer()
        QObject.connect(self.timer_multi_encode, SIGNAL("timeout()"), self.ui_multi_code_get)
        QObject.connect(self.timer_continue_speed, SIGNAL("timeout()"), self.ui_motor_speed_single)
        MainWindow.show()
        if app.exec_() == 0:
            self.motor.can_close()
        sys.exit(app.exec_())

    def ui_button_init(self):
        self.ui.button_enable.clicked.connect(self.ui_motor_enable)
        self.ui.button_disable.clicked.connect(self.ui_motor_disable)
        self.ui.button_speed_single.clicked.connect(self.ui_motor_speed_single)
        self.ui.button_pid_set.clicked.connect(self.ui_motor_pid_set)
        self.ui.button_derive_open.clicked.connect(self.ui_can_open)
        self.ui.button_derive_close.clicked.connect(self.ui_can_close)
        self.ui.button_mc_open.clicked.connect(self.ui_multi_code_start)
        self.ui.button_mc_close.clicked.connect(self.ui_multi_code_stop)
        self.ui.button_speed_continue_start.clicked.connect(self.ui_speed_continue_start)
        self.ui.button_speed_continue_close.clicked.connect(self.ui_speed_continue_stop)

    def ui_multi_code_get(self):
        motor_multi_code_status = self.motor.motor_multi_decode()
        if motor_multi_code_status == 1:
            motor_multi_code_status = self.motor.can_receive_msg()
            if motor_multi_code_status == 1:
                self.ui.edit_encode_multi.setText(str(self.motor.get_motor_multi_encode()))

    def ui_multi_code_start(self):
        self.timer_multi_encode.start(100)

    def ui_multi_code_stop(self):
        self.timer_multi_encode.stop()

    def ui_speed_continue_start(self):
        self.timer_continue_speed.start(100)

    def ui_speed_continue_stop(self):
        self.timer_continue_speed.stop()

    def ui_can_open(self):
        can_init_status = self.motor.can_init()
        can_channel_status = self.motor.can_channel_open()
        if can_channel_status == 1 and can_init_status == 1:
            self.can_oc_flag = 1
        else:
            self.can_oc_flag = -1

    def ui_can_close(self):
        can_close_status = self.motor.can_close()
        if can_close_status == 1:
            self.can_oc_flag = -1
        else:
            self.can_oc_flag = 1

    def ui_motor_enable(self):
        motor_enable_status = self.motor.motor_enable()
        if motor_enable_status == 1:
            self.motor.can_receive_msg()

    def ui_motor_disable(self):
        motor_disable_status = self.motor.motor_stop()
        if motor_disable_status == 1:
            self.motor.can_receive_msg()

    def ui_motor_speed_single(self):
        if is_number(self.ui.edit_speed_input.text()):
            self.ui_speed = int(self.ui.edit_speed_input.text())
            motor_speed_send_status = self.motor.motor_speed_ring(self.ui_speed)
            if motor_speed_send_status == 1:
                motor_speed_receive_status = self.motor.can_receive_msg()
                if motor_speed_receive_status == 1:
                    self.ui.edit_encode_single.setText(str(self.motor.get_motor_single_encode()))

    def ui_motor_pid_set(self):
        if is_number(self.ui.edit_kp.text()):
            self.ui_pid[0] = float(self.ui.edit_kp.text())
        if is_number(self.ui.edit_ki.text()):
            self.ui_pid[1] = float(self.ui.edit_ki.text())
        if is_number(self.ui.edit_kd.text()):
            self.ui_pid[2] = float(self.ui.edit_kd.text())


if __name__ == "__main__":
    motor_control = Myactuator_Control()

