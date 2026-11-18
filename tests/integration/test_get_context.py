# pylint: disable=missing-module-docstring missing-function-docstring
import base64
import json
import os
from urllib.parse import urlparse

import pytest
from dotenv import load_dotenv

from ..ctx import get_ipython_shell

load_dotenv()


def _decode_jwt_payload(jwt):
    _, payload, _ = jwt.split('.')
    decoded = base64.b64decode(payload + '=' * (4 - len(payload) % 4))
    return json.loads(decoded.decode('utf-8'))


@pytest.fixture(name="ipython_shell", scope="module")
def fixture_ipython_shell():
    return get_ipython_shell()


def test_get_context_success(ipython_shell):
    # Arrange
    access_token = os.getenv('ACCESS_TOKEN')
    jwt_payload = _decode_jwt_payload(access_token)
    issuer = urlparse(jwt_payload['iss'])
    line = f'get-context --jwt {access_token}'

    # Act
    context = ipython_shell.run_line_magic('cluedin', line)

    # Assert
    assert context.protocol == issuer.scheme
    assert context.domain == '.'.join(issuer.hostname.split('.')[1:])
    assert context.org_name == jwt_payload['ClientId']
    assert context.access_token == access_token
