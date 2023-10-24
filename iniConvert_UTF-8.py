import os
import chardet
import tkinter as tk
from tkinter import filedialog

def change_encoding_to_utf8(filepath):
    # 파일의 현재 인코딩을 탐지
    with open(filepath, 'rb') as f:
        detected = chardet.detect(f.read())
        current_encoding = detected['encoding']

    # 인코딩이 UTF-8이 아니면, UTF-8로 변환
    if current_encoding and current_encoding != 'utf-8':
        try:
            with open(filepath, 'r', encoding=current_encoding) as f:
                file_contents = f.read()

            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(file_contents)
            
            print(f"Converted {filepath} to UTF-8.")  # 변경한 파일 이름 출력

        except UnicodeDecodeError:
            # 인코딩 탐지가 잘못됐을 경우의 예외 처리
            print(f"Error decoding {filepath} using {current_encoding}. Trying another encoding.")

            try:
                with open(filepath, 'r', encoding='ISO-8859-1') as f:
                    file_contents = f.read()

                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(file_contents)
                
                print(f"Converted {filepath} to UTF-8.")  # 변경한 파일 이름 출력

            except Exception as e:
                print(f"Failed to decode {filepath}. Error: {e}")
    else:
        print(f"{filepath} is already in UTF-8.")  # 이미 UTF-8 인코딩된 파일 알림

def check_and_change_ini_files(directory):
    # 지정한 경로에서 .ini 파일 목록을 가져옴
    ini_files = [f for f in os.listdir(directory) if f.endswith('.ini')]

    # 각 .ini 파일에 대해 인코딩 확인 및 변경 실행
    for ini_file in ini_files:
        filepath = os.path.join(directory, ini_file)
        change_encoding_to_utf8(filepath)
        print("INI File Convet Processing End!!")

# tkinter Disable
root = tk.Tk()
root.withdraw()

# directory pop-up
directory_path = filedialog.askdirectory()

# 선택한 디렉토리 내의 .ini 파일들의 인코딩 확인 및 변경
if directory_path:  # 사용자가 디렉토리를 선택했을 경우만 실행
    check_and_change_ini_files(directory_path)
