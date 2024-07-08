
```markdown
# Cannon Blitz

## Visão Geral

Cannon Blitz é um jogo estratégico onde os jogadores se revezam para destruir as bases do 
oponente usando vários tipos de tiros. O objetivo é colocar e defender estrategicamente 
suas bases enquanto tenta destruir as bases do seu oponente.

## Instruções para Execução

Para executar o programa:

```sh
python src/cannonblitz.py
```

Porém, antes disso:

1. Vá para a pasta `src`:
    ```sh
    cd src
    ```

2. Nesta pasta, crie um ambiente virtual:
    ```sh
    python -m venv venv
    ```

3. Ative o ambiente virtual:
    - No Windows:
      ```sh
      venv\Scripts\activate
      ```
    - No macOS/Linux:
      ```sh
      source venv/bin/activate
      ```

4. Em seguida, instale as dependências:
    ```sh
    pip install -r ../requirements.txt
    ```

5. Volte à pasta inicial:
    ```sh
    cd ..
    ```

6. Agora, você pode executar o programa:
    ```sh
    python src/cannonblitz.py
    ```

## Estrutura do Projeto

- **cannonblitz/**: Contém os arquivos principais do jogo.
- **src/**: Contém o código-fonte do jogo.

### Dependências

As bibliotecas necessárias para executar o jogo estão listadas no arquivo `requirements.txt`. Certifique-se de instalar todas as dependências antes de tentar rodar o jogo.
