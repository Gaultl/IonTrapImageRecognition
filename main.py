# Standard imports
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import os


def getFilePaths(folderPath):
    pathList = []
    # folderPath = input("Enter folder path:\n")
    for file in os.listdir(folderPath):
        pathList.append(os.path.join(folderPath, file))
    return pathList


images = getFilePaths(r"C:\Users\laure\OneDrive\images\ISEFDOE_HighAC_LowDC")
ions = []
times = []
i = 0
time = 0

#Setup detector
params = cv.SimpleBlobDetector_Params()

color = 255

params.filterByArea = False

params.filterByColor = True
params.blobColor = 255

params.filterByCircularity = False

params.filterByInertia = True
params.minInertiaRatio = .001
params.maxInertiaRatio = 10

params.filterByConvexity = True
params.minConvexity = 0.001
params.maxConvexity = 10

detector = cv.SimpleBlobDetector_create(params)

for image in images:
    im = cv.imread(image, 0)

    height, width = im.shape

    ret, thresh1 = cv.threshold(im, 75, 255, cv.THRESH_BINARY)

    # Detect blobs.
    keypoints = detector.detect(thresh1)

    # Draw detected blobs as red circles.
    # cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures the size of the circle corresponds to the size of blob
    blank = np.zeros((1, 1))
    blobs = cv.drawKeypoints(thresh1, keypoints, blank, (0, 0, 255), cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

    down_width = int(width)
    down_height = int(height)
    down_points = (down_width, down_height)
    resized_down = cv.resize(blobs, down_points, interpolation=cv.INTER_LINEAR)

    print(len(keypoints))
    ions.append(len(keypoints))
    # times.append(image[-10:-6])
    times.append(time)
    time += 15

    if i <= 10:
        # Show keypoints
        cv.imshow("Blobs Using Color", resized_down)
        cv.waitKey(0)
        cv.destroyAllWindows()
        i += 1

plt.plot(times, ions, color='red')
plt.show()

pic = 0
while pic < len(ions):
    if ions[pic] == 0:
        del ions[pic]
        del times[pic]
        pic -= 1
    pic += 1

csv = np.transpose(np.array([ions, times]))

print(csv)

print(ions)
print(times)
# print(images)

# Saves data as a csv file
print("Enter the name of your file (include .csv at the end)")
csvName = input()
np.savetxt(csvName, csv, delimiter=",")

# y = [ions[1], ions[int(1*(len(ions)/8))], ions[int(2*(len(ions)/8))], ions[int(3*(len(ions)/8))], ions[int(4*(len(ions)/8))], ions[int(5*(len(ions)/8))], ions[int(6*(len(ions)/8 - 1))], ions[int(7*(len(ions)/8 - 1))], ions[int(8*(len(ions)/8 - 1))]]#, ions[int(9*(len(ions)/11))]]
# x = [times[1], times[int(1*(len(ions)/8))], times[int(2*(len(ions)/8))], times[int(3*(len(ions)/8))], times[int(4*(len(ions)/8))], times[int(5*(len(ions)/8))], times[int(6*(len(ions)/8 - 1))], times[int(7*(len(ions)/8 - 1))], times[int(8*(len(ions)/8 - 1))]] #, times[int(9*(len(ions)/11))]]
#
# print(x)
# print(y)

# plt.plot(times, ions, color = 'blue')
# plt.show()

# Test images

# im = cv.imread(r"C:\Users\laure\Pictures\longBlobs.jpg", 0)
# im = cv.imread(r"C:\Users\laure\Downloads\IMG_5756.jpg", 0)
# im = cv.imread(r"C:\Users\laure\Downloads\IMG_3588.PNG", 0)
# im = cv.imread(r"C:\Users\laure\Downloads\IMG_3587.PNG", 0)
# im = cv.imread(r"C:\Users\laure\Downloads\IMG_3585.PNG", 0)
# im = cv.imread(r"C:\Users\laure\Downloads\16072.jpg", 0)
# im = cv.imread(r"C:\Users\laure\Pictures\QSYSLongBlobs.jpg", 0)
# im = cv.imread(r"C:\Users\laure\Downloads\IMG_5478.jpg", 0)
# im = cv.imread(r"C:\Users\laure\Downloads\IMG_5477.jpg", 0)
# im = cv.imread(r"C:\Users\laure\Downloads\IMG_5476.jpg", 0)
# im = cv.imread(r"C:\Users\laure\Downloads\dino_lite\A018 - 20241019_225011.bmp", 0)
# im = cv.imread(r"C:\Users\laure\Downloads\dino_lite\A019 - 20241019_225120.bmp", 0)
# im = cv.imread(r"C:\Users\laure\Downloads\dino_lite\A020 - 20241019_225122.bmp", 0)
# im = cv.imread(r"C:\Users\laure\Downloads\dino_lite\A021 - 20241019_225129.bmp", 0)
# im = cv.imread(r"C:\Users\laure\Downloads\dino_lite\A022 - 20241019_225132.bmp", 0)
# im = cv.imread(r"C:\Users\laure\Downloads\dino_lite\A023 - 20241019_225143.bmp", 0)
# im = cv.imread(r"C:\Users\laure\Downloads\dino_lite\A024 - 20241019_225146.bmp", 0)
# im = cv.imread(r"C:\Users\laure\Downloads\dino_lite_2\A034 - 20241020_102804.bmp", 0)
# im = cv.imread(r"C:\Users\laure\Downloads\dino_lite_2\A035 - 20241020_102817.bmp", 0)
# im = cv.imread(r"C:\Users\laure\Downloads\dino_lite_2\A036 - 20241020_102819.bmp", 0)
# im = cv.imread(r"C:\Users\laure\Downloads\dino_lite_2\A037 - 20241020_102821.bmp", 0)
# im = cv.imread(r"C:\Users\laure\Downloads\dino_lite_2\A038 - 20241020_102822.bmp", 0)
# im = cv.imread(r"C:\Users\laure\Downloads\dino_lite_2\A039 - 20241020_102824.bmp", 0)
# im = cv.imread(r"C:\Users\laure\Downloads\dino_lite_2\A040 - 20241020_102826.bmp", 0)
# im = cv.imread(r"C:\Users\laure\Downloads\dino_lite_2\A041 - 20241020_102829.bmp", 0)
# im = cv.imread(r"C:\Users\laure\Downloads\dino_lite_2\A042 - 20241020_102831.bmp", 0)
# im = cv.imread(r"C:\Users\laure\Downloads\dino_lite_2\A043 - 20241020_102833.bmp", 0)
# im = cv.imread(r"C:\Users\laure\Pictures\CroppedA041 - 20241020_102829.bmp", 0)
# im = cv.imread(r"C:\Users\laure\Downloads\A046 - 20241020_110019.bmp", 0)
# im = cv.imread(r"C:\Users\laure\Downloads\A053 - 20241020_110028.bmp", 0)
