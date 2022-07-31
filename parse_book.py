import bs4
import requests


def find_books():
    """ The function sends a request to a page with e-books.
    Selects book titles and links to access them.
    Returns the received data as a dictionary."""
    target_list = {}  # dictionary to save target data
    request = requests.get('https://monster-book.com/python-knigi').text  # request to the url
    soup = bs4.BeautifulSoup(request, 'html.parser')  # get data from url
    book_list = soup.find_all('div', class_='views-field views-field-title')  # select the necessary data
    for book in book_list:
        book_name = book.text  # find book's name
        link = book.find('a').get('href')  # find book's link
        full_link = 'https://monster-book.com/' + link  # full link
        target_list.update({book_name: full_link})  # update dictionary
    return target_list

