import streamlit as st
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Функція для відправлення листа
def send_email(sender_name, sender_email, message_content):
    # Налаштування сервера та пошти
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    sender_address = "anileti3069@gmail.com"
    sender_password = "raadujizgrmilrog"

    # Формування листа
    msg = MIMEMultipart()
    msg["From"] = sender_address
    msg["To"] = sender_address  # Лист надсилається на твій же email
    msg["Subject"] = "Новий зворотній зв'язок"

    # Тіло листа
    body = f"""
    Ви отримали нове повідомлення з форми зворотного зв'язку:
    
    Ім'я: {sender_name}
    Email: {sender_email}
    Повідомлення: {message_content}
    """
    msg.attach(MIMEText(body, "plain"))

    try:
        # З'єднання з сервером та надсилання
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Шифрування з'єднання
            server.login(sender_address, sender_password)
            server.send_message(msg)
        return True, None  # Повертаємо успіх і відсутність помилки
    except Exception as e:
        return False, str(e)  # У разі помилки повертаємо її опис

# Створення форми
st.title("Форма для зворотного зв'язку з надсиланням на пошту")

with st.form("feedback_form"):
    name = st.text_input("Ім'я", placeholder="Ваше ім'я")
    email = st.text_input("Електронна пошта", placeholder="example@email.com")
    message = st.text_area("Повідомлення", placeholder="Ваше повідомлення...")
    submit_button = st.form_submit_button("Відправити")

if submit_button:
    if not name or not email or not message:
        st.error("Будь ласка, заповніть усі поля форми.")
    else:
        # Виклик функції для надсилання листа
        success, error_message = send_email(name, email, message)
        if success:
            st.success("Ваше повідомлення успішно надіслано! Дякуємо за ваш зворотній зв'язок.")
        else:
            st.error(f"Виникла помилка при надсиланні повідомлення: {error_message}")
