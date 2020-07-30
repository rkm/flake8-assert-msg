[![Build Status](https://dev.azure.com/ruairidh/flake8-assert-msg/_apis/build/status/rkm.flake8-assert-msg?repoName=rkm%2Fflake8-assert-msg&branchName=master)](https://dev.azure.com/ruairidh/flake8-assert-msg/_build/latest?definitionId=1&repoName=rkm%2Fflake8-assert-msg&branchName=master)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/flake8-assert-msg)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)
![PyPI - License](https://img.shields.io/pypi/l/flake8-assert-msg)
![PyPI](https://img.shields.io/pypi/v/flake8-assert-msg)

# flake8-assert-msg

flake8 plugin which forbids assert statements without messages.

## Installation

`pip install flake8-assert-msg`

## flake8 codes

| Code   | Description             |
| ------ | ----------------------- |
| ASS001 | do not use bare asserts |

## Rationale

This ensures that assertions have clear messages for failures. Adding a message to an assertion also acts as documentation for why the assertion is present.

## As a pre-commit hook

See [pre-commit](https://github.com/pre-commit/pre-commit) for instructions

Sample `.pre-commit-config.yaml`:

```yaml
- repo: https://gitlab.com/pycqa/flake8
  rev: 3.8.1
  hooks:
      - id: flake8
        additional_dependencies: [flake8-assert-msg==1.1.1]
```

## Acknowledgements

-   https://github.com/asottile/flake8-walrus used as a template
