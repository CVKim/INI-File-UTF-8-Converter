# INI-File-UTF-8-Converter

INI File UTF-8 Converter
This project provides a Python script that converts the encoding of .ini files within a specified directory to UTF-8.

Overview
Upon execution, the script prompts the user to select a directory. It then detects and converts the encoding of all .ini files within that directory to UTF-8 if they are not already in that format.

Usage
Execute the Python script.
Use the pop-up window to select the directory containing the .ini files you wish to check and potentially convert.
The script will automatically convert the encoding of .ini files within the chosen directory to UTF-8.
Function Descriptions
change_encoding_to_utf8(filepath)
Arguments:
filepath: Path of the file for which the encoding needs to be checked and potentially converted.
