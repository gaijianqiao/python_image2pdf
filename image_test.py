from PIL import Image
with Image.open('f:\\github\\python_image2pdf\\jpg\\2tree.jpg') as img:

    # print(img.size)
    # box = (100, 100, 200, 200)  # 设置要拷贝的区域
    #
    # # 将im表示的图片对象拷贝到region中，大小为(400*400)像素。这个region可以用来后续的操作(region其实就是一个Image对象)，box变量是一个四元组(左，上，右，下)。
    # region = img.crop(box)
    #
    # region = region.transpose(Image.ROTATE_90)  # 从字面上就可以看出，先把region中的Image反转180度，然后再放回到region中。
    # img.paste(region, box)  # 粘贴box大小的region到原先的图片对象中。

    # r, g, b = img.split()  # 分割成三个通道
    # r.show()
    # g.show()
    # b.show()
    # img = Image.merge("RGB", (g, b, r))  # 将b,r两个通道进行翻转。
    # img.resize((28, 128))
    # img.resize((1,1),Image.BILINEAR)
    img.save("f:\\github\\python_image2pdf\\jpg\\2tree3.jpg",quality=15)