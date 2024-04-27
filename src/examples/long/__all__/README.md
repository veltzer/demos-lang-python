# `__all__`

This example shows how you can use the reserved symbol `__all__`
to restrict which symbols of your module will not be injected
into the users namespace when he will use the

```python
from [module_name] import *
```

syntax.

The `__all__` does not effect other types of import like

```python
import [module_name]
```

or

```python
from [module_name] import [symbol1], [symbol2], ...
```
