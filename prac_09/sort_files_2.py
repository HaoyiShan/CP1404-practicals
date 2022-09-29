import shutil
import os


def main():
    os.chdir('FilesToSort')
    suf = []
    Dir = {}
    for directory_name, subdirectories, filenames in os.walk('.'):
        print(filenames)
        for filename in filenames:
            suffix = filename.split('.')[1]
            if suffix not in suf:
                suf.append(suffix)
        print(suf)
        for i in suf:
            category = input("What category would you like to sort " + i + " files into?")
            Dir[i] = category
        for i in Dir:
            try:
                os.mkdir(Dir[i])
            except FileExistsError:
                pass
            for filename in filenames:
                suffix = filename.split('.')[1]
                if suffix == i:
                    try:
                        shutil.move(filename, Dir[i])
                    except shutil.Error:
                        pass


main()
