#!/usr/bin/python3
"""Defines a file-appending function."""


    """Appends a string to the end of a UTF8 text file.
    Args:
        filename (str): The name of the file to append to.
        text (str): The string to append to the file.
    Returns:
        The number of characters appended.
    """
   def append_to_file(file_path: str, content: str) -> int:
    try:
        with open(file_path, "a") as file:
            file.write(content)
            return len(content)
    except:
        print("An error occurred while appending to file.")
        return 0
