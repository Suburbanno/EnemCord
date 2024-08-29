# EnemCord

> [!WARNING]  
> WIP

EnemCord é um bot para Discord desenvolvido em Python, usando a biblioteca `discord.py`, que permite aos usuários obter questões do ENEM diretamente no Discord. As questões são recuperadas utilizando a API [enem.dev](https://enem.dev).

## Funcionalidades

- 🔍 [WIP] **Busca por Ano e Disciplina**: Os usuários podem buscar questões de anos específicos e de disciplinas específicas do ENEM.
- 🎲 [WIP] **Questão Aleatória**: Obtenha uma questão aleatória para testar seus conhecimentos.
- 📊 [WIP] **Interatividade**: Use botões para responder às questões e receba feedback imediato sobre sua escolha.

## Tecnologias Utilizadas

- **Python**: Linguagem de programação.
- **discord.py**: Biblioteca usada para criar e interagir com o bot no Discord.
- **API [enem.dev](https://enem.dev)**: Usada para obter as questões do ENEM.

## Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/Suburbanno/EnemCord.git
   cd EnemCord
   ```

2. Crie e ative um ambiente virtual (opcional):
   ```bash
   python3 -m venv venv
   venv\Scripts\activate
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

4. Configure suas variáveis de ambiente:
   - Crie um arquivo `.env` na raiz do projeto e adicione suas credenciais, como o token do bot do Discord.
   ```env
   token=token_here
   ```

5. Execute o bot:
   ```bash
   python main.py
   ```

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e pull requests para melhorias ou correções.

1. Fork o repositório.
2. Crie uma branch para sua feature (`git checkout -b feature/nova-feature`).
3. Commit suas mudanças (`git commit -am 'Adiciona nova feature'`).
4. Push para a branch (`git push origin feature/nova-feature`).
5. Abra um Pull Request.

## Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para mais detalhes.
