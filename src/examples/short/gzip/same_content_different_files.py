"""
This example shows that two activations of the gzip library to compress files
actually produce files with different md5 signatures.

The reason for this is the filename, date and compression levels.
You can control this by adding the GzipFile object which has more
parameters. This is not yet demonstrated in this demo.

References:
- http://stackoverflow.com/questions/28213912/python-md5-hashes-of-same-gzipped-file-are-inconsistent
"""

import gzip
import hashlib

f_name = '/etc/passwd'
output_template = '/tmp/test{}.gz'
block_size = 4096


def digest(filename: str) -> str:
    md5 = hashlib.md5()
    with open(filename, 'rb') as f:
        for chunk in iter(lambda: f.read(block_size), b''):
            md5.update(chunk)
    return md5.hexdigest()


def main():
    print("The default way - non identical outputs")
    for x in range(0, 3):
        output_filename = output_template.format(x)
        with open(f_name, 'rb') as input_handle, gzip.open(output_filename, 'wb') as my_zip:
            # pylint: disable=cell-var-from-loop
            for chunk in iter(lambda: input_handle.read(block_size), b''):
                my_zip.write(chunk)
        print(digest(output_filename))

    print("The right way to get identical outputs")
    for x in range(3, 6):
        output_filename = output_template.format(x)
        with open(f_name, 'rb') as input_handle, open(output_filename, 'wb') as output_stream:
            my_zip = gzip.GzipFile(
                filename='',  # do not emit filename into the output gzip file
                mode='wb',
                fileobj=output_stream,
                mtime=0,  # do not emit modification time information into the output gzip file
            )
            for chunk in iter(lambda: input_handle.read(block_size), b''):
                my_zip.write(chunk)
        print(digest(output_filename))


main()
