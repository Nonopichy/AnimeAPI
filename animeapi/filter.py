
# Módulos
from ._utils_ import Cards
from ._variables_ import filters
from ._errs_ import InvalidKeyOrValue

# Inicialização
def Init(**args):
    try:
        return Cards(f"https://animefire.net/{filters[args['key']][args['value']]}/{args['page']}")
    except KeyError:
        raise InvalidKeyOrValue