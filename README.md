### 1. Clonar o Repositório

Primeiro, você precisará clonar o repositório do GitHub para o seu computador. Abra um terminal e execute o seguinte comando:

```bash
git clone https://github.com/pietrobon/webcrawler.git
```

Isso irá baixar o código-fonte do projeto para um diretório local chamado "webcrawler".

### 2. Criar um Ambiente Virtual (Opcional, mas Recomendado)

Para isolar as dependências do seu projeto, é uma boa prática criar um ambiente virtual. Navegue até o diretório do projeto:

```bash
cd webcrawler
```

Em seguida, crie um ambiente virtual:

```bash
python -m venv venv
```

Ative o ambiente virtual (dependendo do seu sistema operacional):

- No Windows:

  ```bash
  venv\Scripts\activate
  ```

- No macOS e Linux:

  ```bash
  source venv/bin/activate
  ```

### 3. Instalar Dependências

Com o ambiente virtual ativado (se você optou por usá-lo), agora você pode instalar as dependências do projeto a partir do arquivo `requirements.txt`:

```bash
pip install -r requirements.txt
```

Isso instalará todas as bibliotecas necessárias listadas no `requirements.txt`.

### 4. Testar função database

É possível realizar um teste antes de partir para execução do `crawler.py`, a função `database.py` pode ser executada a partir de:

```bash
python3 src/database.py
```
A função contém um exemplo de insert e de query de retorno e se seu .env estiver com todas as configurações necessárias, será executada com sucesso.

### 5. Executar o Projeto

Você pode executar o projeto executando o arquivo `crawler.py`. Certifique-se de que você está no diretório raiz do projeto:

```bash
python3 src/crawler.py
```

Isso executará o script `crawler.py` que faz as solicitações da web, extrai os dados, grava no mongodb e também realiza um post no twitter(X).

### 6. Verificar os Resultados

Se executado com sucesso o script irá retornar uma mensagem de sucesso do insert no mongo com o ID do objeto inserido e também o link com o post do twitter.
