import requests
from bs4 import BeautifulSoup
from tabulate import tabulate
import os
import numpy as np
import matplotlib.pyplot as plt
from flask import Flask, jsonify
# import json


def extract_contents(row): return [x.text.replace('\n', '') for x in row]


def get_stats():
    URL = 'https://www.mohfw.gov.in/'

    response = requests.get(URL).content
    soup = BeautifulSoup(response, 'html.parser')

    cases = soup.find(id='state-data')
    HEADERS = extract_contents(cases.find_all('th'))
    
    stats = []

    if cases:
        all_table_rows = cases.find_all('tr')
        all_table_rows.remove(all_table_rows[0])
        # all_table_rows.pop()

        for row in all_table_rows:
            stat = extract_contents(row.find_all('td'))
            if len(stat) < len(HEADERS):
                stat = ['', *stat]
            # stats.append({HEADERS[i]: stat[i] for i in range(0, len(stat))})
            stats.append(stat)

        # table = tabulate(stats, headers=HEADERS)
        # print(table)

    # print(stats)

    return(stats, HEADERS)

get_stats()
