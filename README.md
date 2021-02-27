# flake8-ensure-ascii

Ensure that python code files does not contains UTF-8 or
other fancy char encoding.

This module provides a plugin for `flake8`, the Python code checker.

## Installation

Install with pip:

```bash
pip install flake8-ensure-ascii
```

The plugin officially supports Python `>= 3.6` and `flake8 >= 3.7`.
You may find other Python 3 versions work as well.

## Usage

The plugin finds non ASCII chars you may not want to commit:

```python
def my_function():
    print("It works 😋")
```

```log
./my_file.py:2:21: ENC100 Non ASCII encoding found
```

## Changelog

### 1.0.0

#### Breaking changes

Initial commit !
