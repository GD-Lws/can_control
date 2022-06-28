import datetime
import threading
from concurrent.futures import ThreadPoolExecutor

from PyQt5.QtWidgets import QApplication, QMainWindow
import qt_layout
from MyActuator.Motor_Myactuator import Motor_Myactuator
import time
import sys


# 需要注意线程间的调度
# CAN收发不能同时进行调度（互斥）
# 注意线程间不能同时对同一个内存进行写读
# 界面线程、CAN线程、主线程
# 使用线程池

# 毫秒延时,精度为0.001s
def time_ms_delay(time_data):
    delay_mark = time.time()
    while True:
        offset = time.time() - delay_mark
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


# def qt_button_init():
#     # ui.button_enable.clicked.connect(motor_speed_trans)
#     # ui.button_disable.clicked.connect(motor.motor_stop)
#     # ui.button_speed.clicked.connect(motor_speed_trans)
#     # ui.button_pid.clicked.connect(motor_pid_set)


def motor_speed_enable():
    motor.motor_enable()


def motor_speed_set():
    ui_speed = ui.edit_speed_input.text()


def motor_speed_trans():
    # while True:
    print(datetime.time)
    speed_send_status = -1
    if is_number(ui_speed):
        speed_send_status = motor.motor_speed_ring(int(ui_speed))
    else:
        speed_send_status = motor.motor_speed_ring(0)
    if speed_send_status == 1:
        speed_receive_status = motor.can_receive_msg()
        if speed_receive_status == 1:
            encode_send_status = motor.motor_multi_decode()
            if encode_send_status == 1:
                encode_receive_status = motor.can_receive_msg()
                if encode_receive_status == 1:
                    ui.edit_encode.setText(str(motor.get_motor_multi_encode()))
        # time_ms_delay(3)
    # return speed_send_status


def motor_pid_set():
    kp_num = int(ui.edit_kp.text())
    ki_num = int(ui.edit_ki.text())
    kd_num = int(ui.edit_kd.text())
    print("Set Kp: " + str(kp_num) + " Ki: " + str(ki_num) + " Kd: " + str(kd_num))


if __name__ == "__main__":
    global ui, motor
    global ui_speed
    global kp_num, ki_num, kd_num
    motor = Motor_Myactuator()
    thread_pool = ThreadPoolExecutor(2)
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = qt_layout.Ui_MainWindow()
    ui.setupUi(MainWindow)
    # qt_button_init()
    # ui_thread = thread_pool.submit(ui)
    # decode_thread = thread_pool.submit(motor_speed_trans)
    MainWindow.show()
    t = threading.Timer(0.2, motor_speed_trans).start()
    sys.exit(app.exec_())
