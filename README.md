<div align="center">
    <img src="https://static.zerochan.net/Tanya.Degurechaff.full.2957403.png" width="456" height="456"></img>
    <h1><strong>ANIME API</strong></h1>
    <p><pre>Pesquise, filtre e obtenha informações sobre animes!</pre></p>
    <hr>
</div>

<div>
    <pre>
        <h2 align="center">Informações</h2>
        <p align="center"> 
            <br>Colete informacões e episódios de animes, utilizando este módulo Python.
            <br>Utiliza-se <strong>Web Scraping</strong> em paginas de Animes, para favorecer informações.
            <br>Desenvolvido com intuito de aprendizado, não <strong>responsabilizo-me</strong> pelo seu uso!
        </p>
    </pre>
    <hr>
</div>

<div>
    <pre align="center"><h2>Instalação</h2><p>Você pode instalar pelo gerenciador de pacotes <a href="https://pypi.org/project/fireapi"><strong>PIP</strong></a> ou manualmente, na pagina do <a href="https://github.com/Alexsander4742/FireAPI/releases">Github</a>!</p></pre>
    <h3>MANUALMENTE:</h3>
    <p>
    Baixando o repositório, instale o módulo: <code>setuptools</code>,
    execute em um <strong>terminal</strong>:
        <ul>
            <li>LINUX: <code>python3 setup.py install</code></li>
            <li>WINDOWS: <code>python setup.py install</code></li>
        </ul>
    </p>
    <hr>
</div>

<div>
    <pre align="center"><h2>Métodos</h2><p>Funções que você pode utilizar</p></pre>
    <ul>
        <li><h3>Tops: </h3><p><code>tops()</code></p></li>
        <li><h3>Search: </h3><p><code>search("One Piece", 1) -> ( Nome do Anime, Página <strong>OPCIONAL</strong> )</code></p></li>
        <li><h3>Filter: </h3><p><code>filter("genre", "action", 1) -> ( <a href="https://github.com/Alexsander4742/FireAPI#metodo-filter">Categoria</a>, <a href="https://github.com/Alexsander4742/FireAPI#metodo-filter">Sub-categoria</a>, Página <strong>OPCIONAL</strong> )</code></p></li>
        <li><h3>Anime: </h3><code>anime("one-piece") -> ( <strong>SID</strong> do Anime )</code></li>
    </ul>
    <hr>
</div>

<div>
    <pre align="center"><h2>Método: Filter</h2><p>Categorias & Sub-categorias válidas</p></pre>
    <ol>
        <li>
        animes
        <ul>
            <li>release</li>
            <li>top</li>
            <li>subtitled</li>
            <li>dubbed</li>
        </ul>
        </li>
        <li>
        movie
        <ul>
            <li>subtitled</li>
            <li>dubbed</li>
        </ul>
        </li>
        <li>
        genre
        <ul>
            <li>action</li>
            <li>martial-arts</li>
            <li>adventure</li>
            <li>comedy</li>
            <li>devils</li>
            <li>tragedy</li>
            <li>ecchi</li>
            <li>space</li>
            <li>sport</li>
            <li>fantasy</li>
            <li>science-fiction</li>
            <li>harem</li>
            <li>horror</li>
            <li>games</li>
            <li>josei</li>
            <li>magic</li>
            <li>robot</li>
            <li>mystery</li>
            <li>military</li>
            <li>music</li>
            <li>parody</li>
            <li>psychological</li>
            <li>novel</li>
            <li>seinen</li>
            <li>shoujo-ai</li>
            <li>shounen</li>
            <li>slice-of-life</li>
            <li>supernatural</li>
            <li>thriller</li>
            <li>super-powers</li>
            <li>vampires</li>
            <li>school-life</li>
        </ul>
        </li>
        <li>
        seasons
        <ul>
            <li>autumn</li>
            <li>winter</li>
            <li>spring</li>
            <li>summer</li>
        </ul>
        </li>
    </ol>
</div>

<div>
    <pre align="center"><h2>Método: Anime</h2><p>Funções da classe</p></pre>
    <ol>
        <li>trailer <code>Trailer/Embed Video</code></li>
        <li>image <code>Thumbnail</code></li>
        <li>genres <code>Gêneros</code></li>
        <li>titles <code>Títulos</code></li>
        <li>
            ep <code>Episódio</code>
            <br>
            <ul>
                <li><code>anime("one-piece").ep(1) -> ( Número do Episódio )</code></li>
            </ul>
        </li>
        <li>
            rank <code>Pontuação</code>
            <ul>
                <li>score <code>Classificação</code></li>
                <li>votes <code>Votos</code></li>
            </ul>
        </li>
        <li>
            info <code>Informações adicionais</code>
            <ul>
                <li>anime("one-piece")["studio"] -> ( Chave/Key )</li>
                <li>
                    Chaves válidas
                    <ul>
                        <li>season <code>Temporada lançada</code></li>
                        <li>studio <code>Estúdio de Produção</code></li>
                        <li>sound <code>Legendado/Dublado</code></li>
                        <li>episode <code>Episódios disponíveis</code></li>
                        <li>release <code>Dia de episódio novo</code></li>
                        <li>description <code>Sinopse</code></li>
                        <li>year <code>Ano lançado</code></li>
                    </ul>
                </li>
            </ul>
        </li>
    </ol>
</div>
