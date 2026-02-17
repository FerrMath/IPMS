# Sistema de Gerenciamento de Inventário e Produtos
<br>

**Idiomas:** [English](./README.md) | português 
## Descrição do projeto

Um sistema para gerenciar o inventário e os dados de produtos de uma loja. Ele acompanha mudanças no estoque, valida entradas de produtos e bloqueia operações em produtos descontinuados. O sistema foca em manter a consistência dos dados e facilitar o controle de estoque.

## Funcionalidades

- Acompanhar níveis de estoque para cada produto.  
- Validar informações do produto antes de atualizações ou adições.  
- Impedir a venda de produtos marcados como descontinuados.  
- Categorização básica de produtos.  
- Registrar alterações de estoque (por exemplo, vendas, reposição).  

## Stack Tecnológico

### Backend

- **Linguagem:** Python  
- **Framework:** Flask – gerencia rotas, endpoints de API e lógica básica de requisição/resposta.  
- **Banco de Dados:** MySQL – armazena informações de produtos, estoque e categorias.  
- **ORM:** SQLAlchemy – mapeia tabelas do banco para objetos Python e gerencia consultas.  
- **Migrations:** Alembic – gerencia alterações no esquema do banco de dados de forma segura ao longo do tempo.  

### Frontend

- **Templates:** Jinja – gera páginas HTML dinâmicas usando dados do backend.  
- **Markup & Estilo:** HTML e CSS – layout e estilo básicos.  
- **Interatividade:** JavaScript – funcionalidade mínima no lado do cliente.  

### Futuras Atualizações do Frontend

- Substituir ou complementar os templates Jinja com **React** para uma interface mais dinâmica e responsiva.  
- Usar componentes React para gerenciar listagem de produtos, atualizações de estoque e validação de formulários.  
