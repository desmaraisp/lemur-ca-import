from lemur.exceptions import InvalidConfiguration
import pytest
from flask import Flask
from lemur_plugin_utils.utils import get_option, get_plugin_options


def test_get_plugin_options_valid():
    options = {"plugin": {"plugin_options": [1, 2, 3]}}
    result = get_plugin_options(options)
    assert result == [1, 2, 3]

def test_get_plugin_options_invalid():
    options = {"plugin": {}}
    app = Flask('test')
    with app.app_context():
        with pytest.raises(InvalidConfiguration):
            get_plugin_options(options)

def test_get_option_pub_cert():
    opts = [
        {"name": "public_certificate", "value": "CERTDATA"},
        {"name": "other", "value": "X"}
    ]
    result = get_option(opts, "public_certificate")
    assert result == "CERTDATA"

def test_get_option_pub_cert_throws():
    opts = []
    app = Flask('test')

    with app.app_context():
        with pytest.raises(InvalidConfiguration):
            get_option(opts, "public_certificate")
