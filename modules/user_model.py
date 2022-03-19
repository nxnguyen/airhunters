from datetime import datetime


class MyUser:

    def __init__(self):
        self.id = 0

    def init_by_row(self, row):
        self.id = int(row[0])
        self.name = row[1]
        self.firstName = self.name.split(' ')[0]
        self.lastName = self.name.split(' ')[1]
        self.discordId = row[2]
        self.twitterId = row[3]
        self.twitterProfileLink = 'https://twitter.com/' + self.twitterId

        self.phoneNumber = '0' + str(row[4])

        self.birthDate = datetime.fromisoformat(row[5])
        self.mail = row[6]
        self.teleUsername = self.mail.split('@')[0]
        self.mailPass = row[7]
        self.etherWallet = row[8]
        self.bscWallet = row[9]
        self.chromeProfileId = row[10]
        self.redditId = row[11]
        self.redditProfileLink = 'https://www.reddit.com/user/' + self.redditId
        self.mediumId = row[12]
        self.redditProfileLink = 'https://medium.com/@' + self.mediumId
        self.youtubeChannelLink = row[13]

    def calculate_age(self):
        today = datetime.today()
        return today.year - self.birthDate.year - (
                (today.month, today.day) < (self.birthDate.month, self.birthDate.day))
