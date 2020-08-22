import pkgutil, importlib
import p

def show_pkg(pkg):
    for f, n, ispkg in pkgutil.iter_modules(pkg.__path__):
        print('{}, {}, {}'.format(f,n,ispkg))
        fn = pkg.__name__ + '.' + n
        # 不主动调用则不会被加载。
        m = importlib.import_module(fn)
        if ispkg:
            show_pkg(m)


show_pkg(p)

print(p.__loader__.is_package(p.__name__))
