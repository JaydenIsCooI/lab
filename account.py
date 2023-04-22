class Account:
    def __init__(self, name: str) -> None:
        """
        This function sets up an Account object
        :param name: Account name
        """
        self.__account_name = name
        self.__account_balance = 0

    def deposit(self, amount: float) -> bool:
        """
        This function adds money to an Account's balance if
        amount is greater than zero
        :param amount: Amount of money to be added to the Account's balance
        :return: Returns true if money was added; False if the conditions for amount were not met
        """
        if amount > 0:
            self.__account_balance += amount
            return True
        return False

    def withdraw(self, amount: float) -> bool:
        """
        This function subtracts money from an Account's balance if amount
        is greater than zero but less than the Account's current balance
        :param amount:
        :return: Returns true if money was withdrawn; False if the conditions for amount were not met
        """
        if self.__account_balance > amount > 0:
            self.__account_balance -= amount
            return True
        return False

    def get_name(self) -> str:
        """
        This function returns the Account's name
        :return: Returns the Account's name as a string
        """
        return self.__account_name

    def get_balance(self) -> float:
        """
        This function returns the Account's balance
        :return: Returns the Account's balance as a float
        """
        return self.__account_balance
