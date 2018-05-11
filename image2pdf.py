import os
import sys
from reportlab.lib.pagesizes import A4, landscape
from reportlab.pdfgen import canvas
from PIL import Image
from reportlab.lib.units import inch
'''
遍历当前目录下所有的jpg文件,并按照文件夹名称合并成pdf文档
python 3.4.4
图片文件用数字按顺序命名


'''


def conpdf():
    # 获取横向A4大小
    (w, h) = (1080,19026)#landscape(A4)
    i = 0;
    # 遍历当前目录
    for root, dirs, files in os.walk(os.getcwd()+"\\jpg"):
        #计算处每一张图片的尺寸，通过改尺寸，定义pdf画布和贴入图片的大小
        # print(os.path.basename(root)+".pdf")
        # 用于存放jpg文件
        jpg_list = []
        # 从文件列表中取出jpg文件放入到list中
        for p in files:
            # 将jpg文件名存入列表
            if p[-4:] == '.jpg':
                # jpg_list.append(root + "\\" +p)
                jpg_list.append(p)
        # 对文件名称排序
        # jpg_list.sort(key=lambda x: int(x[:-4]))
        # print(jpg_list)
        c = canvas.Canvas(os.path.basename(root) + ".pdf")
        for f in jpg_list:
            with Image.open(os.getcwd() + "\\jpg\\" + f) as tempImag:
                tempImag.save(os.getcwd() + "\\jpg\\" + f, quality=15)
            # 按顺序把图片画到画布上
            with Image.open(os.getcwd() + "\\jpg\\" + f) as img:
                (w, h) = img.size

            c.bookmarkPage(str(f))
            # 根据根目录名创建一个pdf
            c.setPageSize((w,h))
            c.drawImage(root + "\\" + f, 0, 0, w, h)


            # 结束当前页并新建页
            c.showPage()
        c.save()



    print ("ok.")

if __name__ =='__main__':
    conpdf()