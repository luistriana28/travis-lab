#!/usr/bin/python

suma = 2 + 4

def resultado(suma):
    if suma == 6:
        return "la suma es correcta"
    else:
        return "la suma es:" + str(suma)
    return suma

def test_suma():
    assert resultado(7) != 6