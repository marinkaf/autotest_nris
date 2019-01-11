class Registration_data:
    
    def __init__(self, username, password, code):
        self.username = username
        self.password = password
        self.code = code



class Person_fl_data:

    def __init__(self, phone_code, phone_number, surname, name, patronymic, birthday, passport_num, \
        passport_date, passport_issued_by, passport_department, address, additional_communication, passport_file, passport_visa):

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
