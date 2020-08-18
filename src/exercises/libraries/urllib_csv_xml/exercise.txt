Chapters 1-2: Text Processing / XML
===================================
Ex 1
Fetch the feed of fresh Python packages from http://pypi.python.org/pypi?:action=rss
[Hint: urllib.urlopen()]
Parse the <item> elements [for the exercise, use ElementTree or DOM, not dedicated RSS parsers].
Dump them into a CSV file with the following columns:
Date, Package, Version, Description
[Note: This feed has package and version together in the title field – you’ll have to separate them.]

Observe how the csv module used quotes around descriptions that contain commas.

Bonus Ex: cleanly separate parsing code from writing code.
