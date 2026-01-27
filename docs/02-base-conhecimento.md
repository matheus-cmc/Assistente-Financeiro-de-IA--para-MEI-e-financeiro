# Base de Conhecimento

## Dados Utilizados

| Arquivo | Formato | Utilização no Agente |
|---------|---------|---------------------|
| `transacoes.csv` | CSV | Analisar receitas e despesas do usuário |
| `perfil_usuario.json` | JSON | Personalizar orientações financeiras |
| `metas_financeiras.json` | JSON | Acompanhar metas e planejamento |
| `historico_interacoes.csv` | CSV | Manter contexto das conversas |

---

## Adaptações nos Dados

Os dados mockados foram ajustados para o contexto de autônomos e MEIs, incluindo categorias como despesas operacionais, impostos, investimentos no negócio e metas de reserva financeira. Também foram adicionados campos para datas, valores, categorias e observações.

---
## Estratégia de Integração

### Como os dados são carregados?

```python
import pandas as pd
import json

# Carregamento dos dados
transacoes = pd.read_csv("data/transacoes.csv")
historico = pd.read_csv("data/historico_interacoes.csv")

with open("data/perfil_usuario.json", "r", encoding="utf-8") as f:
    perfil = json.load(f)

with open("data/metas_financeiras.json", "r", encoding="utf-8") as f:
    metas = json.load(f)

---

## Exemplo de Contexto Montado



```
Dados do Cliente:
- Nome: Carlos Oliveira
- Tipo de Perfil: Autônomo (MEI)
- Objetivo Principal: Organizar finanças e separar contas pessoais das profissionais
- Saldo atual do negócio: R$ 4.200

Últimas transações:
- 05/01: Cliente X - Receita - R$ 1.500
- 07/01: Aluguel de sala - Despesa - R$ 800
- 10/01: Internet - Despesa - R$ 120
- 12/01: Reserva financeira - Poupança - R$ 300

```
