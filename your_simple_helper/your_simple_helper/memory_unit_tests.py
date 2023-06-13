import memory
import unittest
from datetime import datetime

def Create_simple_record(name = 'Alex'):
    return memory.Record(name, '+380(50)543-5-391', datetime(year=1970, month=11, day=7))


class AddressBookTest(unittest.TestCase):
    def test_add_record(self):
        address_book = memory.AddressBook()
        record = Create_simple_record()
        address_book.add_record(record)
        self.assertIn(record.user_name.value, address_book.data)

    def test_find_in_values(self):
        address_book = memory.AddressBook()
        record = memory.Record("John Doe", '+380(50)543-5-391',datetime(year=1970, month=11, day=7))
        address_book.add_record(record)
        result = address_book.find_in_values(record)
        self.assertEqual(result, ("John Doe", record))

    def test_days_to_birthday(self):
        record = Create_simple_record("John Doe")
        record.user_birthday = datetime(2023, 6, 17)
        days = record.days_to_birthday()
        self.assertEqual(days, 3)


if __name__ == '__main__':
    unittest.main()
    # Book = memory.AddressBook()
    # some_record = memory.Record('Alex', '+380(50)543-5-391')
    # some_name = memory.Name('Ann')
    # some_phone = memory.Phone('+380(67)777-77-77')
    # some_record.change_n_phone(0, '+380(99)555-44-32')
    # some_record.add_phone(some_phone)
    # some_record.remove_phone(some_phone)
    # some_record.remove_n_phone(0)
    # some_record.add_phone(some_phone)
    # Book.add_record(some_record)

    # print(Book)
