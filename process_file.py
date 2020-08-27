import re
import os


def file_is_empty(path):
    """Validate if a file is empty or not
    Args:
        path (string): path to file

    Returns:
        [True]: return True if file is empty
        [False]: return False if file is empty
    """    
    return os.stat(path).st_size == 0

def main():
    try:
        list_words = read_file('word_file.txt')
        largest_word = find_the_largest_word(list_words)
        transposed_word= transpose_a_word(largest_word)
        print("the largest word:", largest_word)
        print("transposed_word:", transposed_word)
    except Exception as e:
        print(e)

def read_file(file_name):
    """Read a specific file  

    Args:
        file_name (string): path to file

    Returns:
        list: list containing  all items read
    """    
    list_words = []
    if not file_is_empty(file_name):
        try:
            file = open(file_name)
            for word in file:
                word_transformed = re.sub("[^a-zA-Z]",r'',word.strip('\n'))
                list_words.append(word_transformed)
            list_words = list(filter(None, list_words))  
        finally:
            file.close()
            return list_words
    else:
        print("File is empty")

def find_the_largest_word(list_strings):
    """Find the largest word in a list

    Args:
        list_strings (list): string list

    Returns:
        string: the largest word found
    """    
    sortedword = sorted(list_strings,key=len)
    return sortedword[-1]

def transpose_a_word(word):
    """transpose a word

    Args:
        word (string): string to transpose


    Returns:
        string: transpose string
    """    
    list_letters = list(word)
    transpose_letters = list_letters[::-1]
    transposed_word = ''.join(transpose_letters)
    return transposed_word

if __name__ == "__main__":
    main()
