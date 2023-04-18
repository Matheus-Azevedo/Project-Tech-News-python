import sys
from tech_news.analyzer.search_engine import (
    search_by_title,
    search_by_date,
    search_by_category,
)
from tech_news.analyzer.ratings import top_5_categories
from tech_news.scraper import get_tech_news


def option_zero():
    print('Digite quantas notícias serão buscadas:')
    option = int(input())
    print(get_tech_news(option))


def option_one():
    print('Digite o título:')
    option = input()
    print(search_by_title(option))


def option_two():
    print('Digite a data no formato aaaa-mm-dd:')
    option = input()
    print(search_by_date(option))


def option_three():
    print('Digite a categoria:')
    option = input()
    print(search_by_category(option))


def option_four():
    print('Top 5 categorias:')
    print(top_5_categories())


def menu_response(option):
    menu_options = {
        '0': option_zero,
        '1': option_one,
        '2': option_two,
        '3': option_three,
        '4': option_four,
    }
    return menu_options[option]()


# Requisitos 11 e 12
def analyzer_menu():
    condition = True
    while condition:
        print('Selecione uma das opções a seguir:')
        print('0 - Popular o banco com notícias;')
        print('1 - Buscar notícias por título;')
        print('2 - Buscar notícias por data;')
        print('3 - Buscar notícias por categoria;')
        print('4 - Listar top 5 categorias;')
        print('5 - Sair.')
        option = input()
        if option not in ['0', '1', '2', '3', '4', '5']:
            print('Opção inválida', file=sys.stderr)
        elif option == '5':
            condition = False
        else:
            menu_response(option)
