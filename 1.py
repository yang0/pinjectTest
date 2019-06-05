import pinject

class OuterClass(object):
     def __init__(self, inner_class):
         self.inner_class = inner_class

class InnerClass(object):
    def __init__(self):
        self.forty_two = 42

obj_graph = pinject.new_object_graph()
outer_class = obj_graph.provide(OuterClass)
print(outer_class.inner_class.forty_two)

# pinject 自动把inner_class翻译成了InnerClass，然后实例化了一个给outerClass
# 那么如果要传入不同的InnerClass该怎么操作呢
# 是否可以通过字符串来注入和反射呢