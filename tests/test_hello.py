import pytest

from hello import suma

    def test_suma_10():
        assert(suma(6) == 6)

    def test_suma_20():
        assert(suma(7) != 6)
