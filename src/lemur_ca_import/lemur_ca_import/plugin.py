from typing import Tuple

from flask import current_app

from lemur.common.utils import check_validation
from lemur.plugins.lemur_cryptography import plugin as lemur_cryptography
import lemur_ca_import as lemur_ca_import
from lemur_plugin_utils.utils import get_option, get_plugin_options


class CAImporterPlugin(lemur_cryptography.CryptographyIssuerPlugin):
    title = "CA Importer"
    slug = "ca-importer"
    description = "Enables the import of existing CA certificates into Lemur."
    version = lemur_ca_import.VERSION
    author = lemur_ca_import.AUTHOR
    author_url = lemur_ca_import.URL

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
