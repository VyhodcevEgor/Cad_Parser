import requests
from bs4 import BeautifulSoup as BS
from random import randrange
from time import sleep


cad_numbers = []
result = []


def get_new_price(c_num):
    payload = {
        'cadnumber': c_num
    }
    answer = requests.post(
        "http://gupski.ru/wp-content/themes/stav_kray/cadvalue/getInfo.php",
        data=payload)

    bs_ans = BS(answer.text, "html.parser")
    price = bs_ans.find_all("li")
    price = price[-1]
    res = price.text
    return res


if __name__ == '__main__':
    cad_length = len(cad_numbers)
    for idx, cad_num in enumerate(cad_numbers):
        new_price = get_new_price(cad_num)
        result.append({
            'cad_number': cad_num,
            'new_price': new_price
        })
        print(f"Done: {idx + 1}/{cad_length}")
        sleep(randrange(4, 7))
    print(result)
