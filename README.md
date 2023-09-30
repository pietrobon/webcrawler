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

### 4. Executar o Projeto

Você pode executar o projeto executando o arquivo `crawler.py`. Certifique-se de que você está no diretório raiz do projeto:

```bash
python3 src/crawler.py
```

Isso executará o script `crawler.py` que faz as solicitações da web e extrai os dados.

### 5. Verificar os Resultados

O script provavelmente imprimirá os resultados no console. Certifique-se de verificar a saída para ver os dados coletados.

Isso deve permitir que você execute o seu projeto. Lembre-se de personalizar o código de acordo com as suas necessidades específicas.
