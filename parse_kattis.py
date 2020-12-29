from bs4 import BeautifulSoup as bs
import tkinter as tk
import requests
import re

def parse_kattis(url):
    data = requests.get(url)
    soup = bs(data.content, 'lxml')
    title = soup.find('h1')
    side_bar = soup.find(class_='sidebar-info')
    side_bar = side_bar.find_all('p')
    problem_id = side_bar[0].text
    problem_id = problem_id.split(" ")[3]
    difficulty = side_bar[3].text
    difficulty = float(difficulty.split(" ")[2])

    return[problem_id, str(title.text), difficulty]