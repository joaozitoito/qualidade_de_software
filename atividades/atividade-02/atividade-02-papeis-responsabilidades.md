# Atividade 2: Organização da Qualidade no LocalEats

## 1. Identificação

**Turma:** Qualidade de Software  
**Equipe:** Individual  
**Data:** 17/11/2026

### Integrantes

| Nome | Usuário no GitHub |
|---|---|
| João Vítor Goes | @joaozitoito |

**Elemento de Competência:** Identificar papéis, responsabilidades e competências relacionadas às atividades de qualidade e testes.

---

## 2. Tarefa 1: Diagnóstico da situação

### 2.1 Problemas organizacionais

| Problema identificado | Possível consequência para o produto ou para a equipe |
|---|---|
| Não existe um critério claro do que é uma funcionalidade "pronta" | Cada um entrega de um jeito, e funcionalidades chegam ao usuário incompletas ou com defeito |
| Os defeitos são encontrados mas não são registrados nem acompanhados | Os defeitos são esquecidos, voltam a aparecer e ninguém sabe quantos ainda estão abertos |
| Não está definido quem aprova uma nova versão, e algumas tarefas têm várias pessoas enquanto outras não têm ninguém | Versões podem ir para o ar sem ninguém conferir, e quando dá problema ninguém se responsabiliza |

### 2.2 Responsabilidade pela qualidade

**A qualidade do LocalEats deve ser responsabilidade exclusiva do profissional de QA? Justifiquem.**

Não. O QA ajuda muito a testar e encontrar problemas, mas a qualidade começa antes disso. O responsável pelo produto precisa definir bem o que quer, o desenvolvedor precisa fazer testes unitários e revisar o código dos colegas, e o DevOps precisa manter o deploy funcionando. Se só o QA cuidar da qualidade, os defeitos vão ser achados tarde, quando já é mais caro corrigir.

---

## 3. Tarefa 2: Papéis e competências

| Integrante | Papel analisado | Responsabilidades relacionadas à qualidade | Competências técnicas | Competências comportamentais |
|---|---|---|---|---|
| João Vítor Goes | Responsável pelo produto (Product Owner) | Definir o que vai ser feito e a prioridade, escrever os critérios de aceitação junto com a equipe, decidir quais defeitos corrigir primeiro e aprovar a versão | Escrever histórias de usuário e critérios de aceitação, entender o negócio de restaurantes e delivery | Comunicação, tomar decisões, negociar prioridades |
| João Vítor Goes | Desenvolvedor | Implementar as funcionalidades seguindo os critérios de aceitação, criar testes unitários, revisar o código dos colegas e corrigir defeitos | Programação (Python e JavaScript), pytest, TDD, Git | Trabalho em equipe, aceitar críticas na revisão de código, organização |
| João Vítor Goes | QA (analista de qualidade) | Revisar os requisitos, planejar e executar os testes do sistema, automatizar testes com Playwright e registrar os defeitos | Técnicas de teste (particionamento, valor limite, tabela de decisão), automação de testes. A certificação CTFL pode ajudar no desenvolvimento, mas não substitui a experiência | Pensamento crítico, atenção aos detalhes, saber relatar um defeito sem culpar ninguém |
| João Vítor Goes | DevOps | Manter a integração contínua rodando os testes a cada mudança, cuidar dos ambientes de teste e produção e publicar a versão aprovada | CI/CD (por exemplo GitHub Actions), hospedagem na Vercel, monitoramento | Organização, responsabilidade com o sistema no ar, colaboração com dev e QA |

---

## 4. Tarefa 3: Matriz de responsabilidades

Legenda:

- **R:** responsável por executar a atividade;
- **A:** aprovador ou responsável final;
- **C:** consultado antes da execução ou decisão;
- **I:** informado sobre o resultado.

| Atividade de qualidade | Responsável pelo produto | Desenvolvedor | QA | DevOps |
|---|:---:|:---:|:---:|:---:|
| Definir critérios de aceitação | A/R | C | C | – |
| Revisar requisitos | A | C | R | – |
| Implementar a funcionalidade | I | A/R | C | – |
| Revisar o código | – | A/R | C | I |
| Criar testes unitários | – | A/R | C | – |
| Planejar e executar testes do sistema | I | C | A/R | C |
| Registrar e acompanhar defeitos | I | R | A/R | – |
| Priorizar a correção dos defeitos | A/R | C | C | – |
| Aprovar a disponibilização da versão | A | C | C | R |

O "–" quer dizer que o papel não participa daquela atividade. Conferi que toda atividade tem pelo menos um R e só um A.

### 4.1 Lacuna ou conflito encontrado

**Lacuna ou conflito:**  
Na revisão de código, o desenvolvedor é quem faz e quem aprova. Se for o mesmo desenvolvedor que escreveu o código, ele vai estar revisando o próprio trabalho, o que não faz muito sentido.

**Consequência:**  
Erros podem passar despercebidos na revisão e só aparecer nos testes ou para o usuário. Para resolver, a regra seria que quem revisa é sempre um desenvolvedor diferente de quem escreveu o código. Se a equipe for muito pequena, o QA ou um líder técnico pode fazer a revisão.

### 4.2 Práticas de QA recomendadas

| Prática recomendada | Problema que ajuda a resolver | Papéis envolvidos |
|---|---|---|
| Criar uma Definição de Pronto (DoD) e escrever os critérios de aceitação antes de começar a desenvolver. Por exemplo: só está pronto se atender os critérios, tiver testes unitários passando, o código foi revisado e os testes do sistema foram feitos | Falta de clareza sobre quando uma funcionalidade está pronta e funcionalidades chegando com defeito | Responsável pelo produto, Desenvolvedor e QA |
| Registrar todos os defeitos em um só lugar (por exemplo GitHub Issues), com a gravidade e o status (aberto, em correção, em teste, fechado), e olhar essa lista nas reuniões da equipe | Defeitos que não são registrados nem acompanhados, e ninguém sabe quem tem que corrigir | QA, Desenvolvedor e Responsável pelo produto |

---

## 5. Uso de inteligência artificial

**Ferramenta utilizada:**  
Claude (Anthropic), pelo Claude Code.

**Como foi utilizada:**  
Usei para ter ideias de papéis e competências, montar uma primeira versão da matriz RACI e revisar o texto.

**Como as respostas foram verificadas:**  
Conferi a matriz com as regras da atividade (pelo menos um R e só um A em cada linha), vi se cada problema do diagnóstico tinha uma prática ligada a ele e cuidei para não deixar toda a responsabilidade com o QA.
