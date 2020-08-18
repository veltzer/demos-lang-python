"""
An example of reading parquet files with 'fastparquet'.

References:
- https://github.com/dask/fastparquet
"""

from fastparquet import ParquetFile

# pf = ParquetFile('/tmp/file.parquet')
pf = ParquetFile('/tmp/file_compressed.parquet')
df = pf.to_pandas()
print(df)
