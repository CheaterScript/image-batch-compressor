#!/usr/bin/python3

import cv2
import os
import numpy as np
import traceback
import time
from PIL import Image

# 输入路径
INPUT_PATH = 'D:/PYProject/concat/图片'
# 输出路径
OUTPUT_PATH = 'D:/PYProject/concat/替换'
# 输出宽度
WIDTH = 512
# 输出高度
HEIGHT = 512
# 宽度阈值
MAX_WIDTH = 512
# 高度阈值
MAX_HEIGHT = 512
# JPGE输出质量 0-100 越大质量越好
JPEG_QUALITY = 10
# PNG压缩程度 0-10 越小质量越好
PNG_COMPRESSION = 9

# 支持的格式, 不在其中的会跳过处理
FILE_TYPES = ('.jpg', '.jpge', '.png', '.tga')


def cv_imread(file_path):
    img_mat = cv2.imdecode(np.fromfile(
        file_path, dtype=np.uint8), cv2.IMREAD_UNCHANGED)
    return img_mat


def findAllFile(base, handleDir=True):
    for root, dirs, fs in os.walk(base):
        if handleDir:
            for d in dirs:
                dir = os.path.join(root, d)
                dir = dir.replace(INPUT_PATH, '')
                mkdir(OUTPUT_PATH + '/' + dir)
        for f in fs:
            fullname = os.path.join(root, f)
            yield fullname
        # for name


def mkdir(path):
    if not os.path.exists(path):
        os.makedirs(path)


def saveFile(fileName, img):
    _, ExtensionName = os.path.splitext(fileName)
    ExtensionName = ExtensionName.lower()
    file = fileName.replace(INPUT_PATH, '')
    if ExtensionName == '.jpg' or ExtensionName == '.jpeg':
        cv2.imencode(ExtensionName, img, [int(cv2.IMWRITE_JPEG_QUALITY), JPEG_QUALITY])[
            1].tofile(OUTPUT_PATH + '/' + file)
    if ExtensionName == '.PNG' or ExtensionName == '.png':
        cv2.imencode(ExtensionName, img, [int(cv2.IMWRITE_PNG_COMPRESSION), PNG_COMPRESSION])[
            1].tofile(OUTPUT_PATH + '/' + file)
    else:
        cv2.imencode(ExtensionName, img)[
            1].tofile(OUTPUT_PATH + '/' + file)


def handleTGA(fileName):
    img = Image.open(fileName)
    width, height = img.size
    if width >= height and width > MAX_WIDTH:
        img = img.resize((WIDTH, int(height * WIDTH / width)), Image.BICUBIC)
    elif width < height and height > MAX_HEIGHT:
        img = img.resize((int(width * HEIGHT / height), HEIGHT), Image.BICUBIC)
    file = fileName.replace(INPUT_PATH, '')
    img.save(OUTPUT_PATH + '/' + file, 'TGA')


def checkAllFile(q, base, total):
    count = 1
    for i in findAllFile(base, False):
        q.put('正在检验第' + str(count) + '/' + str(total) + '张')
        _, ExtensionName = os.path.splitext(i)
        ExtensionName = ExtensionName.lower()
        if ExtensionName not in FILE_TYPES:
            raise Exception("文件验证失败：" + i)
        if ExtensionName == '.tga':
            img = Image.open(i)
            if img is None:
                raise Exception("文件验证失败：" + i)
        else:
            img = cv_imread(i)
            if img is None:
                raise Exception("文件验证失败：" + i)
        count += 1


def handle(q, inputPath, outputPath, imageWidth, imageHeight, maxWidth, maxHeight, jpgeQuality, pngCompression):
    global INPUT_PATH, OUTPUT_PATH, WIDTH, HEIGHT, MAX_WIDTH, MAX_HEIGHT, JPEG_QUALITY, PNG_COMPRESSION
    # 输入路径
    INPUT_PATH = inputPath
    # 输出路径
    OUTPUT_PATH = outputPath
    # 输出宽度
    WIDTH = imageWidth
    # 输出高度
    HEIGHT = imageHeight
    # 宽度阈值
    MAX_WIDTH = maxWidth
    # 高度阈值
    MAX_HEIGHT = maxHeight
    # JPGE输出质量 0-100 越大质量越好
    JPEG_QUALITY = jpgeQuality
    # PNG压缩程度 0-10 越小质量越好
    PNG_COMPRESSION = pngCompression

    base = INPUT_PATH
    count = 1

    # 检查导出目录是否存在
    if not os.path.exists(OUTPUT_PATH):
        os.makedirs(OUTPUT_PATH)

    for i in findAllFile(base):
        _, ExtensionName = os.path.splitext(i)
        ExtensionName = ExtensionName.lower()
        if ExtensionName not in FILE_TYPES:
            continue
        q.put('正在处理第' + str(count) + '张')
        # continue
        try:
            if ExtensionName == '.tga':
                handleTGA(i)
                count += 1
                continue
            img = cv_imread(i)
            height, width = img.shape[0], img.shape[1]
            if width >= height and width > MAX_WIDTH:
                img = cv2.resize(img, (WIDTH, int(height * WIDTH / width)),
                                 interpolation=cv2.INTER_CUBIC)
            elif width < height and height > MAX_HEIGHT:
                img = cv2.resize(img, (int(width * HEIGHT / height), HEIGHT),
                                 interpolation=cv2.INTER_CUBIC)
            saveFile(i, img)

        except Exception as e:
            q.put(e)
            q.put('错误文件：' + i)
            traceback.print_exc()
            os._exit(0)
        count += 1
    q.put('处理完毕，开始检验')
    checkAllFile(q, OUTPUT_PATH, count - 1)
    q.put('所有图片已经处理完成！')
    time.sleep(1)
    os._exit(0)
