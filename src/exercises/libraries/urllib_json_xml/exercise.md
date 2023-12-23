# Urllib JSON and XML

Fetch [this](http://ws.geonames.org/hierarchyJSON?geonameId=2657896)
Parse this JSON and produce a nested XML showing the place of Zurich in the world:

```xml
<place name="Earth>
    <place name="Zurich />
</place>
```xml

Hint

* special-case the first element, loop over the rest.

* Don't worry about the ugly "Kanton [junk]". That's a bug of geonames.org - they should proper use Unicode in their JSON.
