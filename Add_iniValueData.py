
import configparser
from tkinter import filedialog, simpledialog, Tk, Toplevel, Listbox, Button, Label, StringVar
from tkinter.ttk import Combobox

def select_ini_file():
    root = Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(title="Select INI file", filetypes=[("INI files", "*.ini")])
    return file_path

def get_user_input():
    input_window = Tk()
    input_window.title("Select Values")

    resize_var = StringVar(value=None)  # Set Init None
    qfactor_var = StringVar(value=None)  # Set Init None

    selected_values = [None, None]  # [resize_value, qfactor_value]

    def update_resize_value(event=None):
        resize_var.set(resize_combobox.get())

    def update_qfactor_value(event=None):
        qfactor_var.set(qfactor_combobox.get())

    def on_ok():
        if resize_var.get():
            selected_values[0] = resize_var.get()
        if qfactor_var.get():
            selected_values[1] = qfactor_var.get()
        input_window.quit()

    Label(input_window, text="Select Value for Jpg Resize:").pack(pady=10)
    combobox_values = [str(i) for i in range(10, 110, 10)]
    resize_combobox = Combobox(input_window, textvariable=resize_var, values=combobox_values, postcommand=update_resize_value)
    resize_combobox.bind('<<ComboboxSelected>>', update_resize_value)  # 선택이 변경될 때마다 함수를 호출
    resize_combobox.pack(pady=10)

    Label(input_window, text="Select Value for Jpg Qfactor:").pack(pady=10)
    qfactor_combobox = Combobox(input_window, textvariable=qfactor_var, values=combobox_values, postcommand=update_qfactor_value)
    qfactor_combobox.bind('<<ComboboxSelected>>', update_qfactor_value)  # 선택이 변경될 때마다 함수를 호출
    qfactor_combobox.pack(pady=10)

    ok_button = Button(input_window, text="OK", command=on_ok)
    ok_button.pack(pady=20)

    input_window.mainloop()
    input_window.destroy()

    return selected_values[0], selected_values[1]

def update_ini(file_path, resize_value, qfactor_value):
    config = configparser.ConfigParser()
    config.read(file_path)
    
    img_count = int(config['IMG Information']['img count'])

    for i in range(1, img_count + 1):
        section_name = f'IMG{str(i).zfill(4)}'
        if section_name not in config:
            config[section_name] = {}
        if resize_value and (not config[section_name].get('Jpg Resize') or config[section_name]['Jpg Resize'] != resize_value):
            config[section_name]['Jpg Resize'] = resize_value
        if qfactor_value and (not config[section_name].get('Jpg Qfactor') or config[section_name]['Jpg Qfactor'] != qfactor_value):
            config[section_name]['Jpg Qfactor'] = qfactor_value

    with open(file_path, 'w') as configfile:
        config.write(configfile)

def main():
    file_path = select_ini_file()
    if not file_path:
        print("No INI file selected!")
        return

    resize_value, qfactor_value = get_user_input()
    if resize_value is None and qfactor_value is None:
        print("No values provided!")
        return

    update_ini(file_path, resize_value, qfactor_value)


if __name__ == "__main__":
    main()
