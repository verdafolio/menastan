#!/usr/bin/env python
import random

# Python's ability to manipulate properties makes me nervous
# Maybe it's because I studied Java in university
# On the other hand it works in this situation

class battlespace(object):

    # Constructor
    def __init__(self):
        # These don't change at least
        self.description = 'battlespace'
        self.country = 'Menastan'
        
        # Because all of this is random, we must initialize them by generating a bunch of random numbers
        brch = random.randint(1,4)
        if brch == 1:
            branch = 'Air Force'
        elif brch == 2:
            branch = 'Army'
        elif brch == 3:
            branch = 'Navy'
        elif brch == 4:
            branch = 'Company'
            
         self.branch = branch
            
        # In the Navy you'd be a Commander instead of Colonel
        # And as a spy you'd just be Sir
        if brch == 3:
            rank = 'Commander'
        elif brch == 4:
            rank = 'Sir'
        else:
            rank = 'Colonel'
        
        self.rank = rank
        
        # TODO: Move to a CSV
        lt_name =  random.choice(['Alexander', 'Bajracharya', 'Chang', 'Fox', 'Daniels', 'Lin', 'Clarke', 'Thackeray', 'Lerner', 'Xue', 'Coleman', 'Bradford', 'Wilkerson', 'Wade', 'Hickman', 'Wilcox', 'O\'Neill', 'Espinoza', 'Person', 'Macaulay', 'Schwartz', 'Russell', 'Mercer', 'Hawking', 'Saunders', 'Moore', 'Maxwell', 'Komae', 'Dolan', 'Hernandez', 'Barradell', 'Vasquez', 'Khan', 'Al-Asad', 'Heinz', 'Surkov', 'Caleca', 'Virovets', 'Grekova', 'Gonzalez', 'Nagler', 'Lee', 'Alder', 'Williams', 'Nelson', 'Copeland', 'Blaesi', 'Kim', 'Park', 'Richards', 'O\'Connor','Montalvo', 'Trevino', 'Cobb', 'Arroyo', 'Hong', 'Katz', 'Weiner', 'Stafford', 'Kang', 'Liang', 'Cole', 'Kalfus', 'Goldberg', 'Kosut', 'Bang', 'Yan', 'Akinleye', 'Esiebo', 'Muheisen', 'Mohammed', 'Misaka', 'Woodward', 'Touma', 'Papiko', 'Nagato', 'Teekasingh', 'DeAngeli', 'Iyovitch', 'Bennett', 'Kalfus', 'Gruberg', 'Lizarazo', 'Galperina', 'Nakiri ', 'Marui', 'Tadokoro ', 'Chetrit', 'Zhee', 'Urvashi', 'Shamsie', 'Aldini', 'Mito', 'Glass', 'Akasaki', 'Senjougahara', 'Araragi', 'Childan', 'Hanekawa', 'Tugwell', 'Kleintank', 'Sewell', 'Fuente', 'Norgaard', 'Muser', 'Kershner', 'Wang', 'Wong', 'McCormick', 'Walker', 'Rouhani', 'Rafsanjani', 'Pebdani', 'Robado', 'Antonellis', 'Mathis', 'Holloway', 'Vincent', 'Coffey', 'Shelton', 'Burger', 'Rasmussen', 'Harper', 'Tsang', 'Kshash', 'Madoka', 'Homura', 'Waldman', 'Jeong', 'Beery', 'Bhatt'])
        
        self.lt_name = lt_name
        self.province_number = random.randint(3,6)
        
        # TODO: Move to a CSV
       '0' : 'Al-Hiyal'}
        for x in range(1,self.province_number):
            d[x] = random.choice(['I\'tiraf', 'Al-Fahhas', 'Hawa', 'Hafayah', 'Halwa', 'Kadarasto', 'Kayapasa', 'Gerendira' , 'Jiroyaan','Heridasht', 'Tel Khawah', 'As-Samala', 'Salah al-Arirshut', 'Ghanaqadah', 'Dawasfan', 'Al-Qadeidmi', 'As-Saiyda', 'Marirakh', 'Mneefira', 'Al-Hasalkhad', 'El Atsat', 'Mesmene', 'Mulid', 'Jute', 'Kachidia', 'Maguig', 'En Nagana', 'Um Kera', 'Sota', 'Médenah', 'Ruwaidhat', 'Matariq', 'Al-Aalia', 'Ru’aysah', 'Al-Huwaiyit'])
            
            province(x)
        
        
    # There's no reason for setters, these are instatiated and don't change
    def get_Country(self):
        return self._country
        
    def get_Branch(self):
        return self._branch
        
    def get_Rank(self):
        return self._rank
        
    def get_LTName(self):
        return self._lt_name
        
class province(self):

    def __init__(self, provNum, provName):
        self.security_rating = random.randint(20,90)
        self.local_approval = random.randint(30,80)
        self.province_number = provNum
        self.province_name = provName
    
    # Only setting values that should change
    # Look properties just lead to trouble
    # I should prevent overflows and underflows
    # 
    # The setters add or subtract based on the argument 
    def set_SecurityRating(self, secRating):    
        secRating = secRating + random.randint(-3,3)
        
        if self.security_rating + secRating > 100:
            self.security_rating = 100
        elif self.security_rating + secRating < 0:
            self.security_rating = 0
        else:
            self.security_rating = self.security_rating + secRating

    
    def set_LocalApproval(self, localApproval):
        localApproval = localApproval + random.randint(-3,3)
        
        if self.local_approval + localApproval > 100:
            self.local_approval = 100
        elif self.local_approval + localApproval < 0:
            self.local_approval = 0
        else:
            self.local_approval = self.local_approval + localApproval
           
           
    # The mere act of asking should be cruel and change the values
    # Real life is not kind enough to give you an exact answer
    # So neither should this for the Security Rating or Local Approval
    def get_ProvinceNumber(self):
        return self.province_number
        
    def get_ProvinceName(self):
        return self.province_name
    
    # LOW, GUARDED, ELEVATED, HIGH, SEVERE, BLACKWATCH PLAID
    # The final one is the overflow condition
    def get_SecurityRating(self):
        set_SecurityRating(random.randint(-3,3))
        
        if self.security_rating > 100 or security_rating < 0:
            return "BLACKWATCH PLAID"        
        elif self.security_rating < 20:
            return "SEVERE"
        elif self.security_rating >= 20 and self.security_rating < 40:
            return "HIGH"
        elif self.security_rating >= 40 and self.security_rating < 60:
            return "ELEVATED"
        elif self.security_rating >= 60 and self.security_rating < 80:
            return "GUARDED"
        elif self.security_rating >= 80 and self.security_rating <= 100:
            return "LOW" 
        else: 
            return: "You shouldn't be able to get here"
            
    # CRITICAL, LOW, MODERATE, HIGH        
    def get_LocalApproval(self):
        set_LocalApproval(random.randint(-3,3))
        
        if self.local_approval > 100 or security_rating < 0:
            return "FUCKED UP"
        elif self.local_approval < 25:
            return "CRITICAL"
        elif self.local_approval >= 25 and self.security_rating < 50:
            return "LOW"
        elif self.local_approval >= 50 and self.security_rating < 75:
            return "MODERATE"
        elif self.local_approval >= 75 and self.security_rating <= 100:
            return "HIGH"
        else: 
            return "You shouldn't be able to get here"
