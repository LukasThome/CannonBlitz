### README para Cannon Blitz

## Visão Geral

Cannon Blitz é um jogo estratégico onde os jogadores se revezam para destruir as bases do oponente usando vários tipos de tiros. O objetivo é colocar e defender estrategicamente suas bases enquanto tenta destruir as bases do seu oponente.

## Instruções de Configuração

### Abrindo o jogo

1. **Crie e ative um ambiente virtual:**
    - Navegue até a pasta que contém as pastas `dog` e `config`.
    - Crie um ambiente virtual:
      ```sh
      python -m venv venv
      ```
    - Ative o ambiente virtual:
      - No Windows:
        ```sh
        .\venv\Scripts\activate
        ```
      - No macOS/Linux:
        ```sh
        source venv/bin/activate
        ```

2. **Instale as bibliotecas necessárias:**
    - Execute o comando:
      ```sh
      pip install -r requirements.txt
      ```

3. **Configuração inicial:**
    - Vá até a pasta `config` e siga as instruções contidas nela.

4. **Desenvolva seu jogo:**
    - Utilize a estrutura do projeto para desenvolver seu jogo.

5. **Atualize as bibliotecas necessárias:**
    - Após desenvolver o jogo, execute:
      ```sh
      pip freeze > requirements.txt
      ```

### Distribuindo Seu Jogo

1. **Remova a pasta do ambiente virtual:**
    - Certifique-se de remover a pasta do ambiente virtual (`venv`).

2. **Compacte e envie seu jogo com as seguintes instruções:**
    - Para o destinatário, siga estas etapas:
        1. Crie e ative um ambiente virtual:
            - No Windows:
              ```sh
              Set-ExecutionPolicy RemoteSigned
              ```
            - Crie e ative o ambiente:
              ```sh
              python -m venv venv
              .\venv\Scripts\activate
              ```
        2. Instale as bibliotecas necessárias:
            ```sh
            pip install -r requirements.txt
            ```
        3. Para executar o jogo:
            ```sh
            python <nome_do_seu_jogo>.py
            ```

## Estrutura do Projeto

- **cannonblitz/**: Contém os arquivos principais do jogo.
- **src/**: Contém o código-fonte do jogo.

### Exemplo de Uso

```sh
python cannonblitz.py
```

Certifique-se de que seu ambiente virtual está ativado e todas as dependências estão instaladas antes de executar o jogo.

### Dependências

As bibliotecas necessárias para executar o jogo estão listadas no arquivo `requirements.txt`. Certifique-se de instalar todas as dependências antes de tentar rodar o jogo.

### Contato

Para quaisquer dúvidas ou suporte, entre em contato com o desenvolvedor através do email suporte@cannonblitz.com.

---

Essa é uma visão geral de como configurar, desenvolver e distribuir o jogo Cannon Blitz. Certifique-se de seguir todos os passos cuidadosamente para garantir que o jogo funcione corretamente.