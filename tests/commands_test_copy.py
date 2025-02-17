import os
import shutil
import unittest
from cli_test_project.copy import copy_file


class TestFileOperations(unittest.TestCase):
    root_path = 'c:/test_dir'

    def setUp(self):
        if os.path.exists(self.root_path):
            shutil.rmtree(self.root_path)
        os.makedirs(self.root_path)
        open(os.path.join(self.root_path, 'test_file1.txt'), 'wt+').write('This is a test text.')

    def tearDown(self):
        if os.path.exists(self.root_path):
            shutil.rmtree(self.root_path)

    def test_copy(self):
        copy_file(os.path.join(self.root_path, 'test_file1.txt'), os.path.join(self.root_path,'test_new.txt'))

        self.assertTrue(os.path.exists(os.path.join(self.root_path,'test_new.txt')))


if __name__ == '__main__':
    unittest.main()
