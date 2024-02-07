#!/usr/bin/env python3

import turtle as t
import os

def list_directory_tree(directory):
    for root, dirs, files in os.walk(directory):
        level = root.replace(directory, '').count(os.sep)
        indent = ' ' * 4 * (level)
        print(f"{indent}{os.path.basename(root)}/")
        subindent = ' ' * 4 * (level + 1)
        for file in files:
            print(f"{subindent}{file}")

if __name__ == "__main__":
    starting_directory = "/"
    list_directory_tree(starting_directory)

#     t.mainloop()

# NO LENGTH OPTIMIZATION #
