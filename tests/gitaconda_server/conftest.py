
from pyramid import testing
from webtest import TestApp
import pytest

from gitaconda_server import main


@pytest.fixture(scope='session')
def pyramid_testing_setup(request):
    def fin():
        testing.tearDown()
    request.addfinalizer(fin)
    return testing.setUp()


@pytest.fixture(scope='session')
def pyramid_server(pyramid_testing_setup):
    return TestApp(main({}))
