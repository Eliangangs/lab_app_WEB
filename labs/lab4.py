import streamlit as st
from collections import Counter
import re

def find_repeated_sequences(text, min_words=3, min_repeats=5):
    # Очистка тексту: видалення розділових знаків і нормалізація регістру
    text = re.sub(r'[^\w\s]', '', text).lower()
    words = text.split()
    n = len(words)

    # Словник для збереження частот повторюваних послідовностей
    sequence_counts = Counter()

    # Генерація послідовностей і підрахунок повторів
    for length in range(min_words, n + 1):  # Довжини послідовностей від min_words до max
        for i in range(n - length + 1):  # Початковий індекс
            sequence = ' '.join(words[i:i + length])
            sequence_counts[sequence] += 1

    # Фільтрування послідовностей, які повторюються не менше min_repeats разів
    repeated_sequences = {seq: count for seq, count in sequence_counts.items() if count >= min_repeats}

    return repeated_sequences

def run_lab():
    st.title("Лабораторна робота 4")
    text = st.text_area("Введіть текст для аналізу:", key="text_lab4")
    min_words = st.number_input("Введіть мінімальну кількість слів у послідовності:", min_value=1, value=3, step=1, key="min_words_lab4")
    min_repeats = st.number_input("Введіть мінімальну кількість повторів послідовності:", min_value=1, value=5, step=1, key="min_repeats_lab4")

    if st.button("Знайти повторювані послідовності", key="find_sequences_lab4"):
        if text:
            result = find_repeated_sequences(text, min_words, min_repeats)
            if result:
                st.write("Найдені послідовності:")
                for seq, count in result.items():
                    st.write(f"\"{seq}\" повторюється {count} разів")
            else:
                st.write("Повторюваних послідовностей не знайдено.")
        else:
            st.error("Введіть будь-який текст")
