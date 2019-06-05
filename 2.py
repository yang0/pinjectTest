import pinject

class SomeClass(object):
    def __init__(self, foo):
        self.foo = foo

class Foo(object):
    def test(self):
        print('222')

obj_graph = pinject.new_object_graph(modules=None, classes=[SomeClass])
# obj_graph.provide(SomeClass)  # would raise a NothingInjectableForArgError
obj_graph = pinject.new_object_graph(modules=None, classes=[SomeClass, Foo])
some_class = obj_graph.provide(SomeClass)

some_class.foo.test()

# modules可以指定去哪里搜索要注入的class，classes这个数组可以指定一串要注入的类名
# modules默认情况下会去搜索所有的import的模块