# Вывести последнюю букву в слове
word = 'Архангельск'
# ???
print(word[-1])

# Вывести количество букв "а" в слове
word = 'Архангельск'
# ???
print(word.lower().count('а'))


# Вывести количество гласных букв в слове
word = 'Архангельск'
# ???
vowels = ['а', 'е', 'ё', 'и', 'о', 'у', 'э', 'ю', 'я']
count = 0

for letter in word.lower():
    if letter in vowels:
        count += 1
    
print(count)

# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
# ???
print(len(sentence.split()))

# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
# ???
for word in sentence.split():
    print(word[0])


# Вывести усреднённую длину слова в предложении
sentence = 'Мы приехали в гости'
# ???
list_words = sentence.split()
summ_words = 0

for word in list_words:
    summ_words += len(word)
    
print(summ_words / len(list_words))