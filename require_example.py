from fromconf import FromConf, require


class Base(FromConf):
    def message(self):
        raise NotImplementedError


@require(x='foo')
class A(Base):
    def message(self):
        return 'one thing'


@require(x='bar')
class B(Base):
    def message(self):
        return 'another thing'


if __name__ == '__main__':
    for conf in [{'x': 'foo'}, {'x': 'bar'}]:
        base = Base.from_conf(conf)
        print('Conf {} makes {} with message "{}"'.format(
            conf, base, base.message(),
        ))
