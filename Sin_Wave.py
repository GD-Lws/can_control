import numpy as np
import matplotlib.pyplot as plt


# 正弦波生成,利用三角函数傅里叶分解
# 幅值、频率、时间长度、采样频率
class Sin_Wave:
    def __init__(self, amp=1.0, period=1.0, samples=8):
        self.__amp = amp
        self.__period = period
        self.__size_w = 2 ** samples
        self.__tri_x, self.__tri_y = self.__triangle_wave()
        self.__fy = np.fft.fft(self.__tri_y) / self.__size_w
        self_wave_index, self.wave_data  = self.fft_combine()

    # 产生__samples点取样的三角波，其周期为1
    def __triangle_wave(self):
        tri_x = np.arange(0, 1, 1 / self.__size_w)
        tri_y = np.where(tri_x < 0.5, tri_x, 0)
        tri_y = np.where(tri_x >= 0.5, 1 - tri_x, tri_y)
        return tri_x*self.__period, tri_y*self.__amp

    def plot_FFT_triangle(self):
        plt.figure(1)
        plt.plot(np.clip(20 * np.log10(np.abs(self.__fy[:20])), -120, 120), "o")
        plt.xlabel("frequency bin")
        plt.ylabel("power(dB)")
        plt.title("FFT result of triangle wave")
        plt.show()

    # 产生方波
    def square_wave(self):
        square_x = np.arange(0, 1, 1.0 / self.__size_w)
        square_y = np.where(square_x < 0.5, 1.0, 0)
        return square_x, square_y

    # 取FFT计算的结果fy中的前n项进行合成，返回合成结果，计算loops个周期的波形
    def fft_combine(self):
        n = 2
        length = len(self.__fy)
        combine_data = np.zeros(length)
        combine_index = np.arange(0, length, 1.0) / length * (2 * np.pi)
        for k, p in enumerate(self.__fy[:n]):
            if k != 0:
                p *= 2  # 除去直流成分之外，其余的系数都*2
            combine_data += np.real(p) * np.cos(k * combine_index)  # 余弦成分的系数为实数部
            combine_data -= np.imag(p) * np.sin(k * combine_index)  # 正弦成分的系数为负的虚数部
        return combine_index, combine_data

    def plot_sin_wave(self):
        plt.figure(2)
        plt.plot(self.__tri_x, self.__tri_y, label="original triangle", linewidth=2)
        plt.plot(self.__tri_x, self.wave_data, label="Sin_Wave")
        plt.legend()
        plt.title("partial Fourier series of triangle wave")
        plt.show()
