"""
A basic demo of how to download urls off the web.

References:
http://stackoverflow.com/questions/22676/how-do-i-download-a-file-over-http-using-python
"""

import urllib.request
import progressbar


def get_url(url, file):
    """
    A function to download a file and show progress report
    while doing it
    """
    with open(file, 'wb') as f, urllib.request.urlopen(url) as u:
        meta = u.info()
        file_size = int(meta['Content-Length'])
        block_sz = 8192

        maxval = file_size // block_sz
        if file_size % block_sz > 0:
            maxval += 1

        pbar = progressbar.ProgressBar(maxval=maxval)
        pbar.start()
        while True:
            buffer = u.read(block_sz)
            if not buffer:
                break
            f.write(buffer)
            pbar.update(pbar.currval + 1)
        pbar.finish()


url1 = 'http://images.iskysoft.com/mac-itube-studio/main.jpg'
file1 = '/tmp/downloaded.jpg'

# this is the first way to do it...
urllib.request.urlretrieve(url1, file1)

url2 = 'http://download.ted.com/talks/DavidCameron_2010-480p.mp4'
file2 = '/tmp/tmp.mp4'

get_url(url2, file2)
