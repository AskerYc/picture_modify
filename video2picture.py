import cv2


def video2picture(video_name, aim_path):
    video_path = 'videos/' + video_name
    vc = cv2.VideoCapture(video_path)
    c = 1
    if vc.isOpened():
        rval, frame = vc.read()
        while rval:
            cv2.imwrite(aim_path + '/' + str(c) + '.jpg', frame)
            c += 1
            cv2.waitKey(1)
            rval, frame = vc.read()
    else:
        rval = False


if __name__ == '__main__':
    video2picture('my_face.mp4', 'my_face')
