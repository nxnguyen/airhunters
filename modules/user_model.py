from datetime import datetime

class MyUser:

    def __init__(self):
        self.id = 0

    def init_by_row(self, row):
        self.id = int(row[0])
        self.name = row[1]
        self.birthDate = datetime.fromisoformat(row[2])
        self.mail = row[3]
        self.mailPass = row[4]
        self.etherWallet = row[5]
        self.bscWallet = row[6]
        self.chromeProfileId = row[7]
        self.phoneNumber = '0' + str(row[8])

    def calculate_age(self):
        today = datetime.today()
        return today.year - self.birthDate.year - ((today.month, today.day) < (self.birthDate.month, self.birthDate.day))
