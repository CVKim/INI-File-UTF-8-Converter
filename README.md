
# INI File UTF-8 Converter

This Python utility converts the encoding of `.ini` files within a chosen directory to UTF-8, if they are not already in UTF-8.

## Table of Contents

- [Getting Started](#getting-started)
- [Usage](#usage)
- [Function Descriptions](#function-descriptions)

## Getting Started

To use this tool, simply run the Python script. A graphical user interface will appear, allowing you to select the desired directory.

## Usage

1. Execute the Python script.
2. When the pop-up window appears, navigate to and select the directory containing your `.ini` files.
3. The script will process each `.ini` file in the directory. If an `.ini` file is not in UTF-8 encoding, the script will convert it.

## Function Descriptions

### `change_encoding_to_utf8(filepath)`
- **Purpose**: Checks the encoding of a file and converts it to UTF-8 if it's not already.
- **Parameters**:
  - `filepath`: Path of the `.ini` file to be checked and potentially converted.

