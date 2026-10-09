
class Account: # Тело кода по приёму информации от пользователей 
    # Вход в аккаунт
    def __init__(self, owner, account_number): 
        if not isinstance(owner, str) or not owner.strip(): 
            raise ValueError("Имя владельца не должно быть пустым")

        if not isinstance(account_number, str) or not account_number.strip():
            raise ValueError("Номер счёта не должен быть пустым")

        self.owner = owner
        self.account_number = account_number
        self._balance = 0

    # Пополнение счёта
    def deposit(self, amount):
        if isinstance(amount, bool) or not isinstance(amount, (int, float)):
            raise TypeError("Сумма должна быть числом")

        if amount <= 0:
            raise ValueError("Сумма пополнения должна быть больше нуля")

        self._balance += amount

    # Снятие денег
    def withdraw(self, amount):
        if isinstance(amount, bool) or not isinstance(amount, (int, float)):
            raise TypeError("Сумма должна быть числом")

        if amount <= 0:
            raise ValueError("Сумма снятия должна быть больше нуля")

        if amount > self._balance:
            raise ValueError("Недостаточно средств")

        self._balance -= amount

    # Перевод денег на другой счёт
    def transfer(self, target_account, amount):
        if not isinstance(target_account, Account):
            raise TypeError("Получатель должен иметь банковский счёт")

        if target_account is self:
            raise ValueError("Нельзя переводить деньги на свой счёт")

        if isinstance(amount, bool) or not isinstance(amount, (int, float)):
            raise TypeError("Сумма должна быть числом")

        if amount <= 0:
            raise ValueError("Сумма перевода должна быть больше нуля")

        if amount > self._balance:
            raise ValueError("Недостаточно средств для перевода")

        # Сначала проверяем все условия, затем изменяем оба баланса
        self._balance -= amount
        target_account._balance += amount

    # Получение текущего баланса
    def get_balance(self):
        return self._balance

    # Проверка пустого счёта
    def is_empty(self):
        return self._balance == 0