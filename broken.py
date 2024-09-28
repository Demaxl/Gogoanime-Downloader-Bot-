import os
import re
from pprint import pprint

# os.chdir('C:\Program Files (x86)\Internet Download Manager')


def download(link):
    folder = r'D:\Videos\download'
    command = fr'idman /n /p "{folder}" /d "{link}"'
    os.system(command)


def num(eps):
    try:
        epsnum = re.search(r'e-([\d]+)', eps)
        return int(epsnum.group(1))
    except AttributeError:
        epsnum = re.search(r'EP\.(\d+)\.', eps)
        return (int(epsnum.group(1)))


if __name__ == "__main__":
    start = 235
    end = 250

    animes_path = r"D:\Videos\download"

    videos = [num(vid) for vid in os.listdir(
        animes_path) if vid.endswith("mp4")]

    redownload = [eps for eps in range(start, end+1) if eps not in videos]

    print(redownload)
    # print(sorted(videos))
    # for eps in range(start, end+1):
    #     if eps not in videos:
    #         print(eps)
