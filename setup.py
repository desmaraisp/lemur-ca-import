import os
from setuptools import setup

package_version = os.environ.get("CA_IMPORTER_VERSION")

setup(
  version=package_version if package_version else "0.0.1"
)
