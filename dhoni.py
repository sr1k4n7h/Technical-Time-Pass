from __future__ import print_function
import requests
import shutil

__author__ = 'sr1k4n7h'

# This script is the result of a request from my Cricket Crazy Friend 'Sai Veer'
# Fucntionality : Downloads all MS Dhoni pics from CricInfo Pictures Repo.

def _dwnld(u, i):
    _fna = u.split("/")[-1]
    print("[" + str(i) + "] Downloading : " + _fna)
    _r = requests.get(u, stream=True)
    with open(_fna, 'wb') as _o:
        shutil.copyfileobj(_r.raw, _o)
    del _r


def main():
    _c = 1
    while 1:
        url = "http://www.espncricinfo.com/ci/content/image/data/index.json?page=" + str(_c) + ";object=6;search=dhoni;"
        k = requests.get(url).json()
        if len(k) != 0:
            for _i in k:
                _dwnld(str("http://p.imgci.com" + str(_i['fullpath'])), _c)
                _c += 1
        else:
            return


if __name__ == '__main__':
    main()
