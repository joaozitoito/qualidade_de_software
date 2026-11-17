# Atividade 3: Estratégia e Projeto de Testes do LocalEats

## 1. Identificação

**Turma:** Qualidade de Software  
**Equipe:** Individual  
**Data:** 17/11/2026

### Integrantes

| Nome | Usuário no GitHub |
|---|---|
| João Vítor Goes | @joaozitoito |

**Elemento de Competência:** Planejar e projetar testes selecionando técnicas adequadas.

**Aplicação:** <https://local-eats-unisenac.vercel.app/>

---

## 2. Tarefa 1: Planejamento dos testes

### 2.1 Objetivo dos testes

Verificar se a pesquisa do LocalEats traz os restaurantes certos quando o usuário busca por culinária ou por localização, como o próprio campo de busca promete, e se o sistema avisa quando não encontra nenhum restaurante.

### 2.2 Escopo

#### Funcionalidades incluídas

| Integrante | Funcionalidade incluída | O que será verificado |
|---|---|---|
| João Vítor Goes | Pesquisar restaurantes por especialidade ou localização | O resultado da busca por localização, por culinária, por um termo que não existe e com o campo vazio |

#### Funcionalidade não incluída

| Funcionalidade não incluída | Justificativa |
|---|---|
| Fazer pedido | Não faz parte do fluxo de pesquisa que escolhi testar, envolve carrinho e finalização e ficaria para outro momento |
| Criar conta e entrar no sistema | Só são usadas para chegar até a pesquisa. Vou usar uma conta de teste que já existe, sem testar essas telas |

### 2.3 Abordagem

| Item | Decisão da equipe | Justificativa |
|---|---|---|
| Níveis de teste | Sistema | A pesquisa vai ser testada pela tela, do campo de busca até a lista de restaurantes, com o sistema inteiro funcionando |
| Tipos de teste | Funcional | O que interessa é se o resultado da pesquisa está certo, não velocidade ou segurança |
| Perspectiva caixa-preta ou caixa-branca | Caixa-preta | Os casos são feitos olhando só o que eu digito e o que aparece na tela, sem olhar o código |
| Técnicas de teste | Particionamento de equivalência | Os termos de busca podem ser separados em grupos que o sistema deveria tratar do mesmo jeito (localização, culinária, termo que não existe e vazio). Testando um de cada grupo já cubro os principais casos |

### 2.4 Ambiente e responsabilidades

| Item | Definição |
|---|---|
| Ambiente necessário | Site https://local-eats-unisenac.vercel.app/, Google Chrome atualizado no computador, internet, uma conta de teste já criada (sem dados reais) e restaurantes cadastrados nas localizações "Centro", "Zona Sul", "Zona Norte" e "Bairro Nobre", com culinárias como "Italiana" e "Japonesa" |
| Responsáveis pelo planejamento | João Vítor Goes |
| Responsáveis pela especificação dos casos | João Vítor Goes |
| Responsáveis pela futura execução | João Vítor Goes |

### 2.5 Critérios

| Critério | Definição da equipe |
|---|---|
| Entrada | Site no ar, conta de teste funcionando e a lista de restaurantes aparecendo na página "Explorar" |
| Saída | Os casos CT01 a CT04 executados, com os resultados e os defeitos encontrados registrados |
| Suspensão | Site fora do ar, não conseguir entrar com a conta de teste ou a página mostrar "Erro ao carregar restaurantes." |

---

## 3. Tarefa 2: Riscos e técnicas de teste

### 3.1 Análise dos riscos

| ID | Integrante | Funcionalidade | Risco | Consequência | Probabilidade | Impacto | Prioridade | Justificativa |
|---|---|---|---|---|:---:|:---:|:---:|---|
| R01 | João Vítor Goes | Pesquisar restaurantes | A busca por culinária (por exemplo "Japonesa") não trazer os restaurantes daquela culinária | O usuário acha que não existe restaurante daquele tipo, desiste da busca e os restaurantes perdem clientes | Alta | Alto | Alta | O campo diz que dá para buscar por culinária, e na Atividade 1 a busca por "italiana" deu "Nenhum restaurante encontrado.". Como a busca é uma das principais funções do app, o impacto é alto |
| R02 | João Vítor Goes | Pesquisar restaurantes | Buscar um termo que não existe, ou com o campo vazio, deixar a tela sem resposta (em branco, carregando para sempre ou com erro) | O usuário não sabe se o sistema travou ou se só não tem resultado | Média | Médio | Média | É um caso que costuma ser esquecido no desenvolvimento, mas atrapalha menos porque a busca com termos válidos continua funcionando |

### 3.2 Aplicação das técnicas

#### Análise do integrante 1

**Integrante:** João Vítor Goes  
**Funcionalidade:** Pesquisar restaurantes por especialidade ou localização  
**Risco relacionado:** R01 e R02  
**Técnica escolhida:** Particionamento de equivalência

**Por que a técnica foi escolhida:**  
Não tem como testar todas as palavras que alguém pode digitar na busca. Mas o sistema deveria tratar igual qualquer termo do mesmo grupo: buscar "Centro" ou "Zona Sul" testa a mesma coisa (busca por localização), e o mesmo vale para "Italiana" ou "Japonesa" (busca por culinária). Então escolhendo um valor de cada grupo eu cubro o R01 (grupo da culinária) e o R02 (termo que não existe e campo vazio) com poucos casos.

**Aplicação da técnica:**  

