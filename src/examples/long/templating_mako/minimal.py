import datetime
import mako.template


def years(x):
    curr_year = datetime.datetime.now().year
    return ','.join(map(str, range(x, curr_year + 1)))


d = {
    'a': 'b',
    'c': 'd',
}

input_filename = 'src/examples/long/templating_mako/simple.mako'
output_filename = '/tmp/simple'

template = mako.template.Template(filename=input_filename)
output = template.render(foo='bar', years=years, d=d)
with open(output_filename, 'w') as file_handle:
    file_handle.write(output)
