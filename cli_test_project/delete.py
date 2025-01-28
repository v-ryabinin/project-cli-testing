import os
import shutil


def delete_file(path):
    print(f'test-delete-file {path}')

    if os.path.isfile(path):
        os.remove(path)
    elif os.path.isdir(path):
        shutil.rmtree(path)
    else:
        raise FileNotFoundError(f'Path {path} does not exist')
    print('file is removed')
