import cv2

def take_snapshot():
    videoCaptureObject = cv2.VideoCapture(0)
    result = True

    while(result):
        imagePath = 'C:/yash WHJ Python/C102/picture1.jpg'
        print(imagePath)
        ret, frame = videoCaptureObject.read()
        cv2.imwrite(imagePath, frame)
        print(frame)
        result = False
    
    videoCaptureObject.release()
    cv2.destroyAllWindows()

take_snapshot()