# Responsável: João Vítor Goes
import re

from playwright.sync_api import Page, expect

URL_LOCALEATS = "https://local-eats-unisenac.vercel.app/"


def test_alternar_para_formulario_de_criar_conta(page: Page):
    page.goto(URL_LOCALEATS)

    page.locator("#showRegisterBtn").click()

    # O <label> "Nome Completo" não está associado ao campo (sem "for"), por isso o placeholder.
    expect(page.get_by_placeholder("Seu nome")).to_be_visible()
    expect(page.get_by_role("button", name="Registrar")).to_be_visible()
    expect(page.locator("#loginForm")).to_be_hidden()


def test_meus_pedidos_sem_login_redireciona_para_login(page: Page):
    page.goto(URL_LOCALEATS + "static/orders.html")

    expect(page).to_have_url(re.compile(r"login\.html$"))
    expect(page.get_by_text("Bem-vindo ao app de Qualidade de Software")).to_be_visible()

    page.locator("#showLoginBtn").click()
    expect(page.get_by_placeholder("teste@teste.com")).to_be_visible()
