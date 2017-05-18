from __future__ import print_function
import requests
import shutil


def _dwnld(u, i):
    _fna = u.split("/")[-1]
    print("[" + str(i) + "] Downloading : " + _fna)
    _r = requests.get(u, stream=True)
    with open(_fna, 'wb') as _o:
        shutil.copyfileobj(_r.raw, _o)
    del _r


def main():
    l = 1
    while 1:
        url = "http://www.espncricinfo.com/ci/content/image/data/index.json?page=" + str(l) + ";object=6;search=dhoni;"
        k = requests.get(url).json()
        if len(k) != 0:
            for _i in k:
                _dwnld(str("http://p.imgci.com" + str(_i['fullpath'])), l)
                l += 1
        else:
            return


if __name__ == '__main__':
    main()
