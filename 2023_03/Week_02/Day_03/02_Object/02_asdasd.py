

def hello():
    return 'hello'


hello()


class user:
    a = 'aaa'

    # 인스턴스 메서드
    def hello():
        return 'hello'

    @classmethod
    def class_method(cls):

        return cls.a
