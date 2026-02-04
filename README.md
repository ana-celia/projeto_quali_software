# Artesanato
Atividade para a diciplina de banco de dados para a criação de modelos ORM no django.<br>
O prestador de serviço escolhido foi o artesão, pois utilizarei um projeto com este dominío na matéria de interfaces ricas e esta é uma oportunidade de um ponta pé inicial para a implementação do backend. Ademais, o escopo cumpre um bom propósito para demonstração da atividade requisitada.

## Modelo de dados
```mermaid
---
title: Modelo Conceitual Artesanato
---
erDiagram 
    CLIENTE }o--|{ SERVICO : contrata
    PEDIDO ||--o{ CLIENTE : associado
    PEDIDO }o--|| SERVICO : associado
    FORMA_PAGAMENTO }|--|| PEDIDO : possui
    ENDERECO }|--|| CLIENTE : possui
    CLIENTE ||--o{ RELACAO : tem
``` 
```mermaid
---
title: Modelo Lógico Artesanato
---
erDiagram 
    CLIENTE }o--|{ SERVICO : contrata
    PEDIDO ||--o{ CLIENTE : associado
    PEDIDO }o--|| SERVICO : associado
    FORMA_PAGAMENTO }|--|| PEDIDO : possui
    ENDERECO }|--|| CLIENTE : possui
    CLIENTE ||--o{ RELACAO : tem
    
    CLIENTE {
        int clienteId Pk
        VARCHAR(250) nome
        INT telefone
        TEXT redeSocialLink
    }
    SERVICO {
        int servicoId Pk
        VARCHAR(250) nome
        FLOAT valor
        TIME_STAMP tempoPrevisto
    }
    PEDIDO {
        int pedidoId Pk
        VARCHAR(250) situacao
        VARCHAR(500) descricao
        FLOAT valorAssociado
        FLOAT valorTotal
        FLOAT taxaExtra
        TIME_STAMP dataRecebimento
        TIME_STAMP dataEntrega
        INT formaPagamento Fk
        INT cliente Fk
        INT servico FK
    }
    FORMA_PAGAMENTO {
        VARCHAR(250) nome
        VARCHAR(500) descricao
        FLOAT taxa
    }
    RELACAO{
        INT pessoa01 Fk
        INT pessoa02 Fk
        VARCHAR(250) tipo 
        VARCHAR(250) parentesco 
    }
    ENDERECO {
        INT cliente FK
        VARCHAR(250) rua
        INT numero
        VARCHAR(250) bairro
        VARCHAR(250) cidade
        VARCHAR(250) estado
        INT cep 
    }

```