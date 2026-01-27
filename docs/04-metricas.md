# Avaliação e Métricas

## Como Avaliar seu Agente

A avaliação é feita de duas formas complementares:

1. **Testes estruturados:** Perguntas pré-definidas com respostas esperadas baseadas nos dados do cliente;
2. **Feedback real:** Pessoas testam o agente e atribuem notas de 1 a 5.

---

## Métricas de Qualidade

| Métrica | O que avalia | Exemplo de teste |
|---------|--------------|------------------|
| **Assertividade** | O agente respondeu corretamente? | Perguntar o saldo e receber o valor correto |
| **Segurança** | O agente evitou inventar informações? | Perguntar algo fora do contexto e ele admitir que não sabe |
| **Coerência** | A resposta faz sentido para o perfil do cliente? | Sugerir investimento conservador para cliente conservador |

---

## Exemplos de Cenários de Teste

### Teste 1: Consulta de gastos
- **Pergunta:** "Quanto gastei com alimentação?"
- **Resposta esperada:** Soma das despesas da categoria "alimentação" no `transacoes.csv`
- **Resultado:** [x] Correto  [ ] Incorreto

---

### Teste 2: Recomendação de produto
- **Pergunta:** "Qual investimento você recomenda para mim?"
- **Resposta esperada:** Produto compatível com o perfil moderado do cliente, como Tesouro Selic ou CDB de liquidez diária
- **Resultado:** [x] Correto  [ ] Incorreto

---

### Teste 3: Pergunta fora do escopo
- **Pergunta:** "Qual a previsão do tempo?"
- **Resposta esperada:** O agente informa que é especializado em finanças e não responde previsões climáticas
- **Resultado:** [x] Correto  [ ] Incorreto

---

### Teste 4: Informação inexistente
- **Pergunta:** "Quanto rende o produto XYZ?"
- **Resposta esperada:** O agente admite não ter essa informação disponível
- **Resultado:** [x] Correto  [ ] Incorreto

---

## Resultados

**O que funcionou bem:**
- Respostas financeiras coerentes com o perfil do usuário.
- Boa interpretação das transações e categorização dos gastos.
- Segurança ao não inventar informações.

**O que pode melhorar:**
- Melhorar a linguagem para usuários iniciantes.
- Expandir a base de produtos financeiros.
- Adicionar visualizações gráficas no futuro.

---

## Métricas Avançadas (Opcional)

- Tempo médio de resposta do agente.
- Taxa de erro nas respostas.
- Consumo de tokens por interação.

Ferramentas como LangWatch e LangFuse podem ser utilizadas futuramente para monitoramento e observabilidade.
