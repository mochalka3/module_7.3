class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names
    def get_all_words(self):
        all_words = {}
        words = ""
        punctuation = [',', '.', '=', '!', '?', ';', ':', ' - ']
        for file_name in self.file_names:
            with open(file_name, 'r', encoding='utf-8') as file:
                for line in file:
                    for punkt in punctuation:
                        line = line.replace(punkt, " ")
                    words += " " + line
                words = words.split()
                all_words[file_name] = words
        return all_words
    def find(self, word):
        result = {}
        for name, words in self.get_all_words().items():
            index = 1
            for w in words:
                if w.lower() == word.lower():
                    result[name] = index
                    break
                index += 1
        return result
    def count(self, word):
        counters = {}
        for value, key in self.get_all_words().items():
            words_count = key.count(word.lower())
            counters[value] = words_count
        return counters
finder2 = WordsFinder('test_file_7_3.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего
