import streamlit as st
import requests
from bs4 import BeautifulSoup
import re
from collections import Counter
from urllib.parse import urlparse

def get_page_content(url):
    """Завантажує HTML-код сторінки за допомогою requests."""
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Check for HTTP errors
        return response.text
    except requests.exceptions.RequestException as e:
        st.error(f"Не вдалося завантажити сторінку: {url}. Помилка: {e}")
        return None


def count_words(text):
    """Підраховує частоту появи слів у тексті."""
    words = re.findall(r'\b\w+\b', text.lower())
    word_counts = Counter(words)
    return word_counts

def count_html_tags(soup):
    """Підраховує частоту появи HTML-тегів."""
    tags = [tag.name for tag in soup.find_all(True)]
    tag_counts = Counter(tags)
    return tag_counts

def count_links_and_images(soup):
    """Підраховує кількість посилань (тег <a>) і зображень (тег <img>)."""
    links = soup.find_all('a')
    images = soup.find_all('img')
    return len(links), len(images)

def analyze_news_page(url):
    """Аналізує новинну сторінку: підраховує слова, теги, посилання та зображення."""
    html_content = get_page_content(url)
    if html_content is None:
        return
    
    soup = BeautifulSoup(html_content, 'html.parser')
    
    text_content = soup.get_text()
    word_counts = count_words(text_content)
    
    tag_counts = count_html_tags(soup)
    
    link_count, image_count = count_links_and_images(soup)
    
    st.write(f"Частота появи слів на сторінці '{url}':")
    for word, count in word_counts.most_common(10):
        st.write(f"{word}: {count}")
    
    st.write("\nЧастота використання HTML-тегів:")
    for tag, count in tag_counts.most_common(10):
      st.write(f"{tag}: {count}")

    st.write(f"\nКількість посилань: {link_count}")
    st.write(f"Кількість зображень: {image_count}")

def run_lab():
    st.title("Лабораторна робота 6")
    url = st.text_input("Введіть URL для аналізу:", "https://uk.wikipedia.org/wiki/Головна_сторінка", key="url_lab6")
    if st.button("Аналізувати сторінку", key="analyze_button_lab6"):
        if url:
            analyze_news_page(url)