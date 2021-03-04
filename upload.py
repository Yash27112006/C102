import dropbox
import cv2
import time
import random
start_time = time.time()

def take_snapshot():
    number = random.randint(0, 100)
    videoCaptureObject = cv2.VideoCapture(0)
    result = True

    while(result):

        ret, frame = videoCaptureObject.read()
        img_name = "img"+str(number)+".png"
        cv2.imwrite(img_name, frame)
        start_time = time.time()
        print(frame)
        result = False
        
    return img_name
    print("Snapshot taken !!")
    videoCaptureObject.release()
    cv2.destroyAllWindows()

def upload_file(img_name):
    access_token = '3hotC_0PXGMAAAAAAAAAAZtOy-R-5bUbvhCcSvWOF7iDrNmJCgoqys8ANGZYwo8b'
    file = img_name
    file_from = file
    file_to = "/test/"+(img_name)
    #file_to = input("Enter the full path to upload to dropbox:- ")
    dbx = dropbox.Dropbox(access_token)

    with open(file_from, 'rb') as f:
        dbx.files_upload(f.read(), file_to, mode=dropbox.files.WriteMode.overwrite)
        print("File uploaded !!")

def main():
    while(True):
        if((time.time()-start_time)>=10):
            name = take_snapshot()
            upload_file(name)

main()