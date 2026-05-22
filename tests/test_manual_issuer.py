from flask import Flask
from lemur_manual_issuer_plugin import plugin

def test_create_certificate_returns_pending():
    p = plugin.ManualIssuerPlugin()
    app = Flask('test')
    with app.app_context():
        cert, chain, external_id = p.create_certificate(None, {})
        assert cert == ""
        assert chain == ""
        assert isinstance(external_id, int)

def test_create_authority_returns_expected_roles():
    app = Flask('test')
    with app.app_context():
        options = {
            "name": "test",
            "plugin": {
                "plugin_options": [
                    {"name": "public_certificate", "value": "-----BEGIN CERTIFICATE-----FAKE"}
                ]
            }
        }
        pub, chain, key, roles = plugin.ManualIssuerPlugin().create_authority(options)

        assert pub is not None
        assert pub.startswith("-----BEGIN CERTIFICATE-----")
        assert chain is None
        assert key is None
        assert roles[0]["name"] == "test_admin"
        assert roles[1]["name"] == "test_operator"
