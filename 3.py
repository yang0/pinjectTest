import pinject

class ClassWithTediousInitializer(object):
    @pinject.copy_args_to_internal_fields
    def __init__(self, foo, bar, baz, quux):
        print(self._foo)

cwti = ClassWithTediousInitializer('a-foo', 'a-bar', 'a-baz', 'a-quux')
print(cwti._foo)

#  自动拷贝参数，参数名前面会加下划线。如果想要没有下划线，可以用：@copy_args_to_public_fields