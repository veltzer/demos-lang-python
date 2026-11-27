"""
This is an example that shows all EXIF fields that the ExifRead python module knows.
"""

import exifread
import exifread.tags.exif

# print(dir(exifread))  # noqa: ERA001  teaching: kept in the comment for the reader
# print(dir(exifread.tags))  # noqa: ERA001  teaching: kept in the comment for the reader
# print(dir(exifread.tags.fields))  # noqa: ERA001  teaching: kept in the comment for the reader
# print(dir(exifread.tags.exif))  # noqa: ERA001  teaching: kept in the comment for the reader
# print(type(exifread.tags.EXIF_TAGS))  # noqa: ERA001  teaching: kept in the comment for the reader
# print(exifread.tags.EXIF_TAGS)  # noqa: ERA001  teaching: kept in the comment for the reader
for v in exifread.tags.exif.EXIF_TAGS.values():
    print(v[0])
    # print(k, v)  # noqa: ERA001  teaching: kept in the comment for the reader
