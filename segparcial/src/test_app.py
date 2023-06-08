#from app import index
import src.app as app
def test_index():
    assert app.index() == "Hola mundo"
