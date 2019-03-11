from fromconf import FromConf, field


class Base(FromConf):
    def message(self):
        raise NotImplementedError


class A(Base):
    x = field(int, invariant=lambda x: (x % 2 == 0, 'No odd numbers'))

    def message(self):
        return 'even int {}'.format(self.x)


class B(Base):
    y = field(str)

    def message(self):
        return ''.join(reversed(self.y))


if __name__ == '__main__':
    for conf in [{'x': 10010}, {'y': 'abc'}]:
        base = Base.from_conf(conf)
        print('Conf {} makes {} with message "{}"'.format(
            conf, base, base.message(),
        ))
