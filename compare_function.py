import requests
from bs4 import BeautifulSoup


def compare(val1, val2, val3=0):
    """Function which allows us compare 2 currencies, using google finance."""

    response = requests.get(f'https://www.google.com/finance/quote/{val1}-{val2}')

    soup = BeautifulSoup(response.text, 'lxml')
    convert = soup.find_all('div', class_="YMlKec fxKbKc")
    try:
        convert = convert[0].text
    except IndexError:
        return 'Try again'

    if val3 == 0:
        return f'1 {val1.upper()} = {round(float(convert), 2)} {val2.upper()}'
    elif val3 > 0:
        return f'{val3} {val1.upper()} = {round(float(convert)*val3, 4)} {val2.upper()}'
    else: 
        return 'Try again'


#test
# print(compare('usd', 'uah'))
# print(compare('usd', 'uah', 595))
    