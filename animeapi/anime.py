
# Módulos
from ._anime_ import Anime

# Inicialização
def Init(**args) -> Anime:
    anime = Anime(args["SID"])
    return anime