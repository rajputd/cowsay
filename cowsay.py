#!/usr/bin/env python3
import sys

borderpadding = 2
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
    for line in cow:
        print(line)

def drawTextBox(lines):
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
    lines = []
    for line in sys.stdin:
        lines.append(line.strip())
    return lines

def getMaxLineLength(lines):
    maxLength = 0
    for line in lines:
        length = len(line)
        if length > maxLength:
            maxLength = length
    return maxLength

def padLine(line, maxlinelength):
    paddingLength = maxlinelength - len(line) - borderpadding
    padding = ""
    if paddingLength > 0:
        padding = " " * paddingLength
    return line + padding

if __name__ == "__main__":
    main()


