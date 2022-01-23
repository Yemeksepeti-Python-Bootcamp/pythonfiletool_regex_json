class Users:
    '''
    Class for all users data
    '''
    def __init__(self,
        email = "None",
        username = "None",
        fullname = "None",
        emailuserlk = "0",
        usernamelk = "0",
        year_of_birth = "1900",
        month_of_birth = "01",
        day_of_birth = "01",
        country = "None",
        ap = "1"):
        
        self.email = email
        self.username = username
        self.fullname = fullname
        self.emailuserlk = emailuserlk
        self.usernamelk = usernamelk
        self.year_of_birth = year_of_birth
        self.month_of_birth = month_of_birth
        self.day_of_birth = day_of_birth
        self.country = country
        self.ap = ap