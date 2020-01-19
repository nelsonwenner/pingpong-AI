<h1 align="center">
  <img src="https://user-images.githubusercontent.com/40550247/72228004-81071600-3581-11ea-9972-1cbe906001ed.png" width="120px" />
</h1>

<h1 align="center">
  Pingpong 
Artificial Intelligence 
</h1>

<p align="center">
  <img alt="GitHub language count" src="https://img.shields.io/github/languages/count/nelsondiaas/pingpong-IA?color=%2304D361">

  <a href="https://github.com/nelsondiaas">
    <img alt="Made by @nelsondiaas" src="https://img.shields.io/badge/made%20by-%40nelsondiaas-%2304D361">
  </a>

  <img alt="License" src="https://img.shields.io/badge/license-MIT-%2304D361">

  <a href="https://github.com/nelsondiaas/bookstore-frontend/stargazers">
    <img alt="Stargazers" src="https://img.shields.io/github/stars/nelsondiaas/pingpong-IA?style=social">
  </a>
</p>

### Prerequisites
* Python (>= 3.6)

## Getting Started
1. Fork este repositório e clone em sua máquina
2. Mude o diretório para `pingpong-IA` onde você o clonou;
3. No terminal, execute:

```bash
/* Install dependencies */

$ pip install -r requeriments.txt

/* Coletar dados */

$ python PingPongCollect.py

/* Treinar dados */

$ python NeuralNetwork.py

/* Executar IA */

$ python PingPongIA.py
```

### Neural Network
A rede neural possue uma camada de entrada de 2 neurônios, uma camada oculta que possue 30 neurônios, e uma camada de saida de 1 neurônio. A rede pode ser personalizada apenas com a quantidade de neurônios.


## File Structure

```bash
pingpong-IA
├── src/
│   ├── database/
│   │   ├── controller/
│   │   │   └── db.py
│   │   ├── data/
│   │   │   └── data-50.txt
│   │   └── weights/
│   │       ├── weight-w1.txt
│   │       └── weight-w2.txt
│   ├── network/
│   │   └── NeuralNetwork.py
│   ├── PingPongCollect.py
│   └── PingPongIA.py
├── .gitignore
├── LICENSE.md
├── README.md
└── requeriments.txt
```

### Vision
O objetivo desse jogo, é que a palheita não deixe a bolinha tocar no chão. A implementação se consiste em um aprendizado de maquina supervisionado, por tanto teremos que passar ao jogo dados iniciais para que o mesmo processe o aprendizado. No arquivo ``src/PingPongCollect.py``, ele ira executar o jogo para que você jogue e colete informações para serem usadas no aprendizado de sua maquina, os dados seram salvos em ``src/database/data``. Logo em seguida você poderá treinar seus dados de duas formas, a primeira delas você podera executar os dados coletados diretamente na redeneural sem precisar jogar, no ```terminal``` será impresso uma imformação, que é a taxa de error do treinamento de sua rede neural, quanto menor a taxa melhor, no final desse treinamento sera salvo os pessos em ```src/database/weights```, essas informações são dos neurônios treinados de sua rede, no caso o cerebro o conhecimento em si, a segunda forma de treinar a sua rede e jogando diretamente, no caso treinando e jogando ao mesmo tempo. Para fazer a sua maquina jogar, você tera que executar o arquivo ```src/PingPongIA.py``` lá você pode tanto já setar os pessos emitidos pelo treinamento de sua rede, ou não passar nenhum peso e deixar o aprendizado do zero.

<h1 align="center">
  <img src="https://user-images.githubusercontent.com/40550247/72673856-684da300-3a4e-11ea-8625-b3e597e4838a.gif" width="923px" height="620px"/>
</h1>

## License

Esse projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE.md) para mais detalhes.

---