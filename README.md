# pytimeir

[![Python 3.6](https://img.shields.io/badge/python-3.6-blue.svg)](https://www.python.org/downloads/release/python-360/)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)

A simple package to get events and holidays from [time.ir](https://www.time.ir/)

## Getting Started

Install the package with:

```
pip install pytimeir
```

## Usage

```python
import pytimeir

# get holidays for a year
df = pytimeir.get_holidays(1401)

# get holidays for a range of years
df = pytimeir.get_holidays(1390, 1410)

# get events for a year
df = pytimeir.get_events(1401)

# get events for a range of years
df = pytimeir.get_events(1390, 1410)
```