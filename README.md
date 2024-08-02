# Maze runner competition

[![PyPI Version](https://img.shields.io/pypi/v/maze_runner.svg?style=flat-square)](https://pypi.python.org/p/maze_runner)
[![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=flat-square&logo=github&logoColor=white)](https://github.com/matheusjardimb/maze_runner/)

![https://github.com/matheusjardimb/maze_runner/blob/develop/docs/readme_animation.gif?raw=true](https://github.com/matheusjardimb/maze_runner/blob/develop/docs/readme_animation.gif?raw=true)

## Regras

- Implemente seu algorítmo para encontrar a saída do labirinto
- O programa irá falhar caso o limite de passos for atingido

## Desenvolvimento

Utilize o código da pasta [example/](example/) como referência. Será necessário instalar as
dependências do projeto ([example/requirements.txt](example/requirements.txt)). Sugerimos utilizar a versão do Python
indicada em ([example/.python-version](example/.python-version)).

### Debug no PyCharm

O erro abaixo pode ocorrer no console ao executar o comando `clear` (para limpar o console):
![https://github.com/matheusjardimb/maze_runner/blob/main/docs/debug_error.png?raw=true](https://github.com/matheusjardimb/maze_runner/blob/main/docs/debug_error.png?raw=true)

Para resolvê-lo será necessário ativar "Emulate terminal in output console" no Debug do PyCharm:

![https://github.com/matheusjardimb/maze_runner/blob/main/docs/fix_pycharm.png?raw=true](https://github.com/matheusjardimb/maze_runner/blob/main/docs/fix_pycharm.png?raw=true)

## Contribua!

- [ ] Criou um mapa desafiador? Gere um MR adicionando-o na pasta maps
- [ ] Add menu seletor de mapa (lista todas opções de .csv em maps/)
- [ ] Servir os mapas como uma API
