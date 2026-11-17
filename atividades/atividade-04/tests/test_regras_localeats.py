# Responsável: João Vítor Goes
import pytest

from src.regras_localeats import calcular_desconto


def test_pedido_de_150_recebe_desconto_de_15():
    assert calcular_desconto(150) == pytest.approx(15)


def test_pedido_abaixo_de_100_nao_recebe_desconto():
    assert calcular_desconto(80) == 0


@pytest.mark.parametrize(
    "valor_pedido, desconto_esperado",
    [(99.99, 0), (100, 10), (100.01, 10.001)],
)
def test_desconto_no_limite_de_100_reais(valor_pedido, desconto_esperado):
    assert calcular_desconto(valor_pedido) == pytest.approx(desconto_esperado)


def test_valor_negativo_gera_value_error():
    with pytest.raises(ValueError):
        calcular_desconto(-1)
