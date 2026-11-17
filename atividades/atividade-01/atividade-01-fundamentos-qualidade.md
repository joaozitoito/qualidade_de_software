# Atividade 1: Fundamentos e Características da Qualidade no LocalEats

## 1. Identificação

**Turma:** Qualidade de Software  
**Equipe:** Individual  
**Data:** 17/11/2026

### Integrantes

| Nome | Usuário no GitHub |
|---|---|
| João Vítor Goes | @joaozitoito |

**Elemento de Competência:** Compreender os fundamentos de qualidade de software e sua aplicação no desenvolvimento de sistemas.

**Aplicação:** <https://local-eats-unisenac.vercel.app/>

---

## 2. Tarefa 1: Fundamentos da qualidade

### 2.1 Necessidades explícitas e implícitas

| Tipo | Necessidade | Interessado | Consequência se não for atendida |
|---|---|---|---|
| Explícita | Pesquisar restaurantes por culinária ou por localização (é o que diz o próprio campo de busca) | Usuário | O usuário não acha o tipo de comida que quer e acaba desistindo do app |
| Explícita | Fazer um pedido e depois conseguir ver ele em "Meus Pedidos" | Usuário e restaurante | O usuário fica sem saber se o pedido foi feito e o restaurante pode perder a venda |
| Implícita | Os dados da conta precisam estar protegidos, um usuário não pode ver os pedidos ou favoritos de outro | Usuário e a empresa | Vazamento de dados pessoais, o usuário perde a confiança no app e a empresa pode ter problema com a LGPD |
| Implícita | Os textos e botões precisam ser fáceis de ler, com contraste bom | Usuário, principalmente quem enxerga pouco | O usuário não percebe o botão de busca e tem dificuldade de usar o app |

### 2.2 Questão sobre os fundamentos da qualidade

**Um sistema que implementa todas as funcionalidades explicitamente solicitadas pode, ainda assim, apresentar baixa qualidade? Justifiquem utilizando pelo menos uma necessidade implícita identificada pela equipe.**

Pode sim. Qualidade não é só ter as funcionalidades pedidas, é também atender o que o usuário espera mesmo sem estar escrito. No LocalEats, por exemplo, a busca pode funcionar, mas se o botão "Buscar" tiver um contraste tão ruim que a pessoa nem enxerga direito, a funcionalidade existe mas não é bem usada. Ninguém pediu "o botão tem que ser legível", mas todo usuário espera isso.

---

## 3. Tarefa 2: Exploração da aplicação

| Integrante | Funcionalidade | O que foi realizado | O que foi observado | Evidência |
|---|---|---|---|---|
| João Vítor Goes | Pesquisar restaurantes por especialidade ou localização | Uso esperado: entrei no sistema, deixei o filtro em "Todos", digitei `centro` no campo de busca e cliquei em "Buscar". Uso alternativo: fiz a mesma coisa digitando `italiana`, já que o campo diz que dá para buscar por culinária. | Com `centro` apareceram os restaurantes do Centro (Restaurante Sabor 1, que é Japonesa, Sabor 7, que é Italiana, e Sabor 9, que é Mexicana). Com `italiana` não apareceu nenhum restaurante, só a mensagem "Nenhum restaurante encontrado.", mesmo existindo restaurante italiano (o Sabor 7 apareceu como Italiana na busca por centro). Ou seja, a busca funcionou pela localização, mas não pela culinária. | [ver evidência (centro)](evidencias/joao-vitor-pesquisa-localizacao-centro.webp), [ver evidência (italiana)](evidencias/joao-vitor-pesquisa-especialidade-italiana.png) |

---

## 4. Tarefa 3: Requisitos e características de qualidade

| Integrante | Requisito de Qualidade | Característica ou subcaracterística | Justificativa | Como avaliar |
|---|---|---|---|---|
| João Vítor Goes | Quando o usuário pesquisar uma culinária ou uma localização que existe no sistema (por exemplo "Italiana" ou "Centro"), devem aparecer todos os restaurantes que combinam com o termo, e só eles. | Adequação funcional, subcaracterística correção funcional | A busca existe, então o problema não é falta de funcionalidade, e sim o resultado estar errado. Na minha exploração, a busca por "italiana" não trouxe nada mesmo tendo restaurante italiano. Também dá para pensar em usabilidade, porque o campo promete algo que não faz, mas o principal problema é o resultado incorreto. | Fazer uma lista com todas as culinárias e localizações que aparecem no site, pesquisar cada uma e comparar os restaurantes que aparecem com os que deveriam aparecer. Depois contar quantas pesquisas deram o resultado certo do total. |

---

## 5. Uso de inteligência artificial

**Ferramenta utilizada:**  
Claude (Anthropic), pelo Claude Code.

**Como foi utilizada:**  
Usei para ajudar a organizar as tabelas, dar ideias de necessidades implícitas e revisar o texto da justificativa.

**Como as respostas foram verificadas:**  
Fiz as pesquisas no próprio LocalEats, tirei os prints e conferi se o que estava escrito na tabela era o que aconteceu na tela. A característica escolhida eu comparei com o modelo da ISO/IEC 25010 que vimos em aula.
