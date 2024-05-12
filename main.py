import os
from detect import main
from detect import parse_opt
from stitching import Stitcher
import cv2

root = "tempImg/"
output_folder = "output/"
imglist = []

for filename in os.listdir(root):
    imglist.append(cv2.imread(root + filename))

stitcher = Stitcher(detector="sift", confidence_threshold=0.2)
panorama = stitcher.stitch(imglist)

# 创建一个可调整大小的窗口
cv2.namedWindow('Resizable Window', cv2.WINDOW_NORMAL)

# 显示图像
cv2.imshow('Resizable Window', panorama)

# 如果需要验证保存成功，可以打印结果
if cv2.imwrite(output_folder + "output_image.jpg", panorama):
    print("Image successfully saved.")
else:
    print("Failed to save image.")
opt = parse_opt(source=output_folder + "output_image.jpg", imgsz=(panorama.shape[:2]))
# opt = parse_opt(source="output_image.jpg", imgsz=(panorama.shape[:2]))
if __name__ == '__main__':
    main(opt)


