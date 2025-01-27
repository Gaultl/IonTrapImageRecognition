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


images = getFilePaths(r"C:\Users\laure\OneDrive\images\ISEFDOE_HighAC_HighDC")
areas = []
times = []
i = 0
time = 0
denom = 0

color = 255

for image in images:
    im = cv.imread(image, 0)
    pixels = 0

    height, width = im.shape

    ret, thresh1 = cv.threshold(im, 75, 255, cv.THRESH_BINARY)

    # Calculate area
    for j in thresh1:
        for k in j:
            if k != 0:
                pixels += 1

    if i == 0:
        denom = pixels

    print(pixels/denom)
    areas.append(pixels/denom)
    times.append(time)
    time += 15

    if i <= 10:
        # Show keypoints
        cv.imshow("Blobs Using Color", thresh1)
        cv.waitKey(0)
        cv.destroyAllWindows()
        i += 1

plt.plot(times, areas, color='red')
plt.title(input("Enter the title of the graph:\n"))
plt.show()

pic = 0
while pic < len(areas):
    if areas[pic] == 0:
        del areas[pic]
        del times[pic]
        pic -= 1
    pic += 1

csv = np.transpose(np.array([times, areas]))

print(csv)

# print(ions)
# print(times)
# print(images)

# Saves data as a csv file
print("Enter the name of your file (include .csv at the end)")
csvName = input()
np.savetxt(csvName, csv, delimiter=",")
