# Covidwrapper
## A Python Wrapper for The Coronavirus Covid19 API

Covidwrapper is a python wrapper for https://covid19api.com. It Includes functions that can simplify your code and access vasts amount of realtime covid19 data. For further details on covid19 API, check out their documentation at https://documenter.getpostman.com/view/10808728/SzS8rjbc?version=latest.

## Installation

Covidwrapper is available on the Python Package Index (PyPI) at https://pypi.python.org/pypi/covidwrapper.
You can install covidwrapper using one of the following techniques.

* Use Pip
```bash
pip install covidwrapper
```
* Clone the repo
```bash
git clone https://github.com/damildrizzy/covidwrapper.git
```
## Usage
Get a summary of new and total cases updated daily
```python
from covidwrapper import Covid
covid_summary = Covid.summary()
```
Get all the available countries and provinces, as well as the country slug for per country requests.
```python
from covidwrapper import Covid
covid_summary = Covid.countries()
```
Get cases by country
```python
from covidwrapper import Covid
nigeria = Covid('nigeria')
nigeria.cases_by_country()
```
This will return all confirmed cases in Nigeria. Optionally, you can add an extra parameter, 'deaths' or 'recovered'
to return all deaths or all recovered cases respectively
```python
nigeria_deaths = Covid('nigeria', 'deaths')
nigeria_recoveries = Covid('nigeria', 'recovered')
nigeria_deaths.cases_by_country()
nigeria_recoveries.cases_by_country()
```
