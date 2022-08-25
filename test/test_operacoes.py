import pytest
import numpy as np
from matematica.Calculadora import soma,sub,multiplicacao,divisao,media_lista_valores

@pytest.mark.op_simples
def test_soma_dois_valores_positivos():
    v1 = 5.0
    v2 = 10.0
    assert 15 == soma(v1,v2)

@pytest.mark.op_simples
def test_sub_dois_valores_positivos():
    v1 = 5
    v2 = 15 
    assert -10 == sub(v1,v2)

@pytest.mark.op_simples
def test_multiplicacao_dois_valores_positivos():
    v1 = 2
    v2 = 3
    assert 6 == multiplicacao(v1,v2)

@pytest.mark.exercicio_1
@pytest.mark.op_simples
def test_divisao_por_zero():
    v1 = 6
    v2 =0 
    assert np.inf == divisao(v1,v2)

@pytest.mark.exercicio_1
@pytest.mark.op_complexas
def test_media_lista_com_lista_vazia():
    lista = []
    assert 0 == media_lista_valores(lista)

@pytest.mark.exercicio_1
def test_media_lista_com_valor_string():
    lista = ['arroz','3',4,5,6,65]
    assert 20 == media_lista_valores(lista)
