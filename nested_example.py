from fromconf import FromConf, field, PClass


class Base(FromConf):
    pass


class A(Base):
    x = field(int)


class B(Base):
    x = field(float)


class Nested(PClass):
    inner = field(Base)


if __name__ == '__main__':
    nested = Nested(inner=Base.create({'x': 100}))
    deser_nested = Nested.create(nested.serialize())
    print('{} == {} --> {}'.format(
        nested, deser_nested, nested == deser_nested,
    ))
