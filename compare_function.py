import requests
from bs4 import BeautifulSoup


def compare(val1, val2):
    """Function which allows us compare 2 currencies, using google finance."""

    response = requests.get(f'https://www.google.com/finance/quote/{val1}-{val2}')

    soup = BeautifulSoup(response.text, 'lxml')
    convert = soup.find_all('div', class_="YMlKec fxKbKc")
    try:
        convert = convert[0].text
    except IndexError:
        return 'Try again'


    return f'1 {val1.upper()} = {convert} {val2.upper()}'

#test
# print(compare('usd', 'btc'))