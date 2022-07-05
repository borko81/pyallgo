import os
from time import perf_counter
from threading import Thread

PATH = r'C:\Users\Borko\Desktop\pyallgo'


def walk(where):
    for root, dirname, files in os.walk(where):
        for file in files:
            p = root.split('\\')
            print('|', '-' * len(p) , '[' , os.path.join(root, file) , ']')


def trav_in_path(path):
    exclude = '.git .gitignore .idea venv'.split()
    search = [os.path.join(path, name) for name in os.listdir(path) if name not in exclude]
    for s in search:
        walk(s)
        # Thread(target=walk, args=(s,)).start()


if __name__ == '__main__':
    t1 = perf_counter()
    trav_in_path(PATH)
    print(perf_counter() - t1)
