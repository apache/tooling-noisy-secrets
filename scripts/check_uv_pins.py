# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

import pathlib
import re
import sys
import tomllib
from typing import Final

_SETUP_UV: Final = re.compile(r"uses: astral-sh/setup-uv@[0-9a-f]{40}[^\n]*\n\s+with:\n\s+version: \"([0-9.]+)\"")


def main() -> None:
    versions = set()
    workflows = pathlib.Path(".github/workflows")
    for workflow in sorted([*workflows.glob("*.yml"), *workflows.glob("*.yaml")]):
        text = workflow.read_text()
        pinned = _SETUP_UV.findall(text)
        if text.count("astral-sh/setup-uv@") != len(pinned):
            sys.exit(f"ERROR: {workflow}: every setup-uv step must pin a uv version directly after with:")
        versions.update(pinned)
    if len(versions) != 1:
        sys.exit(f"ERROR: the workflows must all pin the same uv version, not {sorted(versions)}")
    version = versions.pop()
    major, minor, _ = version.split(".")
    expected = [f"uv_build>={version},<{major}.{int(minor) + 1}"]
    requires = tomllib.loads(pathlib.Path("pyproject.toml").read_text())["build-system"]["requires"]
    if requires != expected:
        sys.exit(f"ERROR: pyproject.toml build requirement must be {expected}, not {requires}")


if __name__ == "__main__":
    main()
