import shutil
import os


def main():
    os.chdir('FilesToSort')
    for directory_name, subdirectories, filenames in os.walk('.'):
        print(filenames)
        for filename in filenames:
            suffix = filename.split('.')[1]
            try:
                os.mkdir(suffix)
            except FileExistsError:
                pass
            try:
                shutil.move(filename, suffix)
            except shutil.Error:
                pass


main()
