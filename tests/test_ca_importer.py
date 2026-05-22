from flask import Flask
from lemur_ca_import import plugin


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

