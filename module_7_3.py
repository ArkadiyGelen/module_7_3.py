import string

class WordsFinder:
    def __init__(self, *file_name):
        self.file_name = file_name

    def get_all_words(self):
        check_lst = {}
        for file_name in self.file_name:
            with (open(file_name, 'r', encoding='utf-8') as book):
                words_content = book.read().lower()
                str_punk = str.maketrans(',', ',', string.punctuation + '-')
                words_content = words_content.translate(str_punk)
                words = words_content.split()
                check_lst[file_name] = words
                return check_lst

    def find(self, word):
           check_lst = self.get_all_words()
           lst = {}
           word = word.lower()
           for file_name, words in check_lst.items():
                   if word in words:
                       lst[file_name] = words.index(word)
                   return word, lst

    def count(self, word):
        check_lst = self.get_all_words()
        lst = {}
        word = word.lower()
        for file_name, words in check_lst.items():
            lst[file_name] = words.count(word)
            return lst

finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())
print(finder2.find('TEXT'))
print(finder2.count('teXT'))