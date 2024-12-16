import streamlit as st
from labs import lab1, lab2, lab3, lab4, lab5, lab6, lab7

st.set_page_config(
    page_title="Лабораторні роботи Python",
    page_icon="🎓",
    layout="wide"
)

def display_labs():
    labs = {
        "Лабораторна робота 1": {
            "module": lab1,
            "readme": "labs/lab1_README.md"
        },
        "Лабораторна робота 2": {
            "module": lab2,
            "readme": "labs/lab2_README.md"
        },
         "Лабораторна робота 3": {
            "module": lab3,
            "readme": "labs/lab3_README.md"
        },
         "Лабораторна робота 4": {
            "module": lab4,
            "readme": "labs/lab4_README.md"
        },
        "Лабораторна робота 5": {
            "module": lab5,
            "readme": "labs/lab5_README.md"
        },
        "Лабораторна робота 6": {
            "module": lab6,
            "readme": "labs/lab6_README.md"
        },
          "Лабораторна робота 7": {
            "module": lab7,
            "readme": "labs/lab7_README.md"
        }
    }
    
    for lab_name, lab_info in labs.items():
        with st.expander(lab_name):
            with open(lab_info["readme"], "r", encoding="utf-8") as f:
                st.markdown(f.read())
            if st.button("Розпочати", key=lab_name):
                st.session_state['current_lab'] = lab_name
                
            if 'current_lab' in st.session_state and st.session_state['current_lab'] == lab_name:
                lab_info["module"].run_lab()

display_labs()
