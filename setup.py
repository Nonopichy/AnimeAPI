from setuptools import setup, find_packages

# SETUP
setup(
    name="AnimeAPI", # Nome do módulo
    author="AimCaffe", # Criador/Autor
    author_email="alexsandergomes4742@gmail.com", # Email do Criador/Autor
    packages=find_packages(), # Pacotes
    version="1.1.5", # Versão
    license="gpl-3.0", # Licensa
    description="Pesquise, filtre e obtenha informações sobre animes!", # Descrição pequena
    long_description=open("README.md", "r", encoding="utf-8").read(), # Descrição longa
    long_description_content_type='text/markdown', # Tipo da descrição longa
    url="https://github.com/Alexsander4742/AnimeAPI", # Link do repositório
    download_url="https://github.com/Alexsander4742/AnimeAPI/releases", # Baixar o código fonte
    keywords=[
        "animes", 
        "api", 
        "webscraping"
    ], # Tags de pesquisa
    install_requires=[
        "requests",
        "beautifulsoup4",
        "python-slugify"
    ] # Dependências
)
