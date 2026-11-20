# Noisy Secrets

A Noisy Secret is a bearer credential that is easy to detect when leaked. It contains checksums, so it can be validated offline, and an optional namespace identifying the issuer.

```python
import noisysecrets

secret = noisysecrets.create(b"example.org")
noisysecrets.verify(secret)  # True
```

`verify` checks only the format and the checksums. It does not tell you that a secret was issued by you, and must not be used on its own to authenticate anyone.

This package implements the [draft Noisy Secrets specification](https://tooling.apache.org/noisy-secrets.html). It is licensed under the Apache License 2.0.

## Reporting issues

Report bugs at https://github.com/apache/tooling-noisy-secrets/issues.

**Do NOT report security vulnerabilities through public GitHub issues.** Please report security vulnerabilities to the Apache Security Team by emailing **security@apache.org**. This is a private mailing list. Please send one plain-text, unencrypted, email for each vulnerability you are reporting. For complete details on reporting and the process, see the [ASF Security Team](https://www.apache.org/security/) page.

## Versions

Releases are numbered `0.0.N`, starting at `0.0.1`. Between releases, the version on `main` is that of the next release with `.dev0+dev` appended, such as `0.0.1.dev0+dev` before the first release. The `+dev` makes it a local version, which PyPI will not accept, so a build from source can never be published as a release. The `.dev0` makes it a pre-release, so installers that can see both choose the release.

To release, run `sh scripts/phase.sh release` on an up to date `main`. It changes the version from `0.0.N.dev0+dev` to `0.0.N`, commits, tags that commit `v0.0.N`, and pushes the commit and the tag together. The upload waits until two members of ASF Tooling approve it at https://releases.apache.org/gates. Afterwards, run `sh scripts/phase.sh develop` to change the version to `0.0.(N+1).dev0+dev`, commit, and push.

Run `uv run prek install` once after cloning. Its hooks check these rules on every commit and push, along with the linters and tests, and CI checks them again on every push to `main` and every pull request.

## Keeping your branch up to date

`main` has no merge commits, which are the commits that `git merge` and a plain `git pull` make when they join two lines of work. GitHub refuses any push to `main` that contains one, and the checks fail on any pull request that contains one.

So never merge `main` into your branch. To catch up, move your commits on top of the latest `main`, then replace your branch on GitHub:

```shell
git pull --rebase origin main
git push --force-with-lease
```

The button on a pull request page that updates the branch merges by default, so if you use it, choose its rebase option instead. If you push to `main` directly, run `git config pull.rebase true` once, so that `git pull` never makes a merge commit.

The same two commands fix a pull request whose checks fail with "merge commits are not allowed, so rebase instead". They also fix one that was started during a release and fails the version check, once the release has finished.
