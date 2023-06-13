import re
from datetime import datetime
from collections import UserDict


class SetterValueIncorrect(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class AddressBook(UserDict):
    # Class representing an address book, which is a subclass of UserDict

    def add_record(self, aRecord):
        # Method to add a record to the address book
        self.data[aRecord.user_name.value] = aRecord

    def find_in_values(self, aRecord):
        # Method to find a record in the address book's values
        if aRecord in self.data.values():
            for i in self.data.values():
                if i == aRecord:
                    return (aRecord.user_name.value, aRecord)
        return None


class Field():
    # Base class representing a field
    def __init__(self, value):
        # Constructor to initialize the field with a value
        self._value = value


class Name(Field):
    # Class representing a name field, which is a subclass of Field
    @property
    def value(self):
        # Getter method for the value property
        return self._value

    @value.setter
    def value(self, new_value):
        # Setter method for the value property
        if isinstance(new_value,str):
            self._value = new_value
        else:
            raise SetterValueIncorrect('Only string accepted')


class Phone(Field):
    # Class representing a phone field, which is a subclass of Field
    @property
    def value(self):
        # Getter method for the value property
        return self._value

    @value.setter
    def value(self, new_value):
        # Setter method for the value property
        if re.search(r"[+]380[(]\d{2}[)]\d{3}[-]\d{1,2}[-]\d{2,3}(?=.{1,17})", new_value):
            self._value = new_value
        else:
            raise SetterValueIncorrect('Only correct type of phone numbers accepted')


class Birthday(Field):
    # Class representing a birthday field, which is a subclass of Field

    @property
    def value(self):
        # Getter method for the value property
        return self.__value

    @value.setter
    def value(self, new_value):
        # Setter method for the value property
        if new_value is datetime:
            self._value = new_value
        elif isinstance(new_value, str):
            try:
                self._value = datetime.strptime(new_value, '%d %B %Y')
            except:
                raise SetterValueIncorrect('Incorrect string type of data')
        else:
            raise SetterValueIncorrect('Only string data or datetime accepted')


class Record():
    # Class representing a record

    def __init__(self, name, phone=None, birthday=None):
        # Constructor to initialize the record with a name, phone, and birthday
        self.user_phones = []
        self.user_birthday = birthday

        if isinstance(name, str):
            self.user_name = Name(name)
        elif isinstance(name, Name):
            self.user_name = name
        if phone:
            self.add_phone(phone)

    def __eq__(self, other):
        if isinstance(other, Record):
            return self.user_name.value == other.user_name.value
        return False

    def add_phone(self, aPhone):
        # Method to add a phone to the record
        if isinstance(aPhone, str):
            self.user_phones.append(Phone(aPhone))
        elif isinstance(aPhone, Phone):
            self.user_phones.append(aPhone)

    def remove_phone(self, aPhone):
        # Method to remove a phone from the record
        self.user_phones.remove(aPhone)

    def remove_n_phone(self, aPhoneIndex):
        # Method to remove the phone at a specified index from the record
        self.user_phones.pop(aPhoneIndex)

    def change_n_phone(self, aPhoneIndex, aNewPhone):
        # Method to change the phone at a specified index to a new phone
        self.user_phones[aPhoneIndex].value = aNewPhone

    def days_to_birthday(self):
        # Method to calculate the number of days to the birthday
        if not self.user_birthday:
            return None

        current_datetime = datetime.now()
        this_year_birthday = datetime(
            year=current_datetime.year, month=self.user_birthday.month, day=self.user_birthday.day)
        return (this_year_birthday - current_datetime).days

