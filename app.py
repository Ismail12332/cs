import requests
from bs4 import BeautifulSoup

# Задайте URL сайта, с которого вы хотите извлечь данные
url = 'https://example.com'  # Замените на реальный URL сайта

# Отправьте GET-запрос на указанный URL
response = requests.get(url)

# Проверьте, что запрос прошел успешно (статус код 200)
if response.status_code == 200:
    # Используйте BeautifulSoup для парсинга HTML-страницы
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Найдите элементы с данными на странице с помощью CSS-селекторов или других методов
    # Пример: найдем все элементы с тегом 'span' и классом 'value', где содержатся числа с плавающей точкой
    data_elements = soup.find_all('span', class_='value')
    
    # Обработайте найденные данные 
    for element in data_elements:
        # Получите текстовое значение элемента
        data_value = element.text
        
        # Далее, вы можете сохранить это значение или провести другую обработку
        
        # Пример: сохранить значение в файл
        with open('data.txt', 'a') as file:
            file.write(data_value + '\n')

    print('Данные успешно извлечены и сохранены в файл data.txt')
else:
    print('Произошла ошибка при запросе к сайту. Статус код:', response.status_code)