import streamlit as st

def find_subsequence(lst, subseq):
    n = len(lst)
    m = len(subseq)

    for i in range(n - m + 1):
        if lst[i:i+m] == subseq:
            return True

    return False

def run_lab():
    st.title("Лабораторна робота 2")
    lst_str = st.text_input("Введіть елементи списку через пробіл, наприклад: 1 2 3 4 5 6 7 8 9", "1 2 3 4 5 6 7 8 9", key="lst_str_lab2")
    subseq_str = st.text_input("Введіть елементи підпослідовності через пробіл, наприклад: 4 5 6", "4 5 6", key="subseq_str_lab2")
    if st.button("Перевірити", key="check_button_lab2"):
        try:
            lst = list(map(int, lst_str.split()))
            subseq = list(map(int, subseq_str.split()))
            if find_subsequence(lst, subseq):
                st.success("Послідовність знайдена!")
            else:
                st.error("Послідовність не знайдена.")
        except ValueError:
                st.error("Будь ласка, введіть тільки цілі числа.")