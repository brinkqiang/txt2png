

# -*- coding: utf-8 -*-
import matplotlib
import matplotlib.pyplot as plt

matplotlib.rcParams['font.family'] = ['SimHei']

# Text data to include in the image
# 读取gdb.txt
with open("gdb.txt", "r", encoding="utf-8") as f:
    text = f.read()

    # Set up the figure and axes
    fig, ax = plt.subplots(figsize=(12, 36))

    # 添加文本到图形（临时）
    text_obj = ax.text(0.5, 0.5, text, fontsize=14, va='center', ha='center', wrap=False)

    # 绘制一次以获取文本边界框
    fig.canvas.draw()

    # 获取文本的边界框
    bbox = text_obj.get_window_extent()

    # 将像素坐标转换为图形坐标
    inv = ax.transData.inverted()
    bbox_data = bbox.transformed(inv)

    # 获取文本边界框的宽度和高度
    width = bbox_data.width
    height = bbox_data.height

    # 关闭初始图形
    plt.close(fig)

    # 创建新的图形，并设置大小以适应文本边界框
    fig, ax = plt.subplots(figsize=(width, height))

    # 隐藏坐标轴
    ax.axis('off')

    # 添加文本到新的图形
    ax.text(0.5, 0.5, text, fontsize=14, wrap=False)

    # 保存图像
    plt.savefig("gdb_cheatsheet.png", bbox_inches='tight', dpi=300)