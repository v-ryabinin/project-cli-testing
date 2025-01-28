import os
import shutil


def copy_file(source, dst):
    if not os.path.exists(source):
        raise FileNotFoundError(f'Source file {source} does not exists')
    shutil.copy(source, dst)
    print(f'copy file:{source} to {dst}')
