import requests
import bs4
import time

start_url = 'https://ru.wikipedia.org/w/index.php?title=%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96' \
            '%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83' \
            '&from=%D0%90 '

alphabet = {
    'А': [],
    'Б': [],
    'В': [],
    'Г': [],
    'Д': [],
    'Е': [],
    'Ё': [],
    'Ж': [],
    'З': [],
    'И': [],
    'Й': [],
    'К': [],
    'Л': [],
    'М': [],
    'Н': [],
    'О': [],
    'П': [],
    'Р': [],
    'С': [],
    'Т': [],
    'У': [],
    'Ф': [],
    'Х': [],
    'Ц': [],
    'Ч': [],
    'Ш': [],
    'Щ': [],
    'Э': [],
    'Ю': [],
    'Я': [],
}


class StatusCodeError(Exception):
    def __init__(self, text):
        self.text = text


class WikiParse:
    def __init__(self, start_url, alphabet):
        self.start_url = start_url
        self.alphabet = alphabet

    @staticmethod
    def _get_soup(url):
        while True:
            try:
                response = requests.get(url)
                if response.status_code == 200:
                    soup = bs4.BeautifulSoup(response.text, 'html.parser')
                    return soup
                raise StatusCodeError(f'{response.status_code}')
            except (requests.exceptions.HTTPError,
                    requests.exceptions.ConnectTimeout,
                    StatusCodeError):
                time.sleep(0.2)

    def create_next_url(self, pagination, up_letter):
        if up_letter in alphabet:
            next_url = f"https://ru.wikipedia.org{pagination[1].attrs['href']}"
            pagination_next, up_letter = self.get_parsing(next_url)
            self.create_next_url(pagination_next, up_letter)
        else:
            print('страницы закончились')
            for elem in self.alphabet:
                self.alphabet[elem] = len(self.alphabet[elem])
                print(f'{elem}:', self.alphabet[elem])
            animals = []
            for key, value in self.alphabet.items():
                animals.append(f'{key}: {value}')

    def get_parsing(self, next_url):
        soup_next = self._get_soup(next_url)
        pagination_next = soup_next.find_all('a', attrs={'title': 'Категория:Животные по алфавиту'})
        soup_page = soup_next.find_all('div', attrs={'class': 'mw-category-group'})
        up_letter = ''
        for teg_div in soup_page:
            up_letter = str(teg_div.find('h3').text).upper()
            if up_letter in self.alphabet:
                print(f'Животные на букву {up_letter}')
                animals = teg_div.ul.text.split('\n')
                self.alphabet[up_letter].extend(animals)
            else:
                print(f'Буква {up_letter} больше не нужна')

        return pagination_next, up_letter

    def run(self):
        pagination, up_letter = self.get_parsing(self.start_url)
        self.create_next_url(pagination, up_letter)


if __name__ == '__main__':
    parser = WikiParse(start_url, alphabet)
    parser.run()
