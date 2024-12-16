import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
import re


def task_1():
    st.subheader("Завдання 1")
    x = np.linspace(-3, 3, 400)
    y = 2**x * np.sin(10*x)
    
    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.set_title('Графік Y(x) = 2^x * sin(10x)')
    ax.set_xlabel('x')
    ax.set_ylabel('Y(x)')
    ax.grid()

    st.pyplot(fig)


def task_2():
    st.subheader("Завдання 2")
    text = st.text_area("Введіть текст для аналізу літер:", "Ваш текст тут.", key="text_task2_lab7")
    if st.button("Побудувати гістограму літер", key="hist_letters_button_lab7"):
        if text:
            letter_count = Counter(char.lower() for char in text if char.isalpha())
            letters = list(letter_count.keys())
            frequencies = list(letter_count.values())

            fig, ax = plt.subplots()
            ax.bar(letters, frequencies)
            ax.set_title('Гістограма частоти літер')
            ax.set_xlabel('Літери')
            ax.set_ylabel('Частота')
            ax.grid()
            st.pyplot(fig)


def task_3():
    st.subheader("Завдання 3")
    text = st.text_area("Введіть текст для аналізу речень:", "Ваш текст тут. Яка погода? Це чудово! І ти...", key="text_task3_lab7")
    if st.button("Побудувати гістограму речень", key="hist_sentences_button_lab7"):
       if text:
            regular = re.findall(r'[^.!?]*[.!?]', text)
            counts = {
                'Звичайні': sum(1 for s in regular if not s.strip().endswith(('?', '!', '...'))),
                'Питальні': sum(1 for s in regular if s.strip().endswith('?')),
                'Окличні': sum(1 for s in regular if s.strip().endswith('!')),
            }

            fig, ax = plt.subplots()
            ax.bar(counts.keys(), counts.values())
            ax.set_title('Гістограма частоти речень')
            ax.set_xlabel('Типи речень')
            ax.set_ylabel('Кількість')
            ax.grid()

            st.pyplot(fig)


def run_lab():
    st.title("Лабораторна робота 7")
    task_1()
    st.markdown("---")
    task_2()
    st.markdown("---")
    task_3()