
def test_index(pyramid_server):
    res = pyramid_server.get('/', status=200)
    assert b'hello world' in res.body
