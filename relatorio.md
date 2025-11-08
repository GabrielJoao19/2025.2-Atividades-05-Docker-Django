#  Relatório de Conteinerização do Projeto Django

## 1. Introdução

O objetivo desta atividade foi **conteinerizar um projeto Django**, criando ambientes distintos para **Desenvolvimento (`django-dev`)** e **Produção (`django-prod`)** utilizando imagens baseadas no **Fedora**.  

O foco deste relatório é detalhar os **erros críticos encontrados no ambiente de Produção** e as **correções realizadas** para garantir o funcionamento do servidor.

---

## 2. Análise dos Problemas e Correções


- Estruturação errada dos diretórios
  

---

### 2.1.  Correção do Caminho do Código (`manage.py`)

**Erro inicial:**  
```
python3: can't open file '/app/manage.py': [Errno 2] No such file or directory
```

| Tipo | Descrição |
|------|------------|
| **Problema** | O arquivo `manage.py` não era encontrado no diretório de trabalho (`/app`) do contêiner. |
| **Solução** | Estrutura da maneira correta os diretórios |


---

## 3. Conclusão e Resultado

Após a estruturação dos diretórios da maneira adequada, o servidor Django foi iniciado com sucesso no contêiner de Produção.

| Item | Status |
|------|--------|
| **Status do Contêiner** |  UP (Rodando em segundo plano) |
| **Log de Sucesso** | `Watching for file changes with StatReloader`, confirmando que o servidor Django iniciou corretamente. |
| **Acesso à Aplicação** | [http://localhost:8080](http://localhost:8080) |

---

###  Lição Aprendida

A principal lição aprendida é que a **sincronização exata entre a estrutura local do projeto e a instrução `COPY` do `Dockerfile`** é crítica para a **estabilidade do ambiente de Produção**.
