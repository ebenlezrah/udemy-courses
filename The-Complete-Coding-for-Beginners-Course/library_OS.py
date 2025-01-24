# os.mkdir - Create a directory named path with the specified numeric mode.
import os
# os.mkdir("new_folder")
# this created a new folder (in the current directory)
# os.path - a module inside the os module
# os.path.exists - Return True if path refers to an existing path or an open file descriptor.
if os.path.exists("test.txt"):
    print("The file exists")
else:
    print("The file does not exist")