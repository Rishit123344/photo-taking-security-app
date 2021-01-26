import cv2
def takesnapshot():
    videocaptureobject=cv2.VideoCapture(0)
    result=True
    while(result):
        ret,frame=videocaptureobject.read()
        print(ret)
        print(frame)
        cv2.imwrite('newimage.jpg',frame)
        result=False
    videocaptureobject.release()
    cv2.destroyAllWindows()
takesnapshot()    