
# Tops
def tops() -> list:

    r"""Featured Animes

        Description: SID and Featured Anime Image
    """

    # Módulos
    from .tops import Init
    
    return Init()

# Search
def search(title: str, page: int = 1) -> list:
    
    r"""Search for animes

        Description: List of animes according to page and title.
        Params:
            title # Anime name
            page # Page ( OPTIONAL ) 
    """

    # Módulos
    from .search import Init
    from ._utils_ import Slug
    from ._errs_ import InvalidNumber

    if not page >= 1:
        raise InvalidNumber("page")

    return Init(title=Slug(title), page=page)

# Filter
def filter(key: str, value: str, page: int = 1) -> list:

    r"""Filter animes

        Description: List of animes according to page and title.
        Params:
            key: Valid key
            value: Key value
            page: Page ( OPTIONAL )
    """

    # Módulos
    from .filter import Init
    from ._errs_ import InvalidNumber

    if not page >= 1:
        raise InvalidNumber("page")

    return Init(key=key, value=value, page=page)

# Anime
def anime(SID: str):
    
    # Módulos
    from .anime import Init
    from ._utils_ import Soup
    from ._errs_ import AnimeNotFound

    # Anime existe
    soup = Soup(f"https://animefire.net/animes/{SID}-todos-os-episodios")
    if not soup.contents or soup.title.text == "404 Not Found":
        raise AnimeNotFound

    return Init(SID=SID, soup=soup)