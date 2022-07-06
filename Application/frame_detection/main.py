import cv2
import winsound
import numpy as np
import glob
import os
import time
import math

start = time.time()

dir = 'logs/reconstructed'
for f in os.listdir(dir):
    os.remove(os.path.join(dir, f))

dir = 'logs/differenceFrame'
for f in os.listdir(dir):
    os.remove(os.path.join(dir, f))

dir = 'logs/currectDifferenceFrame'
for f in os.listdir(dir):
    os.remove(os.path.join(dir, f))

# For camera ID
camera_id = 0
i = 0

prev_frame_time = 0
new_frame_time = 0
avgFps = 0

cam = cv2.VideoCapture(camera_id, cv2.CAP_DSHOW)
while cam.isOpened():
    ret, frame1 = cam.read()
    ret, frame2 = cam.read()
    diff = cv2.absdiff(frame1, frame2)
    gray = cv2.cvtColor(diff, cv2.COLOR_RGB2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
    dilated = cv2.dilate(thresh, None, iterations=3)
    contours, _ = cv2.findContours(
        dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    gray = frame1
    gray = cv2.resize(gray, (500, 300))
    font = cv2.FONT_HERSHEY_SIMPLEX
    new_frame_time = time.time()
    fps = 1/(new_frame_time-prev_frame_time)
    prev_frame_time = new_frame_time
    fps = int(fps)
    avgFps += fps
    fps = str(fps)

    for c in contours:
        if cv2.contourArea(c) < 5000:
            continue
        x, y, w, h = cv2.boundingRect(c)
        cv2.rectangle(frame1, (x, y), (x+w, y+h), (0, 255, 0), 2)

        cv2.imwrite('logs/reconstructed/reconstructed'+str(i)+'.jpg', frame2)
        cv2.imwrite('logs/differenceFrame/differenceFrame'+str(i)+'.jpg', diff)
        cv2.imwrite(
            'logs/currectDifferenceFrame/currectDifferenceFrame.jpg', diff)

        winsound.PlaySound('alert.wav', winsound.SND_ASYNC)
    if cv2.waitKey(10) == ord('q'):
        break

    cv2.putText(frame1, fps+'fps', (5, 48), font,
                1.5, (0, 0, 0), 2, cv2.LINE_AA)

    camInfo = 'Cam ' + str(camera_id)

    cv2.putText(frame1, camInfo, (520, 40), font,
                1, (0, 0, 0), 2, cv2.LINE_AA)

    cv2.imshow('Frame Detection', frame1)

    i += 1

avgFps = avgFps / i
cv2.destroyAllWindows()

img_array = []
for filename in glob.glob('E:/College Stuff/SDMCET/8th Sem/Project/Application/frame_detection_v1/logs/differenceFrame/*.jpg'):
    img = cv2.imread(filename)
    height, width, layers = img.shape
    size = (width, height)
    img_array.append(img)


out = cv2.VideoWriter('E:/College Stuff/SDMCET/8th Sem/Project/Application/frame_detection_v1/logs/differenceFrames.avi',
                      cv2.VideoWriter_fourcc(*'DIVX'), 8, size)

for i in range(len(img_array)):
    out.write(img_array[i])
out.release()

img_array = []
for filename in glob.glob('E:/College Stuff/SDMCET/8th Sem/Project/Application/frame_detection_v1/logs/reconstructed/*.jpg'):
    img = cv2.imread(filename)
    height, width, layers = img.shape
    size = (width, height)
    img_array.append(img)


out = cv2.VideoWriter('E:/College Stuff/SDMCET/8th Sem/Project/Application/frame_detection_v1/logs/reconstructed.avi',
                      cv2.VideoWriter_fourcc(*'DIVX'), 6, size)

for i in range(len(img_array)):
    out.write(img_array[i])
out.release()
end = time.time()
totalTime = end - start
os.system('python .\\play.py')
cv2.destroyAllWindows()
os.system('%s %s %s %s' % ('python', '.\\stats.py',
          round(totalTime, 2), math.trunc(avgFps)))
