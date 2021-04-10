# VideoRead
video read and  get frames

本例程用于读取视频数据，并抽取视频数据的帧保存成图像

所用语言：Python
视觉库：OpenCV

使用方式： python video_read.py []
[]表示执行需要的参数 ：其中 --input_video 表示输入视频数据的文件夹路径（含有多个视频），"--output_frames" 表示输出抽取帧的文件夹路径，输入完毕即可执行视频抽取帧的任务，采用了4线程进行处理，提高了运行的效率
