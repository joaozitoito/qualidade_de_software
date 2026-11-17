# Atividade 4: Testes Automatizados do LocalEats

---

## 1. Identificação

- **Turma:** Qualidade de Software
- **Modalidade:** individual
- **Repositório:** https://github.com/joaozitoito/qualidade_de_software
- **Diretório da atividade:** https://github.com/joaozitoito/qualidade_de_software/tree/main/atividades/atividade-04
- **Data da última execução:** 17/11/2026

### Integrantes

1. João Vítor Goes

---

## 2. Integrantes e responsabilidades

| ID | Integrante responsável | Tipo | Comportamento verificado | Arquivo e função de teste |
|---|---|---|---|---|
| TU01 | João Vítor Goes | Unitário | Pedido de R$ 150 tem desconto de R$ 15 | `tests/test_regras_localeats.py::test_pedido_de_150_recebe_desconto_de_15` |
| TU02 | João Vítor Goes | Unitário | Pedido abaixo de R$ 100 não tem desconto | `tests/test_regras_localeats.py::test_pedido_abaixo_de_100_nao_recebe_desconto` |
| TU03 | João Vítor Goes | Unitário | Valores perto do limite de R$ 100 | `tests/test_regras_localeats.py::test_desconto_no_limite_de_100_reais` |
| TU04 | João Vítor Goes | Unitário | Valor negativo gera ValueError | `tests/test_regras_localeats.py::test_valor_negativo_gera_value_error` |
| TF01 | João Vítor Goes | Funcional | Botão "Criar Conta" mostra o formulário de cadastro | `tests/test_localeats.py::test_alternar_para_formulario_de_criar_conta` |
| TF02 | João Vítor Goes | Funcional | Abrir "Meus Pedidos" sem login volta para a tela de login | `tests/test_localeats.py::test_meus_pedidos_sem_login_redireciona_para_login` |

---

## 3. Testes unitários

### Registro das regras implementadas

#### Regra de João Vítor Goes

- **Regra escolhida:** Regra 2, desconto do pedido
- **Função implementada:** `calcular_desconto(valor_pedido)`
- **Arquivo da implementação:** `src/regras_localeats.py`
- **Testes criados:** `test_pedido_de_150_recebe_desconto_de_15`, `test_pedido_abaixo_de_100_nao_recebe_desconto`, `test_desconto_no_limite_de_100_reais` e `test_valor_negativo_gera_value_error`
- **Comportamentos verificados:** pedido de 100 reais ou mais ganha 10% de desconto, pedido abaixo de 100 não ganha nada e valor negativo dá erro. A função devolve só o valor do desconto, não o total do pedido.

---

## 4. Aplicação do TDD

### TDD de João Vítor Goes

- **Regra escolhida:** Regra 2, desconto do pedido
- **Primeiro teste escrito:** `test_pedido_de_150_recebe_desconto_de_15`
- **Por que o teste falhou inicialmente:** a função ainda não existia, o arquivo `regras_localeats.py` estava vazio. O pytest deu `ImportError` ao tentar importar `calcular_desconto`.
- **Implementação mínima realizada:** criei a função só com `return valor_pedido * 0.10`, que já fazia o primeiro teste passar.
- **Segundo teste escrito:** `test_pedido_abaixo_de_100_nao_recebe_desconto`. Com a implementação mínima ele falhou (`assert 8.0 == 0`), porque a função dava desconto para qualquer valor. Coloquei um `if` para retornar 0 quando o pedido for menor que 100.
- **Melhoria ou refatoração realizada:** troquei os números 100 e 0.10 por constantes com nome, adicionei o `ValueError` para valor negativo e usei `pytest.approx` nas comparações com casas decimais, porque conta com float pode dar diferença de arredondamento.

---

## 5. Testes funcionais com Playwright

**Sistema:** https://local-eats-unisenac.vercel.app/

### Teste funcional de João Vítor Goes

- **ID:** `TF01`
- **Fluxo automatizado:** sair do formulário de login e ir para o de criar conta.
- **Interação realizada:** abrir o site (ele já abre na tela de login) e clicar em "Criar Conta".
- **Primeira assertion:** o campo "Seu nome" aparece na tela.
- **Segunda assertion:** o botão "Registrar" aparece na tela.
- **Terceira assertion:** o formulário de login some.
- **Arquivo e função:** `tests/test_localeats.py::test_alternar_para_formulario_de_criar_conta`
- **Resultado final:** aprovado

### Segundo teste funcional (opcional)

- **ID:** `TF02`
- **Fluxo automatizado:** tentar abrir "Meus Pedidos" sem estar logado.
- **Interação realizada:** abrir direto o endereço `static/orders.html` e, depois de cair na tela de login, clicar em "Entrar".
- **Primeira assertion:** o endereço da página termina em `login.html`.
- **Segunda assertion:** aparece o texto "Bem-vindo ao app de Qualidade de Software".
- **Terceira assertion:** depois do clique, aparece o campo de e-mail.
- **Arquivo e função:** `tests/test_localeats.py::test_meus_pedidos_sem_login_redireciona_para_login`
- **Resultado final:** aprovado

