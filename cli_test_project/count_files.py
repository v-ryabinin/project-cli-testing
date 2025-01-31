import os


def count_files(folder):
    items = os.listdir(folder)
    count = 0
    for item in items:
        if os.path.isfile(os.path.join(folder, item)):
            count += 1
        else:
            count += count_files(os.path.join(folder, item))
    return count
