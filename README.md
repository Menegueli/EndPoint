# Flask JSONPlaceholder API Client

Este é um simples aplicativo Flask que funciona como um cliente para a API JSONPlaceholder, fornecendo uma rota para obter posts dessa API específica. A API JSONPlaceholder é um serviço de teste gratuito que simula um back-end RESTful para aplicativos que precisam realizar operações CRUD em posts.

## Pré-requisitos

Certifique-se de ter o Flask instalado. Você pode instalá-lo usando:

```bash
pip install flask
```

## Como Usar

1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
```

2. Navegue até o diretório do projeto:

```bash
cd seu-repositorio
```

3. Execute o aplicativo:

```bash
python app.py
```

O aplicativo estará disponível em [http://127.0.0.1:5000/](http://127.0.0.1:5000/).

4. Acesse a rota `/api/posts` para obter os posts da API JSONPlaceholder:

```bash
curl http://127.0.0.1:5000/api/posts
```

ou abra a rota no seu navegador.

## Estrutura do Projeto

- `app.py`: Contém o código principal do aplicativo Flask.
- `requirements.txt`: Lista de dependências do Python necessárias para o projeto.

## Contribuindo

Sinta-se à vontade para contribuir com melhorias, correções de bugs ou novos recursos. Basta seguir estas etapas:

1. Fork do repositório
2. Crie uma branch para a sua contribuição: `git checkout -b feature/nova-feature`
3. Faça suas alterações e commit: `git commit -m 'Adiciona nova feature'`
4. Faça push para a branch: `git push origin feature/nova-feature`
5. Envie um Pull Request

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

---

Esse README oferece uma visão geral do seu aplicativo Flask e fornece instruções sobre como configurar, executar e contribuir para o projeto. Certifique-se de personalizar as seções de pré-requisitos, como usar e estrutura do projeto conforme necessário para o seu aplicativo específico.
