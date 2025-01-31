import os
import tempfile
import unittest

from cli_test_project.count_files import count_files


class TestFileOperations(unittest.TestCase):
    def setUp(self):
        self.test_dir = tempfile.TemporaryDirectory()

    def tearDown(self):
        self.test_dir.cleanup()

    def test_created_files(self):
        file_path_1 = os.path.join(self.test_dir.name, 'file1.txt')
        with open(file_path_1, 'w') as f:
            f.write('This is a test file.')

        file_path_2 = os.path.join(self.test_dir.name, 'file2.txt')
        with open(file_path_2, 'w') as f:
            f.write('This is a test file2.')

        # run command count
        count = count_files(self.test_dir.name)
        self.assertEqual(count, 2)
