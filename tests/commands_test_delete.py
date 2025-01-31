import os
import shutil
import unittest

from cli_test_project.delete import delete_file


class TestFileOperations(unittest.TestCase):
    def setUp(self):
        self.test_dir = 'test_dir'
        os.makedirs(self.test_dir, exist_ok=True)

 # Create a test file

        self.test_file = os.path.join(self.test_dir, 'test_file.txt')
        with open(self.test_file, 'wt+') as f:
            f.write('This is a test file.')

    def tearDown(self):
        if os.path.exists(self.test_dir):
            shutil.rmtree(self.test_dir)

    def test_delete_file(self):
# Make sure the file exists before deleting
        self.assertTrue(os.path.exists(self.test_file))

        # run command delete

        delete_file (self.test_file)

# check for file deleted
        self.assertFalse(os.path.exists(self.test_file))