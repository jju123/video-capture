from capture import capture
from os import listdir
from os.path import isfile, join

my_file = "C:\\workspace\\real_gauge\\all" # 비디오들이 있는 디렉토리의 디렉토리. (이 디렉토리에는 비디오를 담은 디렉토리들이 있어야 함.)
files = [f for f in listdir(my_file) if isfile(join(my_file, f))]

for file in files:
    capture(f"C:\\workspace\\real_gauge\\all\\{file}") # 이 디렉토리 내의 capture.py 참고
    
