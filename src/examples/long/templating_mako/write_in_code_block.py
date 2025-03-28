""" write_in_code_block.py """

import mako.template

input_filename = "src/examples/long/templating_mako/write_in_code_block.mako"
output_filename = "/tmp/write_in_code_block"

template = mako.template.Template(filename=input_filename)
output = template.render()
with open(output_filename, "w") as file_handle:
    file_handle.write(output)
