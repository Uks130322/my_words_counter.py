import my_words_counter as counter
import sys
from pathlib import Path
print('PATH:', sys.path)

# counter.clean('files/spam1.txt')
# print(counter.word_counter('files/symbols.txt'))
# print(counter.words_occurrences('files/vokras.txt'))
print(counter.rare_words('files/vokras.txt'))
# print(counter.common_words('files/symb.txt'))
# print(counter.bytes_counter('files/spam.txt'))
# print(counter.bytes_counter('files/symbols.txt'))
#print(counter.bytes_counter('files/sym.txt'))
# path = Path('files/vok.txt')
# print(path.is_file())
