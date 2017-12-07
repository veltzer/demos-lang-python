This example shows how re-import code in python on the fly.

*** warning ***
This has many unexpected side effects
*** warning ***

Notes:
- if a is importing b and you re-import a you *do not* import b.
This is fine for most cases. If you want to re-import b then you
have to issue a re-import statement for it to, yourself.
