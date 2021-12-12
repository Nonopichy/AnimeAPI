
# Módulos
from ._utils_ import Cards

# Inicialização
def Init(**args) -> list:

    # Variáveis
    url = "https://animefire.net/pesquisar"
    current = Cards(f"{url}/{args['title']}/{args['page']}")

    return [] if current == Cards(f"{url}/{args['title']}/{args['page'] - 1}") else current
