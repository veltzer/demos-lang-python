#! /usr/bin/python
# SharePrices.py for QAPYTH3.
# CBD October 2011.
import time
import random

share_prices = {'Global Motors': 50,
                'Big Blue Inc.': 50,
                'Gates Software': 50,
                'Banana Computers': 50
                }

# Update stock prices with random price changes.

while True:
    for key, sp in share_prices.items():
        share_prices[key] = max(1.0, sp
                                * (1 + ((random.random() - 0.5)
                                / 0.5) * 0.05))
        print("{:<18s} ${:05.2f}".format(key, share_prices[key]))

    print()
    time.sleep(2)

            
 
