import pkgutil, importlib
import p

def show_pkg(pkg):
    for f, n, ispkg in pkgutil.iter_modules(pkg.__path__):
        print('{}, {}, {}'.format(f,n,ispkg))
        fn = pkg.__name__ + '.' + n
        if ispkg:
            # 不主动调用则不会被加载。
            m = importlib.import_module(fn)
            show_pkg(m)


show_pkg(p)