Não usei `time.sleep` em nenhum teste, o `expect` do Playwright já espera o elemento aparecer.

---

## 6. Resultado da execução

Rodei dentro da pasta `atividades/atividade-04/`:

```powershell
python -m pytest -v | Tee-Object -FilePath relatorio-pytest.txt
```

- **Quantidade total de testes:** 8 (o TU03 roda 3 vezes, um para cada valor)
- **Testes aprovados:** 8
- **Testes reprovados:** 0
- **Link para o relatório:** [relatorio-pytest.txt](relatorio-pytest.txt)
- **Observações:** Todos os testes foram aprovados. O aviso que aparece no final do relatório é do próprio plugin do Playwright, não dos meus testes.

Para instalar o que precisa antes de rodar:

```powershell
python -m pip install -r requirements.txt
python -m playwright install chromium
```

---

## 7. Explicações individuais

### Explicação do teste de João Vítor Goes

- **Teste escolhido:** `test_alternar_para_formulario_de_criar_conta` (TF01)
- **Comportamento verificado:** quando clico em "Criar Conta", o formulário de cadastro tem que aparecer no lugar do de login.
- **Dados ou estado inicial:** o navegador abre sem ninguém logado, então o site mostra a tela de login. Não precisa de conta nem senha.
- **Resultado esperado:** aparecer o campo "Seu nome" e o botão "Registrar", e o formulário de login ficar escondido. Para clicar no botão usei o id `#showRegisterBtn`, porque a tela tem dois botões escritos "Entrar" e pelo texto ficaria confuso.
- **O que faria o teste falhar:** o botão não trocar o formulário, os dois formulários aparecerem juntos, ou mudarem o texto do campo "Seu nome".

---

## 8. Uso de inteligência artificial

- **Ferramenta utilizada:** Claude (Anthropic), pelo Claude Code.
- **Como a ferramenta foi utilizada:** para ajudar a montar a estrutura do projeto, escrever a função e os testes seguindo o TDD, achar os locators do Playwright nas telas do LocalEats e revisar o texto.
- **Uma sugestão que precisou ser alterada ou rejeitada:** a primeira versão do TF01 procurava o campo pelo rótulo, com `get_by_label("Nome Completo")`, e o teste falhou. Troquei por `get_by_placeholder("Seu nome")`. Também desisti de automatizar a pesquisa com usuário logado.
- **Motivo da alteração ou rejeição:** no HTML do LocalEats o rótulo "Nome Completo" não está ligado ao campo, então o Playwright não acha o campo por ele. A pesquisa logada eu não fiz porque teria que deixar uma senha no código do repositório.
- **Como o código sugerido foi verificado:** rodei o pytest, conferi se todos os testes da tabela aparecem no relatório e olhei no site se os textos e botões usados nos testes existem mesmo.

---

## 9. Diferenciais opcionais

- [x] Terceiro teste unitário para caso de borda. (`test_desconto_no_limite_de_100_reais`)
- [x] Uso de `pytest.raises` para verificar exceção. (`test_valor_negativo_gera_value_error`)
- [x] Parametrização com `pytest.mark.parametrize`. (`test_desconto_no_limite_de_100_reais`)
- [ ] Cenário BDD em Gherkin.
- [ ] Automação com `pytest-bdd`.
- [ ] Organização com Page Object Model.
- [x] Segundo teste funcional pelo mesmo integrante. (`test_meus_pedidos_sem_login_redireciona_para_login`)
- [ ] Execução em mais de um navegador.
- [ ] Screenshot, vídeo ou trace do Playwright.
- [x] Registro de uma falha encontrada e corrigida.

### Descrição dos diferenciais

O TU03 testa os valores 99,99, 100 e 100,01, que ficam bem no limite da regra, usando `parametrize` para não repetir o mesmo teste três vezes. O TU04 usa `pytest.raises` para conferir que valor negativo dá `ValueError`. Os dois estão em `tests/test_regras_localeats.py`.

O TF02 é um segundo teste funcional, que confere que a página "Meus Pedidos" não abre sem login (`tests/test_localeats.py`).

**Falha encontrada e corrigida:** na primeira vez que rodei, o TF01 falhou dizendo que não encontrou o campo "Nome Completo", mesmo com o texto aparecendo na tela. Olhando a saída do Playwright, o campo aparecia só como "Seu nome". O motivo é que o `<label>` do formulário não está ligado ao `<input>` (falta o atributo `for`). Mudei o teste para achar o campo pelo placeholder e ele passou. Isso também é um problema de acessibilidade do LocalEats, porque um leitor de tela não vai ler o nome do campo para o usuário.
