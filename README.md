# INI File Utilities

This repository contains Python utilities for handling `.ini` files. These utilities provide functionalities such as encoding conversion, GUI-based value selection, and value updates.

## Table of Contents

- [INI File UTF-8 Converter (A Code)](#ini-file-utf-8-converter-a-code)
- [INI File Value Selector (B Code)](#ini-file-value-selector-b-code)
- [INI File Updater (C Code)](#ini-file-updater-c-code)
- [Usage](#usage)

## INI File UTF-8 Converter (A Code)

This Python utility (A Code) converts the encoding of `.ini` files within a chosen directory to UTF-8, if they are not already in UTF-8.

### Usage for A Code:

1. Execute the Python script.
2. When the pop-up window appears, navigate to and select the directory containing your `.ini` files.
3. The script will process each `.ini` file in the directory. If an `.ini` file is not in UTF-8 encoding, the script will convert it.

### Function Descriptions for A Code:

#### `change_encoding_to_utf8(filepath)`
- **Purpose**: Checks the encoding of a file and converts it to UTF-8 if it's not already.
- **Parameters**: `filepath` - Path of the `.ini` file to be checked and potentially converted.

## INI File Value Selector (B Code)

B Code provides a GUI for the user to select certain values, which can then be written to an `.ini` file.

### Usage for B Code:

1. Execute the Python script.
2. Use the pop-up GUI to select the desired `.ini` file.
3. Use the subsequent GUI to select values for 'Jpg Resize' and 'Jpg Qfactor'.
4. The selected values will be written to the `.ini` file under relevant sections.

## INI File Updater (C Code)

The C Code allows the user to automatically set specific values (`Jpg Resize` and `Jpg Qfactor`) in an `.ini` file.

### Usage for C Code:

1. Execute the Python script.
2. Use the pop-up GUI to select the desired `.ini` file.
3. The script will automatically update the `.ini` file with preset values for 'Jpg Resize' and 'Jpg Qfactor'.

### Note:

Remember to backup your `.ini` files before making any changes, to prevent accidental data loss.

