import requests
from bs4 import BeautifulSoup
from tabulate import tabulate
import os
import numpy as np
import matplotlib.pyplot as plt
from flask import Flask


def extract_contents(row): return [x.text.replace('\n', '') for x in row]


def get_stats():
    URL = 'https://www.mohfw.gov.in/'

    SHORT_HEADERS = ['Sl. No.', 'State', 'Indian-Confirmed',
                     'Foreign-Confirmed', 'Cured', 'Death']

    response = requests.get(URL).content
    soup = BeautifulSoup(response, 'html.parser')

    stats = []
    cases = soup.find(id='cases')
    all_table_rows = cases.find_all('tr')
    all_table_rows.remove(all_table_rows[0])
    all_table_rows.pop()

    for row in all_table_rows:
        stat = extract_contents(row.find_all('td'))
        if len(stat) == 5:
            stat = ['', *stat]
        stats.append({SHORT_HEADERS[i]: stat[i] for i in range(0, len(stat))})

    # table = tabulate(stats, headers=SHORT_HEADERS)
    # print(table)

    return(stats)
