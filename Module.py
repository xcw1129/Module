# PYTHON基础库


# 数值计算库
import matplotlib
import numpy as np
from numpy import random  # 随机数库

# 绘图库
from matplotlib import pyplot as plt
from matplotlib import font_manager  # 字体管理库

# 全局绘图设置
font_path = r"F:\OneDrive\文档\Fonts\times+simsun.ttf"
font_manager.fontManager.addfont(font_path)  # 添加字体
prop = font_manager.FontProperties(fname=font_path)  # 设置字体属性
config = {
    "font.family": 'sans-serif',  # 设置全局字体
    "font.sans-serif": prop.get_name(),
    "font.size": 20,  # 设置全局字体大小
    # 设置各元素字体大小统一
    "axes.titlesize": 20,  # 标题字体大小
    "axes.labelsize": 20,  # 轴标签字体大小
    "xtick.labelsize": 20,  # x轴刻度标签字体大小
    "ytick.labelsize": 20,  # y轴刻度标签字体大小
    "legend.fontsize": 20,  # 图例字体大小
    # 设置正常显示负号
    "figure.figsize": (12,5),  # 默认图形大小，12cm x 5cm
    "figure.dpi": 100,  # 显示分辨率
    "savefig.dpi": 600,  # 保存分辨率
    "axes.prop_cycle": matplotlib.cycler(color=[
        "#1f77b4",  # 蓝
        "#ff7f0e",  # 橙
        "#2ca02c",  # 绿
        "#d62728",  # 红
        "#a77ece",  # 紫
        "#8c564b",  # 棕
        "#520e8e",  # 粉
        "#7f7f7f",  # 灰
        "#bcbd22",  # 橄榄
        "#17becf"   # 青
    ]),  # 设置颜色循环
    "axes.grid": True,  # 显示网格
    "axes.grid.axis": "y",  # 只显示y轴网格
    "grid.linestyle": (0, (8, 6)),  # 网格线为虚线
    "xtick.direction": "in",  # x轴刻度线朝内
    "ytick.direction": "in",  # y轴刻度线朝内
    "mathtext.fontset": "custom",  # 公式字体设置
    "mathtext.rm": "Times New Roman",  # 数学公式字体 - 正常
    "mathtext.it": "Times New Roman:italic",  # 数学公式字体 - 斜体
    "mathtext.bf": "Times New Roman:bold"  # 数学公式字体 - 粗体
}
# 更新rcParams
plt.rcParams.update(config)

# 表格处理库
import pandas as pd

# 科学计算库
import scipy
from scipy import stats  # 统计库
from scipy import signal  # 信号处理库
from scipy import fft  # 傅里叶变换库

# 全局常量定义
PI = np.pi
FLOAT_EPS = np.finfo(float).eps  # 浮点数精度
FIG_SIZE = (12, 5)  # 默认图形大小

if __name__ == "__main__":
    # 测试代码
    x = np.linspace(0, 10, 100)
    y1 = np.sin(x) + np.random.normal(0, 0.1, x.shape)
    y2 = np.cos(x) + np.random.normal(0, 0.1, x.shape)
    y3 = np.tan(x) + np.random.normal(0, 0.1, x.shape)
    
    plt.figure()
    plt.plot(x, y1, label='$f_1$')
    plt.plot(x, y2, label='$f_2$')
    plt.plot(x, y3, label='$f_3$')
    plt.legend()
    plt.title("正弦波$f = sin(t)$")
    plt.xlabel("时间t/s")
    plt.ylabel("幅值")
    
    plt.show()