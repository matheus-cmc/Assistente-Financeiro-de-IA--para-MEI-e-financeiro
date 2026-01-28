# 📚 Base de Conhecimento

## 📁 Dados Utilizados

| Arquivo | Formato | Utilização no Agente |
|---------|---------|---------------------|
| `transacoes.csv` | CSV | Analisar receitas e despesas do usuário |
| `perfil_usuario.json` | JSON | Personalizar orientações financeiras |
| `metas_financeiras.json` | JSON | Acompanhar metas e planejamento |
| `historico_interacoes.csv` | CSV | Manter contexto das conversas |

---

## 🔧 Adaptações nos Dados

Os dados mockados foram adaptados para o contexto de autônomos, freelancers e MEIs, incluindo categorias como:

- Despesas operacionais
- Impostos e encargos
- Investimentos no negócio
- Metas de reserva financeira

Também foram adicionados campos como datas, valores, categorias e observações para permitir análises mais realistas e personalizadas.

---

## 🔗 Estratégia de Integração

### Como os dados são carregados?

Existem duas abordagens principais:

1. **Injeção direta no prompt** (CTRL+C / CTRL+V);
2. **Carregamento via código**, conforme o exemplo abaixo:

```python
import json
import pandas as pd

# ===== CARREGAR DADOS =====
perfil = json.load(open("./data/perfil_investidor.json"))
transacoes = pd.read_csv("./data/transacoes.csv")
historico = pd.read_csv("./data/historico_atendimento.csv")
produtos = json.load(open("./data/produtos_financeiros.json"))
