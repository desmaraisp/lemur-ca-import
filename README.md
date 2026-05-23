# lemur-plugins

This repo contains two different [Lemur](https://github.com/netflix/lemur) plugins:

- `lemur-ca-import`: allows users to import existing CA certificates into Lemur, which can then be used to issue certificates without interacting with remote systems. Useful if you want to migrate your internal CA to Lemur without disrupting your current process.

- `lemur-manual-issuer-plugin`: allows lemur to issue CSRs for certificates which can't be renewed automatically. The plugin then allows you to import the CA's response to complete the cert, after which point the certificate's lifecycle is managed by Lemur as usual. This is useful if you've got a legacy cert management process that requires sending CSRs to a third party CA owner which doesn't offer automated access

## Usage

Both plugins offer more specific documentation on installation and usage in their scoped README

|   |   |   |
|---|---|---|
| lemur-ca-import | [docs](src/lemur_ca_import/README.md) | [package](https://pypi.org/project/lemur-ca-import/) |
| lemur-manual-issuer-plugin | [docs](src/lemur_manual_issuer_plugin//README.md) | [package](https://pypi.org/project/lemur-manual-issuer-plugin/) |
| lemur-plugin-utils | [docs](src/lemur_plugin_utils/README.md) | [package](https://pypi.org/project/lemur-plugin-utils/) |

## Prerequisites

This repo uses [mise](https://mise.jdx.dev/) and [uv](https://mise.jdx.dev/) to manage its dependencies. As such, you only need two commands to set up the project deps:

```bash
mise install
uv sync --all-packages --all-groups
```

## Testing

A simple `uv run pytest` will run the tests across all packages.

## Building

It's possible to manually build the packages with `uv build --all-packages`, but this won't set the various package versions properly. There's a bit of a trick to it, as both plugins depend on a core utils package, and the versions move in lockstep. That's why the repo builds a version of the packages on every PR to make testing a little easier.

## Publishing

The package uses GitHub Actions for automated publishing to pypi.org. On every release, each package is automatically published with the release's version number. The plugins' dependencies are automatically updated to the current version.

