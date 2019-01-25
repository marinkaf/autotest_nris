class Registration_data:
    
    def __init__(self, username=None, password=None, code=None):
        self.username = username
        self.password = password
        self.code = code



class Person_fl_data:

    def __init__(self, \
            phone_code=None, \
            phone_number=None, \
            surname=None, \
            name=None, \
            patronymic=None, \
            birthday=None, \
            passport_num=None, \
            passport_date=None, \
            passport_issued_by=None, \
            passport_department=None, \
            address=None, \
            additional_communication=None, \
            passport_file=None, \
            passport_visa=None):

        self.phone_code = phone_code
        self.phone_number = phone_number
        self.surname = surname
        self.name = name
        self.patronymic = patronymic
        self.birthday = birthday
        self.passport_num = passport_num
        self.passport_date = passport_date
        self.passport_issued_by = passport_issued_by
        self.passport_department = passport_department
        self.address = address
        self.additional_communication = additional_communication
        self.passport_file = passport_file
        self.passport_visa = passport_visa
