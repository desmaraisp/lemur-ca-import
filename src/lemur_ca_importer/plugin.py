from typing import Tuple

from flask import current_app

from lemur.common.utils import check_validation
from lemur.exceptions import InvalidConfiguration
from lemur.plugins.lemur_cryptography import plugin as lemur_cryptography
import lemur_ca_importer


class CAImporterPlugin(lemur_cryptography.CryptographyIssuerPlugin):
    title = "CA Importer"
    slug = "ca-importer"
    description = "Enables the import of existing CA certificates into Lemur."
    version = lemur_ca_importer.VERSION

    options = [
        {
            "name": "public_certificate",
            "type": "textarea",
            "default": "",
            "required": True,
            "validation": check_validation("^-----BEGIN CERTIFICATE-----.*-----END CERTIFICATE-----$"),
            "helpMessage": "External CA public certificate in PEM format. This is used to build the certificate chain and is required when creating an authority.",
        },
        {
            "name": "private_key",
            "type": "textarea",
            "default": "",
            "required": True,
            "validation": check_validation("^-----BEGIN PRIVATE KEY-----.*-----END PRIVATE KEY-----$"),
            "helpMessage": "External CA private key in PEM format. With this, Lemur can sign certificates using the imported CA. This is required when creating an authority.",
        }
    ]

    author = lemur_ca_importer.AUTHOR
    author_url = lemur_ca_importer.URL

    @staticmethod
    def create_authority(options) -> Tuple[str, str, None, list]:
        """
        The authority created here is bound to a single user-provided CA certificate.

        :param options:
        :return:
        """
        current_app.logger.debug(
            f"Issuing new imported authority with options: {options}"
        )

        plugin_options = get_plugin_options(options)
        cert_pem = get_option(plugin_options, "public_certificate")
        private_key = get_option(plugin_options, "private_key")

        roles = [
            {"username": "", "password": "", "name": options["name"] + "_admin"},
            {"username": "", "password": "", "name": options["name"] + "_operator"},
        ]
        return cert_pem, private_key, None, roles

def get_plugin_options(options):
    plugin_options = options.get("plugin", {}).get("plugin_options")
    if not plugin_options:
        error = f"Invalid options for ca importer plugin: {options}"
        current_app.logger.error(error)
        raise InvalidConfiguration(error)
    return plugin_options

def get_option(plugin_options, option_name) -> str:
    for option in plugin_options:
        if option.get("name") == option_name:
            return option.get("value")

    error = f"Invalid options for ca importer plugin: {option_name}"
    current_app.logger.error(error)
    raise InvalidConfiguration(error)

