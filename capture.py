import cv2
import os

def capture(file_name): # file_name은 경로가 포함되어야 함.
    
    video_file = file_name.split("\\")[-1].split(".")[0] # 경로와 확장자를 제외한 비디오의 이름.
    print(video_file)
    create_path = f"C:\\workspace\\real_gauge\\images\\{video_file}" # 캡쳐 이미지를 생성할 디렉토리.
    try:
        if not os.path.exists(create_path):
            os.makedirs(create_path)
    except OSError:
        print ('Error: Creating directory. ' +  create_path)
    
    cap = cv2.VideoCapture(file_name) # 지정한 경로에 해당하는 비디오를 잡음.
    i = 0 # 캡쳐된 이미지에 부여될 번호

    count = 0 # 캡쳐될 이미지 수를 제어하기 위함.
    while(cap.isOpened()):
        ret, frame = cap.read()

        # This condition prevents from infinite looping
        # incase video ends.
        if ret == False:
            break

        if count % 14 == 0 :
            cv2.imwrite(os.path.join(create_path , str(i)+'.jpg') , frame) # Save Frame by Frame into disk using imwrite method
            i += 1
        count += 1
  
    cap.release()
    cv2.destroyAllWindows()
