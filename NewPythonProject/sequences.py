#problem1 tupples
tu = (1, 2, [4, 5], 2, 'apple', 2)

print('--- Tupple elements: ---')
for item in tu:
    print(item)

# Тестване на методи за кортежи
apple_index = tu.index('apple')
count_twos = tu.count(2)

print(f"\nIndex of 'apple': {apple_index}") # Очакван резултат: 4
print(f"Count of twos: {count_twos}") # Очакван резултат: 3

# Опит за промяна на неизменяема последователност:
# tu[0] = 10  --> Грешка: TypeError: 'tuple' object does not support item assignment

#problem2 strings
print("\n--- String Manipulation ---")
text = "I'm using single quotes in Python"

print(f"Original string: {text}")
print(f"Lowercase letters: {text.lower()}")
print(f"Uppercase letters: {text.upper()}")

# Разделяне на думи по интервал
words_list = text.split()
print(f"List of words: {words_list}")
# Азбучно сортиране
words_list.sort()
print(f"Sorted words: {words_list}")

#problem3 slicing
print("\n--- List Slicing ---")
li = [10, 20, 30, 40, 50, 60, 70, 80]

print(f"Original list: {li}")
print(f"First 3 elements [:3]: {li[:3]}")       # [10, 20, 30]
print(f"Indices 2 to 5 [2:6]: {li[2:6]}")        # [30, 40, 50, 60]
print(f"Every second element [::2]: {li[::2]}")    # [10, 30, 50, 70]
print(f"In reverse order [::-1]: {li[::-1]}")         # [80, 70, 60, 50, 40, 30, 20, 10]
print(f"Without the last element [:-1]: {li[:-1]}")          # [10, 20, 30, 40, 50, 60, 70]

#problem4 list methods
print("\n--- List Methods ---")
li = [10, 20, 30, 40, 50, 60, 70, 80]

print(f"Original list: {li}")
print(f"First 3 elements [:3]: {li[:3]}")       # [10, 20, 30]
print(f"Indices 2 to 5 [2:6]: {li[2:6]}")        # [30, 40, 50, 60]
print(f"Every second element [::2]: {li[::2]}")    # [10, 30, 50, 70]
print(f"In reverse order [::-1]: {li[::-1]}")         # [80, 70, 60, 50, 40, 30, 20, 10]
print(f"Without the last element [:-1]: {li[:-1]}")          # [10, 20, 30, 40, 50, 60, 70]

#problem 5 combined works
print("\n--- Text Analysis ---")
text = input('Enter a sentence: ')

words = text.split()
total_words = len(words)

# Намиране на най-дългата дума
longest_word = ''
for word in words:
    if len(word) > len(longest_word):
        longest_word = word

# Обръщане на всяка дума чрез slicing [::-1]
reversed_words = [word[::-1] for word in words]
reversed_text = ' '.join(reversed_words)

# Проверка за наличие на 'python'
has_python = 'python' in text.lower()

print('\n=== RESULTS FROM ANALYSIS ===')
print(f"Total number of words: {total_words}")
print(f"Longest word: '{longest_word}' ({len(longest_word)} characters)")
print(f"Text with reversed words: {reversed_text}")
print(f"Contains 'Python': {'Yes' if has_python else 'No'}")