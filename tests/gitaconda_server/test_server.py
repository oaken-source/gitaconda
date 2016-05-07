
def test_hello(pyramid_server):
    res = pyramid_server.get('/', status=200)
    assert b'Hello!' in res.body
