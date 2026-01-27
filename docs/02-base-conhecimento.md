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
Existe duas possibilidades, injetar os dados diretamente no prompt(CTRL+C, CTRL+V) ou carregar os arquivos via codigo como no exemplo abaixo:

```python
import json
import pandas as pd

# ===== CARREGAR DADOS =====
perfil = json.load(open("./data/perfil_investidor.json"))
transacoes = pd.read_csv("./data/transacoes.csv")
historico = pd.read_csv("./data/historico_atendimento.csv")
produtos = json.load(open("./data/produtos_financeiros.json"))


---

## Exemplo de Contexto Montado



```

### Como os dados são usados no prompt?

Dados do Cliente:
- Nome: Carlos Oliveira
- Profissão: Designer Freelancer (MEI)
- Perfil Financeiro: Conservador
- Objetivo Principal: Organizar finanças e separar contas pessoais das profissionais
- Saldo atual do negócio: R$ 4.200

Últimas transações:
- 05/01: Cliente X - Receita - R$ 1.500
- 07/01: Aluguel de sala - Despesa - R$ 800
- 10/01: Internet - Despesa - R$ 120
- 12/01: Reserva financeira - Poupança - R$ 300

Produtos disponíveis para ensino:
- Tesouro Selic: Renda fixa, baixo risco, ideal para reserva de emergência.
- CDB Liquidez Diária: Renda fixa, baixo risco, bom para capital de giro.
- LCI/LCA: Renda fixa, isento de IR, indicado para médio prazo.
- Fundo Multimercado: Risco médio, indicado para diversificação.
- Fundo de Ações: Alto risco, indicado para longo prazo.


```
