from pytest import *
from account import *

class Test:
    def setup_method(self):
        self.a1 = Account("John")

    def teardown_method(self):
        pass

    def test_init(self):
        assert self.a1.get_name() == "John"
        assert self.a1.get_balance() == 0

    def test_deposit(self):
        assert self.a1.deposit(10) is True
        assert self.a1.deposit(0) is False
        assert self.a1.deposit(-10) is False
        assert self.a1.deposit("hi") is False

    def test_withdraw(self):
        assert self.a1.withdraw(10) is False
        assert self.a1.withdraw(0) is False
        assert self.a1.withdraw(-10) is False
        assert self.a1.withdraw("hi") is False

        self.a1.deposit(10)
        assert self.a1.withdraw(5) is True
