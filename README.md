currencyNotifier
================

Simple Python script that suggests when to sell a currency pair.

This script lets you know when a certain currency reaches your selling cap. It also lets you set a floor value for your savings and returns your balance plus the estimated earnings.

*Notes: I made it for exercise purposes only. Didn't find a proper API so I managed to scrap this [Google Finance Converter](https://www.google.com/finance/converter) service using [BeautifulSoup](https://github.com/bdoms/beautifulsoup). Originally built for Bitcoin.*

Usage
-----

Install BeautifulSoup:

    $ pip install beautifulsoup


Configure a value for your initial savings:

    initialSavings = float(1)


Run the script:

    $ python currencyNotifier.py


To-Do
---
Still pending to make it run daily and notify via email.


Meta
----
Guido Sirna - [@guidosirna](https://twitter.com/guidosirna) - https://github.com/guidosirna/currencyNotifier
