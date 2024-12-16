import streamlit as st

class MyString(str):
    def has_repeated_sequences(self):
        for i in range(len(self) - 2):
            substring = self[i:i + 3]
            if self.count(substring) > 1:
                return True
        return False

    def is_palindrome(self):
        normalized_str = self.lower()
        return normalized_str == normalized_str[::-1]

def run_lab():
    st.title("Лабораторна робота 5")
    input_string = st.text_input("Введіть рядок:", "AbaCba", key="input_string_lab5")
    
    if st.button("Перевірити", key="check_button_lab5"):
      s = MyString(input_string)
      st.write(f"Рядок '{input_string}' є паліндромом: {s.is_palindrome()}")
      st.write(f"Рядок '{input_string}' має повторювані послідовності: {s.has_repeated_sequences()}")