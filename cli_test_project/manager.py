import argparse

from cli_test_project.copy import copy_file

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--command', choices= ['copy'], help='my_command')

    args = parser.parse_args()
    if   args.command == 'copy':
        copy_file('','')

