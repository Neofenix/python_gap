import unittest
from  process_file import read_file, find_the_largest_word, transpose_a_word, file_is_empty


class Test(unittest.TestCase):

    def test_read_file_sucessfully(self):
        self.assertEqual(read_file('data_tests/successful_file.txt'), ['a', 'ab', 'abc', 'abcd', 'abcde'],'List is not equal')

    def test_read_empty_file(self):
        self.assertIsNone(read_file('data_tests/empty_file.txt'))
    
    def test_read_file_with_characters(self):
        self.assertEqual(read_file('data_tests/characters_file.txt'), ['a', 'ab'],'Lists is not equal')

    def test_read_file_with_spaces(self):
        self.assertEqual(read_file('data_tests/file_with_spaces.txt'), ['a', 'ab','abcd', 'efgh','ijklmn'],'Lists is not equal')

    def test_find_the_largest_word_sucessfully(self):
        self.assertEqual(find_the_largest_word(['efzadf', 'ab', 'efhji']),'efzadf')

    def test_transpose_a_word_sucessfully(self):
        self.assertEqual(transpose_a_word('ewzadf'),'fdazwe')

    def test_should_file_is_empty_return_true(self):
        self.assertTrue(file_is_empty('data_tests/empty_file.txt'))
    
    def test_should_file_is_empty_return_false(self):
        self.assertFalse(file_is_empty('data_tests/file_with_spaces.txt'))

if __name__ == '__main__':
    unittest.main()