| Classe | Situação | Valor escolhido | Resultado esperado |
|---|---|---|---|
| Válida 1 | Termo igual a uma localização cadastrada | `Centro` | Só restaurantes do Centro |
| Válida 2 | Termo igual a uma culinária cadastrada | `Japonesa` | Só restaurantes de culinária Japonesa |
| Inválida 1 | Termo que não é nem localização nem culinária | `Lua` | Mensagem "Nenhum restaurante encontrado." |
| Inválida 2 | Campo de busca vazio | (vazio) | Nenhum filtro aplicado, aparecem todos os restaurantes |

**Casos derivados:** CT01 (Válida 1), CT02 (Válida 2), CT03 (Inválida 1) e CT04 (Inválida 2)

---

## 4. Tarefa 3: Casos de teste e rastreabilidade

### 4.1 Casos de teste

### CT01: Pesquisar por uma localização que existe

**Integrante responsável:** João Vítor Goes  
**Funcionalidade:** Pesquisar restaurantes por especialidade ou localização  
**Risco ou requisito relacionado:** Requisito de qualidade da Atividade 1 (resultado correto da pesquisa)  
**Técnica utilizada:** Particionamento de equivalência (classe Válida 1)

**Pré-condição:**  
Estar logado com a conta de teste e com a página "Explorar" mostrando os restaurantes.

**Dados de entrada:**  
Termo de busca: `Centro`

**Passos:**

1. Clicar no campo "Buscar por culinária ou localização...".
2. Digitar `Centro`.
3. Clicar em "Buscar".

**Resultado esperado:**  
Aparecem só restaurantes com localização "Centro", e pelo menos um restaurante aparece.

### CT02: Pesquisar por uma culinária que existe

**Integrante responsável:** João Vítor Goes  
**Funcionalidade:** Pesquisar restaurantes por especialidade ou localização  
**Risco ou requisito relacionado:** R01  
**Técnica utilizada:** Particionamento de equivalência (classe Válida 2)

**Pré-condição:**  
Estar logado, com a página "Explorar" aberta, e existir pelo menos um restaurante de culinária "Japonesa" (dá para ver clicando no filtro "Japonesa").

**Dados de entrada:**  
Termo de busca: `Japonesa`

**Passos:**

1. Clicar no filtro "Todos" para tirar outros filtros.
2. Digitar `Japonesa` no campo de busca.
3. Clicar em "Buscar".

**Resultado esperado:**  
Aparecem os restaurantes de culinária "Japonesa" (os mesmos que aparecem no filtro "Japonesa") e a mensagem "Nenhum restaurante encontrado." não aparece.

### CT03: Pesquisar um termo que não existe

**Integrante responsável:** João Vítor Goes  
**Funcionalidade:** Pesquisar restaurantes por especialidade ou localização  
**Risco ou requisito relacionado:** R02  
**Técnica utilizada:** Particionamento de equivalência (classe Inválida 1)

**Pré-condição:**  
Estar logado e com a página "Explorar" aberta.

**Dados de entrada:**  
Termo de busca: `Lua`

**Passos:**

1. Digitar `Lua` no campo de busca.
2. Clicar em "Buscar".

**Resultado esperado:**  
Nenhum restaurante aparece e o sistema mostra a mensagem "Nenhum restaurante encontrado.".

### CT04: Pesquisar com o campo vazio

**Integrante responsável:** João Vítor Goes  
**Funcionalidade:** Pesquisar restaurantes por especialidade ou localização  
**Risco ou requisito relacionado:** R02  
**Técnica utilizada:** Particionamento de equivalência (classe Inválida 2)

**Pré-condição:**  
Estar logado, com a página "Explorar" aberta e uma busca por `Centro` já feita (a lista está filtrada).

**Dados de entrada:**  
Termo de busca: vazio

**Passos:**

1. Apagar tudo o que está escrito no campo de busca.
2. Clicar em "Buscar".

**Resultado esperado:**  
O filtro é removido e voltam a aparecer todos os restaurantes, igual quando a página é aberta.

### 4.2 Matriz de rastreabilidade

| Integrante | Funcionalidade | Risco ou requisito | Técnica utilizada | Casos de teste |
|---|---|---|---|---|
| João Vítor Goes | Pesquisar restaurantes | Requisito de resultado correto da pesquisa (Atividade 1) | Particionamento de equivalência | CT01 |
| João Vítor Goes | Pesquisar restaurantes | R01: busca por culinária não trazer resultado | Particionamento de equivalência | CT02 |
| João Vítor Goes | Pesquisar restaurantes | R02: termo que não existe ou vazio sem resposta clara | Particionamento de equivalência | CT03 e CT04 |

Todos os riscos têm pelo menos um caso de teste.

---

## 5. Uso de inteligência artificial

**Ferramenta utilizada:**  
Claude (Anthropic), pelo Claude Code.

**Como foi utilizada:**  
Usei para ter ideias de riscos da pesquisa, comparar as técnicas de teste e revisar se os passos dos casos estavam claros.

**Uma sugestão que precisou ser alterada ou rejeitada:**  
Uma das sugestões foi usar análise de valor limite na pesquisa. Não usei porque a busca é por texto e não tem um número mínimo ou máximo para testar os limites. O que existe são grupos de termos, então o particionamento de equivalência fazia mais sentido.

**Como as respostas foram verificadas:**  
Conferi no LocalEats se as localizações e culinárias que usei nos casos existem mesmo, qual mensagem aparece quando não tem resultado, e se todo caso de teste está ligado a um risco na matriz.
