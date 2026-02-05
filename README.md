## **🎯 Sobre o Projeto**

Projeto desenvolvido para a disciplina **Qualidade de Software** do Prof. Marcelo - TADS/IFRN, Natal.  
Uma API REST para gestão de serviços artesanais, clientes, pedidos e relacionamentos.

## **🏗️ Arquitetura**

```
┌─────────────────────────────────────────────────────┐
│                    Django REST API                  │
├─────────────────────────────────────────────────────┤
│  Models → Serializers → Views → URLs → Templates    │
└─────────────────────────────────────────────────────┘
```

## **🛠️ Tecnologias Utilizadas**

### **Backend**
- **Python 3.12** - Linguagem principal
- **Django 5.2.1** - Framework web
- **Django REST Framework 3.14** - API REST
- **PostgreSQL 15** - Banco de dados
- **DRF Spectacular** - Documentação OpenAPI/Swagger

### **Qualidade de Código**
- **Flake8** - Análise de estilo PEP8
- **Pylint + pylint-django** - Análise estática
- **Radon** - Métricas de complexidade
- **SonarCloud** - Análise contínua de qualidade

### **DevOps & CI/CD**
- **GitHub Actions** - Pipeline CI/CD
- **Docker** - Containerização
- **Graphviz** - Geração de diagramas UML

## **🔧 Configuração do Ambiente**

### **1. Clone o repositório**
```bash
git clone https://github.com/seu-usuario/artesanato.git
cd artesanato
```

### **2. Configure ambiente virtual**
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate     # Windows
```

### **3. Instale dependências**
```bash
pip install -r requirements.txt
```

### **4. Configure variáveis de ambiente**
```bash
cp .env.example .env.local
# Edite .env.local com suas configurações
```

### **5. Execute migrações**
```bash
python manage.py migrate
```

### **6. Inicie o servidor**
```bash
python manage.py runserver
```

## **✅ Padrões de Qualidade Implementados**

### **1. Análise Estática**
- **Pylint** com configuração personalizada (`.pylintrc`)
- **Flake8** com regras específicas (`.flake8`)
- **Radon** para métricas de complexidade

### **2. Pipeline CI/CD** (`.github/workflows/django-ci.yml`)
- **Detecção de código duplicado** (Radon)
- **Análise de code smells** (Pylint + Radon)
- **Testes automatizados** (Django Test)
- **Geração de diagramas UML** (Django Extensions)
- **Verificação de estilo PEP8**

### **3. Segurança**
- Credenciais em variáveis de ambiente
- Configuração SonarCloud para análise contínua
- Validação de inputs e sanitização
- Proteção contra vulnerabilidades comuns

### **4. Documentação**
- **OpenAPI/Swagger** via DRF Spectacular
- Diagramas UML automáticos
- Documentação de endpoints
- Relatórios de qualidade gerados automaticamente

## **📊 Métricas de Qualidade**

### **Code Quality Gates**
- ✅ Complexidade ciclomática máxima: 10
- ✅ Duplicação máxima: 5%
- ✅ Cobertura de testes mínima: 80%
- ✅ Issues críticos: 0
- ✅ Security hotspots: Resolvidos

## **🔍 Pipeline de Qualidade**

O pipeline executa automaticamente em cada PR/push:

```
1. Análise de Code Smells → 2. Detecção de Duplicação → 
3. Verificação de Estilo → 4. Execução de Testes → 
5. Geração de Diagramas → 6. Upload de Artefatos
```

## **🚚 Deploy**

### **Requisitos para Produção**
1. PostgreSQL configurado
2. Variáveis de ambiente definidas
3. SSL/TLS configurado
4. Servidor WSGI (Gunicorn)
5. Servidor web (Nginx)

## **📚 Recursos Adicionais**

- [Documentação Django](https://docs.djangoproject.com/)
- [Django REST Framework](https://www.django-rest-framework.org/)
- [Guia de Estilo Python (PEP8)](https://peps.python.org/pep-0008/)
- [Conventional Commits](https://www.conventionalcommits.org/)

## **👨‍🏫 Disciplina**

**Qualidade de Software** - TADS/IFRN Natal  
**Professor:** Marcelo  
**Período:** 2025.2

---

**🎯 Objetivo do Projeto:** Desenvolver práticas de qualidade de software através de uma aplicação Django real, implementando análise estática, CI/CD, métricas de qualidade e boas práticas de desenvolvimento.
