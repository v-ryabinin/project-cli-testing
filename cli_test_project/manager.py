import argparse

from cli_test_project.copy import copy_file
from cli_test_project.count_files import count_files
from cli_test_project.delete import delete_file

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--command', choices= ['copy', 'delete','count'], help='my_command')
    parser.add_argument('--path', type = str, required=True, help='path to file')

    args = parser.parse_args()
    if   args.command == 'copy':
        copy_file('','')

    if args.command == 'delete':
        delete_file(args.path)

    if args.command == 'count':
        count=count_files(args.path)
        print(count)