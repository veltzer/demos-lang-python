"""
An example of writing parquet files with 'fastparquet'.

References:
- https://github.com/dask/fastparquet
"""

import pandas
from fastparquet import write

df = pandas.read_csv("/etc/passwd", sep=":")

# this is uncompressed write (I think!)
write('/tmp/file.parquet', df)
# this is compressed write
write('/tmp/file_compressed.parquet', df, compression='GZIP', file_scheme='hive')
