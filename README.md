# Noisy Secrets

A Noisy Secret is a bearer credential that is easy to detect when leaked. It contains checksums, so it can be validated offline, and an optional namespace identifying the issuer.

```python
import noisysecrets

secret = noisysecrets.create(b"example.org")
noisysecrets.verify(secret)  # True
```

`verify` checks only the format and the checksums. It does not tell you that a secret was issued by you, and must not be used on its own to authenticate anyone.

This package implements the [draft Noisy Secrets specification](https://tooling.apache.org/noisy-secrets.html). It is licensed under the Apache License 2.0.

## Versions

Releases are numbered `0.0.N`, starting at `0.0.1`. Between releases, the version on `main` is that of the next release with `.dev0+dev` appended, such as `0.0.1.dev0+dev` before the first release. The `+dev` makes it a local version, which PyPI will not accept, so a build from source can never be published as a release. The `.dev0` makes it a pre-release, so installers that can see both choose the release.

Run `uv run prek install` once after cloning. Its hooks check these rules on every commit and push, along with the linters and tests, and CI checks them again on every push.
