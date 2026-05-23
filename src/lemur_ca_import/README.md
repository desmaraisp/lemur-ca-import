# lemur-ca-import

This [Lemur](https://github.com/netflix/lemur) plugin allows users to import existing CA certificates into Lemur, which can then be used to issue certificates without interacting with remote systems. Useful if you want to migrate your internal CA to Lemur without disrupting your current process or having to create a new CA.


## Parent documentation
Please refer to the parent project's [documentation](https://github.com/desmaraisp/lemur-plugins) for more information

## Installation
This can be installed with a simple `pip install lemur-ca-import`, though since it depends on Lemur, you'll need a couple of dependencies such as gcc

## Usage
Upon attempting to create a new Lemur Authority, selecting this plugin as source will allow you to import both the CA's public certificate and its private key. Once the certificate has been imported, you can then issue certificates as you would with the base `cryptography` plugin.
