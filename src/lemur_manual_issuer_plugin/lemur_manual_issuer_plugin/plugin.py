from typing import Optional, Tuple
import uuid

from flask import current_app

from lemur.common.utils import check_validation
from lemur.plugins import IssuerPlugin
import lemur_manual_issuer_plugin as lemur_manual_issuer_plugin
from lemur_plugin_utils.utils import get_option, get_plugin_options


class ManualIssuerPlugin(IssuerPlugin):
    title = "Manual Issuer"
    slug = "manual-issuer"
    description = "Enables the creation and signing of certificates by hand, using third-party tools or services."
    version = lemur_manual_issuer_plugin.VERSION
    author = lemur_manual_issuer_plugin.AUTHOR
    author_url = lemur_manual_issuer_plugin.URL

    options = [
        {
            "name": "Public Certificate",
            "type": "textarea",
            "default": "",
            "required": True,
            "validation": check_validation("^-----BEGIN CERTIFICATE-----.*-----END CERTIFICATE-----$"),
            "helpMessage": "External CA public certificate in PEM format. This is used to build the certificate chain and is required when creating an authority.",
        }
    ]

    def create_certificate(self, csr, issuer_options) -> Tuple[str, str, int]:
        """
        Directly returns a pending certificate.

        :param csr:
        :param issuer_options:
        :return:
        """
        current_app.logger.debug(
            f"Issuing a pending cert to complete later: {issuer_options}"
        )
        return "", "", int(uuid.uuid4())

    def create_authority(self, options) -> Tuple[Optional[str], Optional[str], Optional[str], list]:
        """
        The authority created here is bound to a single user-provided CA certificate. Only the CA's public cert is requested.

        :param options:
        :return:
        """
        current_app.logger.debug(
            f"Issuing new manual authority with options: {options}"
        )

        plugin_options = get_plugin_options(options)
        public_cert = get_option(plugin_options, "Public Certificate")

        roles = [
            {"username": "", "password": "", "name": options["name"] + "_admin"},
            {"username": "", "password": "", "name": options["name"] + "_operator"},
        ]
        return public_cert, None, None, roles
