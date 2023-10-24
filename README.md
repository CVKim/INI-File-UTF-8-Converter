INI File Utilities
This repository contains Python utilities for handling .ini files. These utilities provide functionalities like encoding conversion, GUI-based value selection, and value updates.

Table of Contents
Getting Started
Usage
Function Descriptions
Contributing
Getting Started
To use these tools, simply run the corresponding Python script. Each script provides its own user interface for ease of use.

Usage
A. INI File UTF-8 Converter
Execute the A script.
A GUI will prompt you to select a directory containing .ini files.
The script will process each .ini file in the directory. If an .ini file is not in UTF-8 encoding, the script will convert it.
B. INI File Value Selector and Updater
Execute the B script.
A GUI will prompt you to select an .ini file.
Another GUI will allow you to select values for "Jpg Resize" and "Jpg Qfactor".
The selected values will be updated or added in the .ini file under the corresponding sections.
C. INI File Direct Updater
Execute the C script.
A GUI will prompt you to select an .ini file.
The script will then directly set "Jpg Resize" to '50' and "Jpg Qfactor" to '70' for all relevant sections in the .ini file.
Function Descriptions
change_encoding_to_utf8(filepath)
Purpose: Checks the encoding of a file and converts it to UTF-8 if it's not already in UTF-8.
Parameters:
filepath: Path of the .ini file to be checked and potentially converted.
select_ini_file()
Purpose: Provides a GUI for selecting an .ini file.
Returns: Path of the selected .ini file.
get_user_input()
Purpose: Provides a GUI to select values for "Jpg Resize" and "Jpg Qfactor".
Returns: Tuple containing the selected values.
update_ini(file_path, resize_value, qfactor_value)
Purpose: Updates the .ini file with selected or predefined values.
Parameters:
file_path: Path of the .ini file to be updated.
resize_value: Value for "Jpg Resize".
qfactor_value: Value for "Jpg Qfactor".
Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change. Ensure to update tests as appropriate.
