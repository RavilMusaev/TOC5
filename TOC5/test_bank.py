
import unittest
from bank import Account


class TestBankAccount(unittest.TestCase):

    def setUp(self):
        # Создаём новые счета перед каждым тестом
        self.account = Account("Иван Иванов", "12345")
        self.second_account = Account("Пётр Петров", "67890")

    # Проверка создания счёта
    def test_create_account(self):
        self.assertEqual(self.account.owner, "Иван Иванов")
        self.assertEqual(self.account.account_number, "12345")
        self.assertEqual(self.account.get_balance(), 0)

    # Проверка некорректного создания счёта
    def test_invalid_owner(self):
        with self.assertRaises(ValueError):
            Account("", "12345")

    def test_invalid_account_number(self):
        with self.assertRaises(ValueError):
            Account("Иван Иванов", "")

    # Проверка пополнения
    def test_deposit(self):
        self.account.deposit(1000)
        self.assertEqual(self.account.get_balance(), 1000)

    def test_deposit_multiple_times(self):
        self.account.deposit(500)
        self.account.deposit(300)
        self.assertEqual(self.account.get_balance(), 800)

    def test_deposit_negative_amount(self):
        with self.assertRaises(ValueError):
            self.account.deposit(-100)

        self.assertEqual(self.account.get_balance(), 0)

    def test_deposit_zero(self):
        with self.assertRaises(ValueError):
            self.account.deposit(0)

    def test_deposit_invalid_type(self):
        with self.assertRaises(TypeError):
            self.account.deposit("100")

    # Проверка снятия
    def test_withdraw(self):
        self.account.deposit(1000)
        self.account.withdraw(300)
        self.assertEqual(self.account.get_balance(), 700)

    def test_withdraw_insufficient_funds(self):
        self.account.deposit(500)

        with self.assertRaises(ValueError):
            self.account.withdraw(600)

        self.assertEqual(self.account.get_balance(), 500)

    def test_withdraw_negative_amount(self):
        self.account.deposit(500)

        with self.assertRaises(ValueError):
            self.account.withdraw(-100)

        self.assertEqual(self.account.get_balance(), 500)

    def test_withdraw_zero(self):
        with self.assertRaises(ValueError):
            self.account.withdraw(0)

    def test_withdraw_invalid_type(self):
        with self.assertRaises(TypeError):
            self.account.withdraw("100")

    # Проверка перевода
    def test_transfer(self):
        self.account.deposit(1000)
        self.account.transfer(self.second_account, 400)

        self.assertEqual(self.account.get_balance(), 600)
        self.assertEqual(self.second_account.get_balance(), 400)

    def test_transfer_insufficient_funds(self):
        self.account.deposit(200)

        with self.assertRaises(ValueError):
            self.account.transfer(self.second_account, 300)

        # Балансы обоих счетов не должны измениться
        self.assertEqual(self.account.get_balance(), 200)
        self.assertEqual(self.second_account.get_balance(), 0)

    def test_transfer_negative_amount(self):
        self.account.deposit(500)

        with self.assertRaises(ValueError):
            self.account.transfer(self.second_account, -100)

        self.assertEqual(self.account.get_balance(), 500)
        self.assertEqual(self.second_account.get_balance(), 0)

    def test_transfer_zero(self):
        self.account.deposit(500)

        with self.assertRaises(ValueError):
            self.account.transfer(self.second_account, 0)

        self.assertEqual(self.account.get_balance(), 500)
        self.assertEqual(self.second_account.get_balance(), 0)

    def test_transfer_to_self(self):
        self.account.deposit(500)

        with self.assertRaises(ValueError):
            self.account.transfer(self.account, 100)

        self.assertEqual(self.account.get_balance(), 500)

    def test_transfer_invalid_type(self):
        self.account.deposit(500)

        with self.assertRaises(TypeError):
            self.account.transfer(self.second_account, "100")

        self.assertEqual(self.account.get_balance(), 500)
        self.assertEqual(self.second_account.get_balance(), 0)

    # Проверка получения баланса
    def test_get_balance(self):
        self.account.deposit(750)
        self.assertEqual(self.account.get_balance(), 750)

    # Проверка пустого счёта
    def test_empty_account(self):
        self.assertTrue(self.account.is_empty())

    def test_non_empty_account(self):
        self.account.deposit(100)
        self.assertFalse(self.account.is_empty())

    def test_empty_after_withdrawal(self):
        self.account.deposit(500)
        self.account.withdraw(500)
        self.assertTrue(self.account.is_empty())


if __name__ == "__main__":
    unittest.main()