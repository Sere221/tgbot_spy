import wikipediaapi

wiki_wiki = wikipediaapi.Wikipedia('MyProjectName (merlin@example.com)', 'ru')


def viki(text):
    page_py = wiki_wiki.page(text.strip())
    if page_py.exists():
        return f'{page_py.title}\n{page_py.summary[0:200]}\n\nБольше информации тут: {page_py.fullurl}'
    else:
        return 'Информация не найдена'