import os
def delete_file (path):
    print('test-delete-file')

    if os.path.isfile(path):
        os.remove(path)
    else:
        pass