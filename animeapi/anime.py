
# Módulos
from ._objects_ import Anime

# Inicialização
def Init(**args) -> Anime:
    anime = Anime(args["SID"])
    return anime