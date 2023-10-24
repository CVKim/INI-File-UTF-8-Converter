
import configparser
from tkinter import filedialog
from tkinter import Tk

def select_ini_file():
    # Select ini file - Tk Lib
    root = Tk()
    root.withdraw()  # 주 창을 숨깁니다.
    file_path = filedialog.askopenfilename(title="Select INI file", filetypes=[("INI files", "*.ini")])
    return file_path

def update_ini(file_path):
    # INI File lOAD
    config = configparser.ConfigParser()
    config.read(file_path)

    # [IMG Information] 섹션에서 'img count' 값 Read
    img_count = int(config['IMG Information']['img count'])

    # [IMG0001] ~ [IMG0028] 섹션에 'Jpg Qfactor = 10'을 add
    for i in range(1, img_count + 1):
        section_name = f'IMG{str(i).zfill(4)}'
        if section_name not in config:
            config[section_name] = {}
        config[section_name]['Jpg Resize'] = '50'
        config[section_name]['Jpg Qfactor'] = '70'

    # 수정 후, 저장
    with open(file_path, 'w') as configfile:
        config.write(configfile)

def main():
    ini_file_path = select_ini_file()
    if ini_file_path:  # User Select File
        update_ini(ini_file_path)
        print(f"Updated {ini_file_path} successfully!")
    else:
        print("No file selected!")

if __name__ == "__main__":
    main()
