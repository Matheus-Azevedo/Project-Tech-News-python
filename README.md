# Tech News
### Autor: Matheus Eduardo de Sousa Azevedo

Este projeto foi desenvolvido por mim e faz parte do acervo de atividades executadas na escola de programação Trybe. A formação ao longo de 1 ano em Desenvolvimento Web desta instituição  conta com mais de 1.500 horas de aulas e aborda introdução ao desenvolvimento de software, front-end, back-end, ciência da computação, engenharia de software, metodologias ágeis e habilidades comportamentais. Tudo voltado totalmente para o mercado de trabalho com intuito de entregar um profissional adequado para a realidade atual. 

# Sobre o projeto

O projeto Tech News tem como objetivo realizar consultas em notícias sobre tecnologia, utilizando técnicas de raspagem de dados para extrair informações do blog da Trybe. Serão utilizados o terminal interativo do Python e módulos personalizados, que serão importados em outros códigos. Os dados extraídos serão armazenados em um banco de dados para posterior utilização.

# O que foi desenvolvido

O conjunto de requisitos consiste em quatro funções que fazem parte do processo de raspagem de notícias do blog da Trybe:

1.  A função fetch: é responsável por fazer a requisição HTTP ao site e obter o conteúdo HTML. A função respeita um Rate Limit de 1 requisição por segundo, retorna o conteúdo HTML da resposta se a requisição for bem-sucedida com Status Code 200: OK e retorna None se a resposta tiver um código de status diferente de 200 ou se a requisição não receber resposta em até 3 segundos. É necessário definir o header user-agent como "Fake user-agent" para que a raspagem do blog da Trybe funcione corretamente.
    
2.  A função scrape_updates: é responsável por fazer o scrape da página inicial do blog da Trybe para obter uma lista contendo as URLs das notícias listadas. A função não inclui a notícia em destaque da primeira página, apenas as notícias dos cards. A função retorna uma lista vazia se não encontrar nenhuma URL de notícia.
    
3.  A função scrape_next_page_link: é responsável por fazer o scrape da URL da próxima página do blog da Trybe. A função retorna a URL obtida se encontrar o link da próxima página e retorna None caso contrário.
    
4.  A função scrape_news: é responsável por fazer o scrape dos dados de uma única notícia para preencher um dicionário com as seguintes informações: URL, título, data, autor, tempo de leitura, resumo e categoria. A função retorna o dicionário preenchido.
    

As funções foram implementadas em Python no arquivo "scraper.py" na pasta "tech_news". As funções foram testadas manualmente e atendem aos requisitos especificados. As funções foram submetidas a avaliação automatizada pelo avaliador, que verifica se o código implementado atende aos requisitos definidos.
