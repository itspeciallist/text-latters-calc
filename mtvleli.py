from collections import Counter
import re

# გახსენით ფაილი და წაიკითხეთ მისი შინაარსი
with open('list.txt', 'r', encoding='utf-8') as file:
    content = file.read()

# შინაარსის სიტყვებად დაყოფა (არაიანბანური სიმბოლოების მოშორება)
words = re.findall(r'\b\w+\b', content)

# სიტყვების რაოდენობის დათვლა
word_count = len(words)

# ყველაზე დიდი სიგრძის სიტყვის პოვნა
max_word = max(words, key=len)
max_length = len(max_word)

# ყველაზე ხშირად გამეორებული ასოს პოვნა ყველაზე დიდ სიტყვაში
letter_counts = Counter(max_word)
most_repeated_letter, count = letter_counts.most_common(1)[0]

# ყველა ასოს რაოდენობის დათვლა (მხოლოდ ანბანური სიმბოლოები)
all_letter_counts = Counter(re.sub(r'[^a-zA-Zა-ჰ]', '', content))

# შედეგების გამოჩენა
print(f"სიტყვების რაოდენობა: {word_count}")
print(f"ყველაზე დიდი სიგრძის სიტყვა: {max_word}")
print(f"ამ სიტყვაში ასოები: {max_length}")
print(f"ყველაზე ხშირად გამეორებული ასო: {most_repeated_letter}")
print(f"რამდენჯერ გაიმეორა: {count}")
print("\nყველა ასოს რაოდენობა (დალაგებული):")
for letter, count in sorted(all_letter_counts.items(), key=lambda x: x[1], reverse=True):
    print(f"ასო: {letter}, რაოდენობა: {count}")
