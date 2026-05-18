import pytest
from flask import Flask
from lemur_ca_importer import plugin

def test_create_authority_returns_expected_roles():
    app = Flask('test')
    with app.app_context():
        options = {
            "name": "test",
            "plugin": {
                "plugin_options": [
                    {"name": "public_certificate", "value": "-----BEGIN CERTIFICATE-----FAKE"},
                    {"name": "private_key", "value": "FAKE"}
                ]
            }
        }
        pub, key, chain, roles = plugin.CAImporterPlugin().create_authority(options)

        assert pub is not None
        assert pub.startswith("-----BEGIN CERTIFICATE-----")
        assert chain is None
        assert key is not None
        assert key is "FAKE"
        assert roles[0]["name"] == "test_admin"
        assert roles[1]["name"] == "test_operator"

def test_get_plugin_options_valid():
    options = {"plugin": {"plugin_options": [1, 2, 3]}}
    result = plugin.get_plugin_options(options)
    assert result == [1, 2, 3]

def test_get_plugin_options_invalid():
    options = {"plugin": {}}
    app = Flask('test')
    with app.app_context():
        with pytest.raises(plugin.InvalidConfiguration):
            plugin.get_plugin_options(options)

def test_get_option_pub_cert():
    opts = [
        {"name": "public_certificate", "value": "CERTDATA"},
        {"name": "other", "value": "X"}
    ]
    result = plugin.get_option(opts, "public_certificate")
    assert result == "CERTDATA"


def test_get_option_pub_cert_throws():
    opts = []
    app = Flask('test')

    with app.app_context():
        with pytest.raises(plugin.InvalidConfiguration):
            plugin.get_option(opts, "public_certificate")
