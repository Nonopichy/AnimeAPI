from distutils.core import setup
from setuptools import find_packages

# README
try:
    long_description = open("README.md", encoding="utf-8")
except Exception:
    long_description = ""

# SETUP
setup(
    name="AnimeAPI", # Nome do módulo
    packages=find_packages(), # Pacotes
    version="0.1", # Versão
    license="gpl-3.0", # Licensa
    description="Pesquise, filtre e obtenha informações sobre animes!", # Descrição pequena
    long_description=long_description, # Descrição longa
    long_description_context_type="text/markdown", # Tipo da descrição longa
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