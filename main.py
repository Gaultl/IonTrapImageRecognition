# Standard imports
import cv2 as cv
import numpy as np

# Read image
# im = cv.imread(r"C:\Users\laure\Pictures\longBlobs.jpg", 0)
# im = cv.imread(r"C:\Users\laure\Downloads\IMG_5756.jpg", 0)
# im = cv.imread(r"C:\Users\laure\Downloads\IMG_3588.PNG", 0)
# im = cv.imread(r"C:\Users\laure\Downloads\IMG_3587.PNG", 0)
# im = cv.imread(r"C:\Users\laure\Downloads\IMG_3585.PNG", 0)
# im = cv.imread(r"C:\Users\laure\Downloads\16072.jpg", 0)
# im = cv.imread(r"C:\Users\laure\Pictures\QSYSLongBlobs.jpg", 0)

height, width = im.shape

params = cv.SimpleBlobDetector_Params()

color = 255

params.minThreshold = 1
params.maxThreshold = 255

# params.filterByArea = True
# params.minArea = 15
# params.maxArea = 10000
#
params.filterByColor = True
params.blobColor = color

# params.filterByCircularity = True
# params.minCircularity = 0.785
# params.maxCircularity = 1

# while color > 0:
#     params.blobColor = color
#     detector = cv.SimpleBlobDetector_create(params)
#
#     keypoints = detector.detect(im)
#
#     if len(keypoints) != 0:
#         print((len(keypoints)))
#         print(color)
#
#     color -= 1


detector = cv.SimpleBlobDetector_create(params)

down_width = int(width)
down_height = int(height)
down_points = (down_width, down_height)
resized_down = cv.resize(im, down_points, interpolation= cv.INTER_LINEAR)

# Detect blobs.
keypoints = detector.detect(resized_down)

# Draw detected blobs as red circles.
# cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures the size of the circle corresponds to the size of blob
blank = np.zeros((1, 1))
blobs = cv.drawKeypoints(resized_down, keypoints, blank, (0, 0, 255), cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

down_width = int(width)
down_height = int(height)
down_points = (down_width, down_height)
resized_down = cv.resize(blobs, down_points, interpolation= cv.INTER_LINEAR)

print(len(keypoints))

# Show keypoints
cv.imshow("Blobs Using Color", resized_down)
cv.waitKey(0)
cv.destroyAllWindows()
