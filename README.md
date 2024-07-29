# Maze runner competition

[![PyPI Version](https://img.shields.io/pypi/v/maze_runner.svg?style=flat-square)](https://pypi.python.org/p/maze_runner)
[![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=flat-square&logo=github&logoColor=white)](https://github.com/matheusjardimb/maze_runner/)

## Regras

- Implemente seu algorítmo para encontrar a saída do labirinto
- O programa irá falhar caso o limite de passos for atingido

## TODO

- [x] Publicar projeto como lib pip
- [x] Add limitador de passos ('timeout')
- [x] Contar quantos passos foram dados até o momento (e no final)
- [ ] Gerar gif da animação total?
    - [X] Add rodapé e cabeçalho no gif
    - [ ] Add número de vezes que cada célula foi 'pisada'
- [ ] Add imagem em "Social preview" no GitHub
- [ ] Add menu seletor de mapa (lista todas opções de .csv em maps/)
- [ ] Servir os mapas como uma API

## Desenvolvimento

Utilize o código [example/running_maze.py](example/running_maze.py) como referência. Será necessário instalar as
dependências do projeto ([example/requirements.txt](example/requirements.txt)) e utilizar a versão correta do
Python ([example/.python-version](example/.python-version)).

## Debug no PyCharm

O erro abaixo pode ocorrer no console ao executar o comando `clear` (para limpar o console):
![debug_error.png](docs%2Fdebug_error.png)

Para resolvê-lo será necessário ativar "Emulate terminal in output console" no Debug do PyCharm:

![fix_pycharm.png](docs%2Ffix_pycharm.png)