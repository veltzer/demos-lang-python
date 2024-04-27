# Using `yapsy`

What do we learn from this example?
* that `yapsy` knows how to do recursion (see plugin3).
* that you must have descriptions of plugins (the .yapsy-plugin file)
plugins without this file will not be found (see plugin4).
* the standard yapsy interface had 'activate' and 'deactivate' APIs.
this seems reasonable.
You don't have to implement them when you define a plugin (see plugin1)
You can use both of them (see plugin5)
You can use just one of them (see plugin2, plugin3)
* you can design the API to the plugins in any way you see fit.

TODO
* show how to access the plugins name space and extract variables from there.
