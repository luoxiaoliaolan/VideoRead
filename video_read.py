# -*- coding:utf-8 -*-
#@Time : ${DATE} ${TIME}
#@Author: lyb
#@File : ${NAME}.py
#@Description : 用于批量的视频数据的加载和解帧

import os
import time
import cv2 as cv
import sys
import argparse
from multiprocessing import Pool


# 多线程读取视频数据并解帧为图片
def read_vedio_frame(vedio_dir, frame_dir, name):

    video_flag = os.path.exists(vedio_dir)
    if(video_flag == False):
        print("please input corrrect path!")

    try:
        video_path = os.path.join(vedio_dir, name)
        cap = cv.VideoCapture(video_path)
    except FileNotFoundError:
        print("reading video path error")
    #总帧数
    frames_num = cap.get(7)

    print("input video frames is： {}".format(frames_num))
    #判断输入的保存视频帧的文件夹是否存在，若不存在则创建一个
    if not os.path.exists(frame_dir):
        os.mkdir(frame_dir)
        
    #把视频逐帧解帧
    if not os.path.exists(os.path.join(frame_dir, name.split('.')[0])):
        os.mkdir(os.path.join(frame_dir, name.split('.')[0]))

    count = 0
    while(1):
        #cap的read方法读取视频帧，返回rval表示帧读取成功与否，frame表示读取的帧
        rval, frame = cap.read()
        if rval is False:
            break
        image_dir = os.path.join(frame_dir, name.split('.')[0], str(count) + ".jpg")
        print("解析的视频帧的保存路径为：{}".format(image_dir))
        count = count + 1
        cv.imwrite(image_dir, frame)
    cap.release()

if __name__ == '__main__':
    #加入路径参数输入
    parser = argparse.ArgumentParser()
    parser.add_argument("--input_video", default="D:/code/video", type=str)
    parser.add_argument("--output_frames", default="D:/code/video/frames", type=str)

    args = parser.parse_args()

    #获取视频列表,使用了函数式编程以及列表表达式
    videos_list = list(filter(lambda x: x.endswith("mp4"), os.listdir(args.input_video)))

    #多线程处理
    num_workers = 4
    pool = Pool(processes=num_workers)
    start_time = time.time()
    for video_name in videos_list:
        if os.path.splitext(video_name)[1] == ".mp4":
            print(video_name)
            pool.apply(read_vedio_frame, args=(args.input_video, args.output_frames, video_name))
    pool.close()
    pool.join()
    print("解析视频帧的时间：{}s".format(time.time() - start_time))
    print("done")
