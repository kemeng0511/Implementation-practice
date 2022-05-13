import numpy as np
import cv2 as cv
import glob

# images = cv.imdecode(np.fromfile("E:/PyCharm Community Edition 2020.1.1/IP/img/chessboard.jpg", dtype=np.uint8), -1)
# cv.imshow("building", original)
# cv.waitKey(0)


# 找棋盘格角点
# 阈值
criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 30, 0.001)
# 棋盘格模板规格
w = 7
h = 7
# 世界坐标系中的棋盘格点,例如(0,0,0), (1,0,0), (2,0,0) ....,(8,5,0)，去掉Z坐标，记为二维矩阵
objp = np.zeros((w * h, 3), np.float32)
objp[:, :2] = np.mgrid[0:w, 0:h].T.reshape(-1, 2)
# 储存棋盘格角点的世界坐标和图像坐标对
objpoints = []  # 在世界坐标系中的三维点
imgpoints = []  # 在图像平面的二维点

images = glob.glob('E:/PyCharm Community Edition 2020.1.1/IP/img/calib/*.jpg')


def draw(image, corner, imgpts):
    corner = tuple(corner[0].ravel())
    image = cv.line(image, corner, tuple(imgpts[0].ravel()), (255, 0, 0), 5)
    image = cv.line(image, corner, tuple(imgpts[1].ravel()), (0, 255, 0), 5)
    image = cv.line(image, corner, tuple(imgpts[2].ravel()), (0, 0, 255), 5)
    return image


for fname in images:
    img = cv.imread(fname)
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    # 找到棋盘格角点
    ret, corners = cv.findChessboardCorners(gray, (w, h), None)
    # 如果找到足够点对，将其存储起来
    if ret == True:
        cv.cornerSubPix(gray, corners, (11, 11), (-1, -1), criteria)
        objpoints.append(objp)
        imgpoints.append(corners)
        # 将角点在图像上显示
        cv.drawChessboardCorners(img, (w, h), corners, ret)
        cv.imshow('findCorners', img)
        cv.waitKey(0)
    cv.destroyAllWindows()

    # 标定
    ret, mtx, dist, rvecs, tvecs = cv.calibrateCamera(objpoints, imgpoints, gray.shape[::-1], None, None)
    print("Camera Matrix : \n") # 内参矩阵
    print(mtx)
    print("Distortion Parameters : \n")
    print(dist)
    print("Rotation Vectors : \n")
    print(rvecs)
    print("Translate Vectors: \n")
    print(tvecs)

# # 去畸变
# img2 = cv.imread('calib/00169.png')
# h, w = img2.shape[:2]
# newcameramtx, roi = cv.getOptimalNewCameraMatrix(mtx, dist, (w, h), 0, (w, h))  # 自由比例参数
# dst = cv.undistort(img2, mtx, dist, None, newcameramtx)
# # 根据前面ROI区域裁剪图片
# # x,y,w,h = roi
# # dst = dst[y:y+h, x:x+w]
# # cv.imwrite('calibresult.png',dst)



# 反投影误差
    total_error = 0
    for i in range(len(objpoints)):
        imgpoints2, _ = cv.projectPoints(objpoints[i], rvecs[i], tvecs[i], mtx, dist)
        error = cv.norm(imgpoints[i], imgpoints2, cv.NORM_L2)
        total_error += error*error
    print( "rms error: {}".format(np.sqrt(total_error/(len(objpoints)*len(imgpoints2)))))
    # # 将重投影点在图像上显示
    # cv.drawChessboardCorners(img, (w, h), imgpoints2, True)
    # cv.imshow('Reprojected Points', img)
    # cv.waitKey(0)
    # cv.destroyAllWindows()

    # 使用solvePnP
    exact_corners = cv.cornerSubPix(gray, corners, (11, 11), (-1, -1), criteria)
    _, rvec, tvec, inliers = cv.solvePnPRansac(objp, exact_corners, mtx, dist)
    print("Axis in the 2D: ", imgpoints2)


