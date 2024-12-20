import streamlit as st
import pandas as pd


st.title("Про мене")
st.subheader('Рубрика *Не вигадані факти.*')

st.write("Я Eliangangs. Виросла в звичайному містечку в Садгорі, навчалась в ліцеї НВК 'Берегиня', закінчила з відзнакою та згодом в 2004 році літала в Флориду. Була генеральним директором Ілона Маска та є простою людиною.")
st.write("Мій гітхабик з стеком сайтиків: https://github.com/Eliangangs :)")
data = pd.DataFrame({
    'Year': ['1984', '1994', '2004', '2014', '2024'],
    'Earnings': [100, 110, 4020, 65000, 70000]
})

data.set_index('Year', inplace=True)

# Побудова гістограми
st.write('Моя невеличка зарплата за останні за 50 років')
st.bar_chart(data)