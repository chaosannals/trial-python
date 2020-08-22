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

def show_mod(mod):
    loader = mod.__loader__
    print(mod)
    if loader.is_package(mod.__name__):
        for _, n, _ in pkgutil.iter_modules(mod.__path__):
            fn = mod.__name__ + '.' + n
            m = importlib.import_module(fn)
            show_mod(m)

show_pkg(p)
print('-------------------------')
show_mod(p)