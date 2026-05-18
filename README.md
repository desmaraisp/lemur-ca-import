# lemur-ca-import

A [Lemur](https://github.com/netflix/lemur) plugin that allows users to import existing CA certificates into the system, which can then be used to issue certificates without interacting with remote systems.

## Installation

Install from PyPI:

```bash
pip install lemur-ca-import
```

Or from source in development mode:

```bash
pip install -e .
```

With test dependencies:

```bash
pip install -e '.[tests]'
```

## Testing

Run the test suite:

```bash
python -m pytest
```

## Building

Build distributions locally:

```bash
python -m build
```

This generates both sdist and wheel in `dist/`.

To control the package version, set the `CA_IMPORTER_VERSION` environment variable:

```bash
CA_IMPORTER_VERSION=1.2.3 python -m build
```

## Publishing

The package uses GitHub Actions for automated CI/CD:

- **PR builds** (`.github/workflows/pr-build.yml`): Tests and builds on each PR targeting `main`. Artifacts are uploaded and linked in the PR.
- **Release publishing** (`.github/workflows/release.yml`): Tests, builds, and publishes to PyPI on each GitHub release. Uses OIDC trusted publishing (no long-lived tokens).

## Usage

The `CAImporterPlugin` is registered as a Lemur issuer plugin via entry point `ca_importer`. Configure it in Lemur by providing:

- **public_certificate**: External CA certificate in PEM format
- **private_key**: External CA private key in PEM format

The plugin creates an authority bound to the imported CA certificate and generates admin/operator roles.

