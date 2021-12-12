
# Módulos
import unittest
import animeapi

class TestMethods(unittest.TestCase):

    # Tops
    def testTops(self):
        print("\n#1    [{}] TOPS".format("SUCESS" if animeapi.tops() else "ERROR"))

    # Search
    def testSearch(self):
        print("\n#2    [{}] SEARCH".format("SUCESS" if animeapi.search("One Piece") else "ERROR"))
    
    # Filter
    def testFilter(self):
        print("\n#3    [{}] FILTER".format("SUCESS" if animeapi.filter("genre", "action") else "ERROR"))
    
    # Anime
    def testAnime(self):
        print("\n#4    [{}] ANIME".format("SUCESS" if animeapi.anime("one-piece").ep(1) else "ERROR"))

if __name__ == '__main__':
    unittest.main()
