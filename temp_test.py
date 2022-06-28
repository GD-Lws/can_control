def myactuator_test():
    myactuator = Motor_Myactuator()
    if myactuator.motor_enable() == 1:
        myactuator.can_receive_msg()
    time.sleep(5)
    if myactuator.get_motor_status() == 1:
        send_flag = myactuator.motor_speed_ring(65535)
        if send_flag == 1:
            receive_flag = myactuator.can_receive_msg()
    myactuator.can_close()


def can_derive_test():
    can_derive = Can_Derive()
    can_derive.can_init()
    can_derive.can_channel_open()
    send_array = ctypes.c_ubyte * 8
    send_data = send_array(0x88, 0, 0, 0, 0, 0, 0, 0)
    can_derive.change_send_data(send_data)
    derive_send_flag = can_derive.can_send_msg(send_id=0x141)
    while derive_send_flag == 1:
        derive_receive_flag = can_derive.can_receive_msg()
        if derive_receive_flag == 1:
            derive_send_flag = -1


def sin_wave_test():
    sin_wave = Sin_Wave()
    sin_wave.plot_FFT_triangle()
    sin_wave.plot_sin_wave()
    index = np.arange(0, 256)
    a = np.arange(0, 1, 1 / 256)
    sin_wave_2 = np.sin(2 * np.pi * a)
    print(sin_wave.wave_data)
    print(sin_wave_2)
    plt.Figure()
    plt.plot(index, sin_wave.wave_data, label="sin_wave")
    plt.plot(index, sin_wave_2, label="sin_wave_2")
    plt.legend()
    plt.show()
