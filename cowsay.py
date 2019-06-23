#!/usr/bin/env python3
import sys

#padding around speech bubble text
borderpadding = 2

#cow ascii art
cow = [
    "          \\  ^__^",
    "           \\ (oo)\\________",
    "             (__)\\        )\\/\\",
    "                  ||----W |",
    "                  ||     ||"
]

def main():
    lines = getLines()
    drawTextBox(lines)
    drawAnimal()

def drawAnimal():
    """Draws a cow in the terminal with ascii art"""
    for line in cow:
        print(line)

def drawTextBox(lines):
    """draws a textbox using the ascii art into the terminal. The textbox
       will contain the lines passed into this function.

    Parameters:
        lines (array of strings) : the text that will be inside the textbox

    Returns:
        None
    """
    maxlinelength = getMaxLineLength(lines) + borderpadding
    horizontal_border = " " + ('-' * maxlinelength)
    print(horizontal_border)

    if len(lines) == 1:
        print("< " + padLine(lines[0], maxlinelength) + " >")
    else:
        print("/ " + (" " * (maxlinelength - borderpadding)) + " \\")
        for line in lines:
            print("| " + padLine(line, maxlinelength) + " |")
        print("\\ " + (" " * (maxlinelength - borderpadding)) + " /")

    print(horizontal_border)

def getLines():
    """return lines in stdin as an array of strings with whitespace stripped.

    Parameters: None.

    Returns:
        (array of strings) : lines of text sent to stdin
    """

    lines = []
    for line in sys.stdin:
        lines.append(line.strip())
    return lines

def getMaxLineLength(lines):
    """Return the length of the longest line of text in the array of lines

    Parameters:
        lines (array of strings) : the array that contains the lines that will
                                    be searched.

    Returns:
        (int) : length of the longest string in the array
    """

    maxLength = 0
    for line in lines:
        length = len(line)
        if length > maxLength:
            maxLength = length
    return maxLength

def padLine(line, maxlinelength):
    """Add whitespace to the end of the given line so it's length equals maxlinelength

    Parameters:
        line (string) : the line that will have whitespace added to it.
        maxlinelnegth (int) : the target length of the line after it has
                              been padded.

    Returns:
        (string) : the line parameter padded with whitespace at the end.
    """

    paddingLength = maxlinelength - len(line) - borderpadding
    padding = ""
    if paddingLength > 0:
        padding = " " * paddingLength
    return line + padding

if __name__ == "__main__":
    main()


