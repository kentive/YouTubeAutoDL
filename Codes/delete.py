import os
import glob

def all_delete():
    for file in glob.glob('../Videos/*'):
        os.remove(file)

if __name__ == '__main__':
    all_delete()