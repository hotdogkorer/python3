import cv2 as cv
import numpy as np
import os

vid_path = "C:/label/MG/labelImg/bf_1flag/"  # 영상이 있는 폴더 경로
#vid_path = "C:/label/MG/vid/"  # 영상이 있는 폴더 경로
frame_path = "C:/label/MG/labelImg/af/flag/"  # 캡처한 프레임들을 저장 할 경로


def video_list(list, name, i):
    temp = []
    for file in list:
        print(file.split(sep=".")[i])
        if file.split(sep=".")[i] != name:
            list.remove(file)
            print(file)
        else:
            temp.append(file)
    return temp


if __name__ == "__main__":
    file_list = os.listdir(vid_path)  # vid_path 내의 모든 file 들을 불러옴
    print(file_list)
    # file_list = video_list(file_list, "mp4", 0)  # list 내의 video file 들만 가져옴
    # print(file_list)

    # frame capture
    for index, file in enumerate(file_list):
        count = 1

        if True:

            if os.path.exists(frame_path + file) == True:
                print(f"file or dir is alread exist - {file}")
                pass
            else:
                try:
                    os.makedirs(frame_path + file)
                except:
                    print(f"mkdir - {file}")
                    pass
            vidcap = cv.VideoCapture(vid_path + file)

            print(vid_path + file)
            while True:
                try:
                    _, frame = vidcap.read()
                    cv.imwrite(frame_path + file +
                               f"/{file.split('.')[0]} {count}.jpg", frame)
                    print(
                        f"saved frame {file} - {count}.jpg has successfully completed!")

                    if cv.waitKey(10) == 27:
                        break
                except:
                    print("save done! " + file)
                    break

                count += 1
