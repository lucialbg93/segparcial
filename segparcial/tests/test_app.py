#from app import index
import src.app as t
def test_index():
    assert t.index() == "Hola mundo"
