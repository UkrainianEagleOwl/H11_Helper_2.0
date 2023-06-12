from collections import UserDict


class AddressBook(UserDict):
    def add_record(self, aRecord):
        self.data[aRecord.user_name.value] = aRecord

    def find_in_values(self, aRecord):
        result = True if not (aRecord in self.data.values()) else None
        if result:
            for i in self.data.values():
                if i == aRecord:
                    return (aRecord.name.value, aRecord)
        else:
            return None

    
class Field():
    value = ''

    def __init__(self, aValue):
        self.value = aValue

class Name(Field):
    value = 'UserName' 

class Phone(Field):
    value = '+38073877327'

class Record():
    user_name = Name
    user_phones = []

    def __init__(self, aName,aPhone):
        if isinstance(aName, str):
            self.user_name.value = aName
        elif isinstance(aName, Name):
            self.user_name = aName      
        self.add_phone(aPhone)

    def add_phone(self,aPhone):       
        if isinstance(aPhone, str):
            self.user_phones.append(Phone(aPhone))
        elif isinstance(aPhone, Phone):
            self.user_phones.append(aPhone)

    def remove_phone(self, aPhone):
        self.user_phones.remove(aPhone)
    
    def remove_n_phone(self, aPhoneIndex):
        self.user_phones.pop(aPhoneIndex)
    
    def change_n_phone(self, aPhoneIndex, aNewPhone):
        self.user_phones[aPhoneIndex].value = aNewPhone
