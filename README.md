# Sistema de Cadastro de Clientes

Aplicação desktop para cadastro e gerenciamento de clientes, desenvolvida em Python com interface gráfica moderna utilizando CustomTkinter. O projeto segue a arquitetura **MVC (Model-View-Controller)** e utiliza **SQLite** como banco de dados local.

---

## Tecnologias Utilizadas

- [Python 3](https://www.python.org/)
- [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter) - Interface gráfica moderna e responsiva
- [SQLite3](https://www.sqlite.org/index.html) - Banco de dados embutido

---

## Funcionalidades

- Tela de login com autenticação de usuários
- Cadastro de novos clientes (Nome, E-mail, Telefone)
- Listagem automática de todos os clientes cadastrados
- Atualização da lista em tempo real após cada cadastro
- Validação de campos obrigatórios
- Banco de dados local persistente (`banco.db`)

---

## Estrutura do Projeto (MVC)

```
Sistema de cadastro de cliente/
├── main.py                  # Ponto de entrada da aplicação
├── Model/
│   ├── ConexaoModel.py      # Conexão e operações com o banco SQLite
│   └── banco.db             # Arquivo do banco de dados
├── View/
│   └── JanelaView.py        # Interface gráfica (telas de login e clientes)
├── Controller/
│   └── LoginController.py   # Regras de negócio e validações
└── README.md
```

---

## Pré-requisitos

- Python 3.8 ou superior instalado
- Pacote `customtkinter` instalado

---

## Como Executar

1. Clone este repositório:
```bash
git clone https://github.com/Calebe-josue/Sistema-cadastro-de-clientes
```

2. Acesse a pasta do projeto:
```bash
cd "Sistema de cadastro de cliente"
```

3. Instale a dependência necessária:
```bash
pip install customtkinter
```

4. Execute a aplicação:
```bash
python main.py
```

---

## Login Padrão

Para acessar o sistema, utilize as credenciais pré-cadastradas:

- **Usuário:** `Calebe`
- **Senha:** `1234`

---



### Tela de Login
Interface simples e intuitiva para autenticação do usuário.

### Tela de Clientes
Após o login, você poderá:
- Cadastrar novos clientes preenchendo os campos Nome, E-mail e Telefone
- Visualizar a lista atualizada automaticamente
- Clicar em **Atualizar** para recarregar os dados do banco

---

## Melhorias Implementadas

- Conexões com o banco de dados abertas e fechadas corretamente a cada operação, evitando travamentos
- Validação de campos vazios no cadastro de clientes
- Limpeza automática dos campos após cadastro bem-sucedido
- Mensagens de feedback (sucesso/erro) na interface
- Formatação organizada da lista de clientes

---

## Autor

Desenvolvido por [Calebe](https://github.com/seu-usuario)

Sinta-se à vontade para contribuir, reportar issues ou sugerir melhorias!

