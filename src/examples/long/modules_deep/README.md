This is a demo of how module initialization work.

things to note:

- order of initialization is from outside to the inside.
	if some folders in the hierarcy do not have an "__init__.py"
	file then those files just don't get called.

- you don't have to have a "__init__.py" file in every level of the hierarchy.
	You can actually not have this at *any* level of the hierarchy.
	However, it is the best practice to put a "__init__.py" file in *every*
	place in the hierarchy. 

- any "__init__.py" file is executed exactly once. You don't have to worry about that.
	Python does that all on its own.

- module usage is logical (import outer.inner.mod) instead of physical:
	outer/inner/mod.py. that is very good because:
	- you can write module loaders that load from other sources than
	the file system.
	- you can override file location using PYTHONPATH.
