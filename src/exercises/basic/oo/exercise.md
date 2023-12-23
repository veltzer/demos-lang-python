# Object Oriented

Create two classes to match the data in the two input files: `cars.csv`, `people.csv`
One class will be called "Person" and the other "Car"
Read all the data from the csv files and create the appropriate instances.
Make sure that when given a car you can easily retrieve its owners.
Make sure that when given a person you can easily retrieve its cars.

## hints

* here is how to read a text file line by line and split it's lines according to some character (say ","):

```python
with open("file.csv", "rt") as stream:
    for line in stream:
        line=line.rstrip() # remove the newline at the end
        values = line.split(",")
```
