
def test_hello_set(pyramid_server):
    res = pyramid_server.get('/hello/john/smith', status=200)
    assert b'name: john smith' in res.body

def test_hello_postset(pyramid_server):
    res = pyramid_server.get('/hello', status=200)
    assert b'name: john smith' in res.body
