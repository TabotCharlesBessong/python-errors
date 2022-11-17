
error = FileNotFoundError: [Errno 2] No such file or directory: './file.txt'
problem = {file : open("file.txt")}
solution = {file : open(r"day24\files\file.txt")}
solution2 = {file: open(r"H:\MERNSTACK2\100-days-of-code\day24\files\file.txt") }
# explanation
# Open the file using either the relative or absolute path and add an r in front of it
