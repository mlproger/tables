from bs4 import BeautifulSoup
import pandas as pd

def first_numbers(file_name, inn):
    file = open(f"data/{file_name}", "r")
    index = file.read()
    s = BeautifulSoup(index, 'lxml')
    blocks = s.find_all('div', {"class":"reportContentUI"})

    info_index = 0

    for block in range(len(blocks)):
        if inn in blocks[block].text and "Телефон" in blocks[block].text:
            info_index = block
    first_number = ""
    for i in blocks[info_index]:
        if "Телефон:" in i.text:
            first_number = i.text.replace('Телефон:',' ').replace('\n', '')
    file.close()
    return first_number

def birthsday_date(file_name, inn):
    file = open(f"data/{file_name}", "r")
    index = file.read()
    s = BeautifulSoup(index, 'lxml')
    blocks = s.find_all('div', {"class":"reportContentUI"})

    info_index = 0

    for block in range(len(blocks)):
        if inn in blocks[block].text and "День рождения:" in blocks[block].text:
            info_index = block
    birthsday = ""
    for i in blocks[info_index]:
        if "День рождения:" in i.text:
            birthsday = i.text.replace('День рождения:',' ').replace('\n', '').replace(' ', '')

    file.close()

    return birthsday


def email(file_name, inn):
    file = open(f"data/{file_name}", "r")
    index = file.read()
    s = BeautifulSoup(index, 'lxml')
    title = s.find_all('div', {"class":"grid_column_title"})
    result = s.find_all('div', {"class":"grid_column_result"})

    emails = []

    for i in range(len(title)):
        if "Email" in title[i].text:
            emails.append(result[i].text)


    file.close()

    return ','.join(emails)



def second_Numbers(file_name, inn):
    file = open(f"data/{file_name}", "r")
    index = file.read()
    s = BeautifulSoup(index, 'lxml')
    blocks = s.find_all('div', {"class":"prod_search_ui"})

    numbers = ""

    for i in blocks:
        if "Телефон:" in i.text:
            numbers = i.text.replace('Телефон:','')
            break
    
    file.close()

    return ','.join(numbers.split(','))







