#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:livingbody
@file:generate_dongman.py
@time:2021/12/11
"""
import os

from qgui import CreateQGUI
from qgui.banner_tools import GitHub
from qgui.notebook_tools import ChooseFileTextButton, ChooseDirTextButton, RunButton
from qgui import MessageBox

import paddlehub as hub
import cv2


def print_image(image):
    from PIL import Image, ImageTk
    if isinstance(image, str):
        image = Image.open(image)
        print(image)
        image.show()


if __name__ == "__main__":
    animegan_v2 = hub.Module(name="animegan_v2_hayao_99")


    # 预测主程序
    def infer(args):
        img_path = args["文件输入框"].get()
        out_path = args["保存位置"].get()
        # 简单做个判断，保证输入是正确的
        if not os.path.exists(img_path):
            MessageBox.info("请选择要风格化的图片")
            # 不选择就不做预测了
            return 1
        if not os.path.exists(out_path):
            MessageBox.info("请选择图片保存目录")
            return 2

        # 执行分割
        print("开始分割")
        animegan_v2.style_transfer(images=[cv2.imread(img_path)],
                                   visualization=True,
                                   output_dir=out_path)

        # 打开结果文件夹 不支持MAC系统
        os.startfile(out_path)
        # print_image()
        print("处理完毕")


    # 创建主界面
    main_gui = CreateQGUI(title="基于PaddleHub的宫崎骏动漫动漫风格化")

    # 在界面最上方添加一个按钮，链接到GitHub主页
    main_gui.add_banner_tool(GitHub("https://github.com/QPT-Family/QGUI"))
    # 在主界面部分添加一个文件选择工具
    main_gui.add_notebook_tool(ChooseFileTextButton(name="文件输入框"))
    # 再加个文件夹选择工具
    main_gui.add_notebook_tool(ChooseDirTextButton(name="保存位置"))
    # 添加一个运行按钮
    main_gui.add_notebook_tool(RunButton(infer))
    main_gui.set_navigation_info(title="宫崎骏动漫动漫画生产",
                                 info="基于PaddleHub的宫崎骏动漫动漫风格化，在右侧选择需要扣图的图片和保存位置，点击开始运行即可获取结果。")
    # 简单加个简介
    main_gui.set_navigation_about(author="Livingbody",
                                  version="0.0.1",
                                  github_url="https://github.com/QPT-Family/QGUI")
    # 跑起来~
    main_gui.run()
