# Noisy Secrets

A Noisy Secret is a bearer credential that is easy to detect when leaked. It contains checksums, so it can be validated offline, and an optional namespace identifying the issuer.

```python
import noisysecrets

secret = noisysecrets.create(b"example.org")
noisysecrets.verify(secret)  # True
```

`verify` checks only the format and the checksums. It does not tell you that a secret was issued by you, and must not be used on its own to authenticate anyone.

This package implements the [draft Noisy Secrets specification](https://tooling.apache.org/noisy-secrets.html). It is licensed under the Apache License 2.0.
