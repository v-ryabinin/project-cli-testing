import argparse

from cli_test_project.copy import copy_file
from cli_test_project.count_files import count_files
from cli_test_project.delete import delete_file

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--command', choices=['copy', 'delete', 'count'], help='my_command')
    parser.add_argument('--path', type=str, required=False, help='path to file')
    parser.add_argument('--source', type=str, required=False, help='source')
    parser.add_argument('--dst', type=str, required=False, help='destination')

    args = parser.parse_args()
    if args.command == 'copy':
        copy_file(args.source, args.dst)

    if args.command == 'delete':
        delete_file(args.path)

    if args.command == 'count':
        count = count_files(args.path)
        print('total files:', count)
