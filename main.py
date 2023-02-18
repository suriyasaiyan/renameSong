import os
from pathlib import Path
import random
def main():

    sou= Path()/""
    for filename in os.listdir(sou):
        if '-' in filename:
            f= filename.split('-')[1]
            if f in os.listdir(sou):
                os.rename(os.path.join(sou, filename), os.path.join(sou,f"{f}_{random.randint(1,9)}"))
            else:
                os.rename(os.path.join(sou, filename), os.path.join(sou, f))

        elif ']' in filename:
            f= filename.split(']')[1]
            if f in os.listdir(sou):
                os.rename(os.path.join(sou, filename), os.path.join(sou,f"{f}_{random.randint(1,9)}"))
            else:
                os.rename(os.path.join(sou, filename), os.path.join(sou, f))
        
        else: 
            continue


if __name__ == '__main__':
    main()
    