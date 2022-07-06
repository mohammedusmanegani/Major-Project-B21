import enum
import os
import cv2
import sys

from numpy import average


class SIZE_UNIT(enum.Enum):
    BYTES = 1
    KB = 2
    MB = 3
    GB = 4


def convert_unit(size_in_bytes, unit):
    """ Convert the size from bytes to other units like KB, MB or GB"""
    if unit == SIZE_UNIT.KB:
        return size_in_bytes/1024
    elif unit == SIZE_UNIT.MB:
        return size_in_bytes/(1024*1024)
    elif unit == SIZE_UNIT.GB:
        return size_in_bytes/(1024*1024*1024)
    else:
        return size_in_bytes


def get_file_size(file_name, size_type=SIZE_UNIT.BYTES):
    """ Get file in size in given unit like KB, MB or GB"""
    size = os.path.getsize(file_name)
    return convert_unit(size, size_type)


differenceFrameFolderpath = 'E:/College Stuff/SDMCET/8th Sem/Project/Application/frame_detection_v1/logs/differenceFrame'
differenceFrameFolderSize = 0
for path, dirs, files in os.walk(differenceFrameFolderpath):
    for f in files:
        fp = os.path.join(path, f)
        differenceFrameFolderSize += get_file_size(fp, SIZE_UNIT.MB)

reconstructedFolderpath = 'E:/College Stuff/SDMCET/8th Sem/Project/Application/frame_detection_v1/logs/reconstructed'
reconstructedFolderSize = 0
for path, dirs, files in os.walk(reconstructedFolderpath):
    for f in files:
        fp = os.path.join(path, f)
        reconstructedFolderSize += get_file_size(fp, SIZE_UNIT.MB)

image = cv2.imread("bg.jpg")
diffInSize = abs(round(reconstructedFolderSize - differenceFrameFolderSize, 2))
bandwidthSaved = "Bandwidth Saved: " + str(diffInSize) + "MB"
coordinates1 = (350, 350)
coordinates2 = (350, 450)
coordinates3 = (350, 550)
coordinates4 = (350, 750)
coordinates5 = (350, 850)
font = cv2.FONT_HERSHEY_SIMPLEX
fontScale = 2.5
color = (0, 0, 0)
thickness = 3
totalTime = "In " + str(sys.argv[1]) + " Seconds"
avgFps = "Average FPS: " + str(sys.argv[2]) + "fps"
oneHourDataSaving = (diffInSize * 3600) / float(sys.argv[1])
oneHourDataSavingText = "You Save " + \
    str(round(oneHourDataSaving, 2)) + "MB in 1 Hour"
twelveHourDataSaving = (diffInSize * 43200) / float(sys.argv[1])
twelveHourDataSavingText = "You Save " + \
    str(round(twelveHourDataSaving, 2)) + "MB in 12 Hours"
cv2.putText(image, avgFps, coordinates1, font,
            fontScale, color, thickness, cv2.LINE_AA)

cv2.putText(image, bandwidthSaved, coordinates2, font,
            fontScale, color, thickness, cv2.LINE_AA)

cv2.putText(image, totalTime, coordinates3, font,
            fontScale, color, thickness, cv2.LINE_AA)

cv2.putText(image, oneHourDataSavingText, coordinates4, font,
            fontScale, color, thickness, cv2.LINE_AA)

cv2.putText(image, twelveHourDataSavingText, coordinates5, font,
            fontScale, color, thickness, cv2.LINE_AA)

image = cv2.resize(image, (780, 480))

while True:
    if cv2.waitKey(10) == ord('q'):
        break
    cv2.imshow("Stats", image)

cv2.destroyAllWindows()
