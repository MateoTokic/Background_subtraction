import cv2

video = cv2.VideoCapture('traffic2.mp4')

background_subtractor = cv2.createBackgroundSubtractorKNN(history=2000,dist2Threshold=400, detectShadows=False)

for i in range(400):
    ret, frame = video.read()
    if not ret:
        break
    background_subtractor.apply(frame)
    

bg = background_subtractor.getBackgroundImage()


cv2.imshow('Background', bg)

while True:
    ret, frame = video.read()

    if not ret:
        break

    fg_mask = background_subtractor.apply(frame)


    bg_mask = cv2.bitwise_not(fg_mask)

    result = cv2.bitwise_and(frame, bg, mask=bg_mask)

    frame[fg_mask == 255] = bg[fg_mask == 255]

    cv2.imshow('Foreground mask',fg_mask)
    cv2.imshow('Result', frame)
    cv2.waitKey(1)
    

video.release()
cv2.destroyAllWindows()
