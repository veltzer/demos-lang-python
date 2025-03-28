""" minimal.py """

import mako.template

input_filename = "src/examples/long/templating_mako/minimal.mako"
output_filename = "/tmp/minimal"

template = mako.template.Template(filename=input_filename)
output = template.render(foo="bar")
with open(output_filename, "w") as file_handle:
    file_handle.write(output)
