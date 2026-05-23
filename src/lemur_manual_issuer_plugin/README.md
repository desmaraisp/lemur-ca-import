# lemur-manual-issuer-plugin

This [Lemur](https://github.com/netflix/lemur) plugin allows lemur to issue CSRs for certificates which can't be renewed automatically. The plugin then allows you to import the CA's response to complete the cert, after which point the certificate's lifecycle is managed by Lemur as usual. This is useful if you've got a legacy cert management process that requires sending CSRs to a third party CA owner which doesn't offer automated access


## Parent documentation
Please refer to the parent project's [documentation](https://github.com/desmaraisp/lemur-plugins) for more information

## Installation
This can be installed with a simple `pip install lemur-manual-issuer-plugin`, though since it depends on Lemur, you'll need a couple of dependencies such as gcc.

## Usage
Upon attempting to create a new Lemur Authority, selecting this plugin as source will allow you to import the CA's public certificate, but not its private key. This means that you can import an arbitrary third party CA's certificate into Lemur. Generating certificates with this authority will generate CSRs, which you can then send to your CA by whichever archaic process you'd like to use (pigeons, emails, butterfly-induced bit flips, etc.). Once the CA has processed your request, you can simply import the response in Lemur and carry on as usual.
