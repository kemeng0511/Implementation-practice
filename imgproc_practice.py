import numpy as np
import cv2 as cv

# 1.Load a single image and display it
original = cv.imdecode(np.fromfile("E:/PyCharm Community Edition 2020.1.1/IP/img/0501.jpg", dtype=np.uint8), -1)
cv.imshow("building", original)
cv.waitKey(0)

# 6.Load color image and convert it to grayscale
gray_im = cv.cvtColor(original, cv.COLOR_BGR2GRAY)
cv.imshow("gray", gray_im)
cv.waitKey(0)
cv.destroyAllWindows()

# # 2.Load a video file and display it
# # 3.Load a video file and save sequence numbered image files
# toy = cv.VideoCapture("E:/PyCharm Community Edition 2020.1.1/IP/img/Toy.mp4")
# while True:
#     ret, frame = toy.read()
#     i = 1
#     if frame is not None:
#         cv.imshow("Video", frame)
#         # cv.imwrite('E:/PyCharm Community Edition 2020.1.1/IP/img/'+str(i)+'.jpg', frame)
#         i += 1
#         if cv.waitKey(3) & 0xFF == ord('q'):
#             break
# toy.release()
# cv.destroyAllWindows()

# # 4.Load color image and swap RGB channels
# (B, G, R) = cv.split(original)
# cv.imshow("swap R and B", cv.merge([R, G, B]))
# cv.waitKey(0)
# cv.destroyAllWindows()

# # 5.Load color image and rotate it 45 degrees
# rows, cols, _ = original.shape
# matrix = cv.getRotationMatrix2D((cols/2, rows/2), -45, 1)
# img_45rotation = cv.warpAffine(original, matrix, (cols, rows))
# cv.imshow('Rotation:45', img_45rotation)
# cv.waitKey(0)
# cv.destroyAllWindows()

# # 7.Detect edges in a grayscale image (Sobel, Laplacian, Canny)
# # Sobel
# edge_sobel_x = cv.Sobel(gray_im, cv.CV_16S, 1, 0)
# edge_sobel_y = cv.Sobel(gray_im, cv.CV_16S, 0, 1)
# absX = cv.convertScaleAbs(edge_sobel_x)  # 转回uint8
# absY = cv.convertScaleAbs(edge_sobel_y)
# edge_sobel = cv.addWeighted(absX, 0.5, absY, 0.5, 0)
# cv.imshow("Sobel", edge_sobel)
# cv.waitKey(0)
#
# # Laplacian
# edge_lap = cv.Laplacian(gray_im, cv.CV_16S)
# edge_lap = cv.convertScaleAbs(edge_lap)
# cv.imshow('Laplacian', edge_lap)
# cv.waitKey(0)
#
# # Canny
# edge_canny = cv.Canny(gray_im, 50, 150)
# cv.imshow('Canny', edge_canny)
# cv.waitKey(0)

# # 8.Add random noise in a grayscale image
# # gaussian noise
# def clamp(pv):
#     """防止溢出"""
#     if pv > 255:
#         return 255
#     elif pv < 0:
#         return 0
#     else:
#         return pv
#
#
# def gaussian_noise_demo(image):
#     """添加高斯噪声"""
#     h, w, c = image.shape
#     for row in range(0, h):
#         for col in range(0, w):
#             s = np.random.normal(0, 15, 3)  # 产生随机数，每次产生三个
#             b = image[row, col, 0]  # blue
#             g = image[row, col, 1]  # green
#             r = image[row, col, 2]  # red
#             image[row, col, 0] = clamp(b + s[0])
#             image[row, col, 1] = clamp(g + s[1])
#             image[row, col, 2] = clamp(r + s[2])
#     return image
#
#
# noise = gaussian_noise_demo(original)
# cv.imshow("noise img", noise)
# cv.waitKey(0)
#
# # 9.Remove the noise added in the above operation
# remove_noise = cv.GaussianBlur(noise, (5, 5), 0)
# cv.imshow("gaussian blur img", remove_noise)
# cv.waitKey(0)


# # 10.Binarize a grayscale image. Add track bar GUI to change the threshold
# # 添加新窗口
# cv.namedWindow('test_threshold')
# # 创建滑块,注册回调函数 lambda x: None没有滑动时
# cv.createTrackbar('num', 'test_threshold', 0, 255, lambda x: None)
#
# while 1:
#     num = cv.getTrackbarPos("num", "test_threshold")
#     ret, thresh = cv.threshold(original, num, 255, cv.THRESH_BINARY)
#     cv.imshow('test_threshold', thresh)
#     k = cv.waitKey(1) & 0xFF
#     if k == 27:
#         break
# cv.destroyAllWindows()


# 11.Apply labeling operation to a binarized image
# 阈值分割得到二值化图片
ret, binary_im = cv.threshold(gray_im, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
cv.imshow('binary', binary_im)
cv.waitKey(0)

# # 膨胀操作
# kernel = cv.getStructuringElement(cv.MORPH_RECT, (3, 3))
# bin_clo = cv.dilate(binary_im, kernel, iterations=2)
# cv.imshow('bin_clo', bin_clo)
# cv.waitKey(0)

# 连通域分析
num_labels, labels, stats, centroids = cv.connectedComponentsWithStats(binary_im, connectivity=8)

# 查看各个返回值
# 连通域数量
print('num_labels = ',num_labels)
# 连通域的信息：对应各个轮廓的x、y、width、height和面积
print('stats = ',stats)
# 连通域的中心点
print('centroids = ',centroids)
# 每一个像素的标签1、2、3.。。，同一个连通域的标签是一致的
print('labels = ',labels)

# 不同的连通域赋予不同的颜色
output = np.zeros((original.shape[0], original.shape[1], 3), np.uint8)
for i in range(1, num_labels):

    mask = labels == i
    output[:, :, 0][mask] = np.random.randint(0, 255)
    output[:, :, 1][mask] = np.random.randint(0, 255)
    output[:, :, 2][mask] = np.random.randint(0, 255)
cv.imshow('label', output)
cv.waitKey(0)
cv.destroyAllWindows()


