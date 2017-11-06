# open file and counts how many chars there are and how many words
CharCount = WordCount = LineCount = 0


with open('test-file.txt', 'r') as f:
    for line in f:
        LineCount += 1
        WordCount += len(line.split())
        CharCount += len(line)

with open('results.txt', 'w') as file:
    file.write('Line count = ' + format(LineCount) + '\n')
    file.write('Word count = ' + format(WordCount) + '\n')
    file.write('Char count = ' + format(CharCount) + '\n')
