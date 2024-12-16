import streamlit as st
import os
import shutil


def create_file(group_name, students_data):
    filename = f"group_{group_name}.txt"
    with open(filename, "w", encoding="utf-8") as file:
        for student, score in students_data.items():
            file.write(f"{student},{score}\n")
    return filename


def read_file(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            return [line.strip().split(",") for line in file]
    except FileNotFoundError:
        return []

def append_file(filename, student, score):
    with open(filename, "a", encoding="utf-8") as file:
         file.write(f"{student},{score}\n")
         

def find_files(directory, pattern):
    files = []
    for filename in os.listdir(directory):
        if filename.startswith(pattern) and filename.endswith(".txt"):
           files.append(os.path.join(directory, filename))
    return files

def find_data_in_file(filename, search_term):
    results = []
    for line in read_file(filename):
        if any(search_term in item for item in line):
            results.append(line)
    return results


def sort_by_score(filename):
    students = read_file(filename)
    students_with_scores = []
    for student, score in students:
      try:
        students_with_scores.append((student, float(score)))
      except ValueError:
        continue
    sorted_students = sorted(students_with_scores, key=lambda item: item[1], reverse=True)
    return sorted_students


def run_lab():
    st.title("Лабораторна робота 3")
    
    st.header("Створення файлу")
    group_name = st.text_input("Введіть назву групи:", "1", key="group_name_lab3")
    students_data_input = st.text_area("Введіть дані студентів у форматі 'Ім'я,Середній бал', кожен студент з нового рядка:", key="students_data_lab3")
    
    if st.button("Створити файл", key="create_file_button_lab3"):
        students_data = {}
        for line in students_data_input.split("\n"):
            if line:
                try:
                  name, score = line.split(",")
                  students_data[name.strip()] = float(score.strip())
                except ValueError:
                  st.error("Невірний формат введення даних")
                  return
        if students_data:
             filename = create_file(group_name, students_data)
             st.success(f"Файл {filename} успішно створено.")


    st.header("Зчитування файлу")
    filename_read = st.text_input("Введіть назву файлу для читання:", "group_1.txt", key="filename_read_lab3")
    if st.button("Зчитати файл", key="read_file_button_lab3"):
        if filename_read:
           data = read_file(filename_read)
           if data:
             st.write("Дані з файлу:")
             for line in data:
                st.write(f"Ім'я: {line[0]}, Середній бал: {line[1]}")
           else:
              st.error("Файл не знайдено або порожній.")

    st.header("Дозапис у файл")
    filename_append = st.text_input("Введіть назву файлу для дозапису:", "group_1.txt", key="filename_append_lab3")
    student_append = st.text_input("Введіть ім'я студента для дозапису:", key="student_append_lab3")
    score_append = st.text_input("Введіть середній бал студента для дозапису:", key="score_append_lab3")
    if st.button("Дозаписати файл", key="append_file_button_lab3"):
        if filename_append and student_append and score_append:
            try:
                append_file(filename_append, student_append, float(score_append))
                st.success("Дані успішно дозаписано у файл.")
            except ValueError:
                st.error("Невірний формат середнього балу")


    st.header("Пошук файлів у каталозі")
    directory = "."
    pattern = st.text_input("Введіть початковий префікс для пошуку файлів:", "group_", key="pattern_search_lab3")
    if st.button("Пошук файлів", key="find_files_button_lab3"):
        files = find_files(directory, pattern)
        if files:
            st.write("Знайдені файли:")
            for file in files:
                st.write(file)
        else:
            st.error("Файлів не знайдено.")
    
    st.header("Пошук даних у файлі")
    filename_search = st.text_input("Введіть назву файлу для пошуку даних:", "group_1.txt", key="filename_search_lab3")
    search_term = st.text_input("Введіть термін для пошуку:", key="search_term_lab3")
    if st.button("Пошук даних", key="find_data_button_lab3"):
        if filename_search and search_term:
            results = find_data_in_file(filename_search, search_term)
            if results:
              st.write("Результати пошуку:")
              for line in results:
                st.write(f"Ім'я: {line[0]}, Середній бал: {line[1]}")
            else:
               st.error("Дані не знайдено.")


    st.header("Сортування даних у файлі за середнім балом")
    filename_sort = st.text_input("Введіть назву файлу для сортування:", "group_1.txt", key="filename_sort_lab3")
    if st.button("Сортувати", key="sort_file_button_lab3"):
        if filename_sort:
            sorted_data = sort_by_score(filename_sort)
            if sorted_data:
              st.write("Відсортовані дані:")
              for student, score in sorted_data:
                st.write(f"Ім'я: {student}, Середній бал: {score}")
            else:
                st.error("Файл не знайдено або не має коректних даних.")