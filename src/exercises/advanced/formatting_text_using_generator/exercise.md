# Formatting Text Using Generator

Your task is to reformat paragraphs in a text stream.
Your input will be an iterator of lines.
Your output shall also be an iterator of lines.
Paragraphs in this exercise are delimited by empty lines.
They should be reformatted using textwrap.wrap with default settings.

Hint: use a pipeline of several stages.

Debugging hint:

```python
print(list(reformat(['foo', 'bar', '', 'long', 'encyclopedia'])))
```
