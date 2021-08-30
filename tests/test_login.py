from api import tuto
import os
import tempfile
import pytest

@pytest.fixture
def client():
    db_fd, tuto.app.config['DATABASE'] = tempfile.mkstemp()
    tuto.app.config['TESTING'] = True

    with tuto.app.test_client() as client:
        with tuto.app.app_context():
            tuto.init_db()
        yield client

    os.close(db_fd)
    os.unlink(tuto.app.config['DATABASE'])

def test_login():
    rv = client.get('/login')
    assert b'You are trying to log in' in rv.data
