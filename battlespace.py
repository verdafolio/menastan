#!/usr/bin/env python
import random

class battlespace(object):

    # Constructor
    def __init__(self)
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
            
        if brch == 3:
            rank = 'Commander'
        elif brch == 4:
            rank = 'Sir'
        else:
            rank = 'Colonel'
        
        self.rank = rank
        
        lt_name =  random.choice(['Alexander', 'Bajracharya', 'Chang', 'Fox', 'Daniels', 'Lin', 'Clarke', 'Thackeray', 'Lerner', 'Xue', 'Coleman', 'Bradford', 'Wilkerson', 'Wade', 'Hickman', 'Wilcox', 'O\'Neill', 'Espinoza', 'Person', 'Macaulay', 'Schwartz', 'Russell', 'Mercer', 'Hawking', 'Saunders', 'Moore', 'Maxwell', 'Komae', 'Dolan', 'Hernandez', 'Barradell', 'Vasquez', 'Khan', 'Al-Asad', 'Heinz', 'Surkov', 'Caleca', 'Virovets', 'Grekova', 'Gonzalez', 'Nagler', 'Lee', 'Alder', 'Williams', 'Nelson', 'Copeland', 'Blaesi', 'Kim', 'Park', 'Richards', 'O\'Connor','Montalvo', 'Trevino', 'Cobb', 'Arroyo', 'Hong', 'Katz', 'Weiner', 'Stafford', 'Kang', 'Liang', 'Cole', 'Kalfus', 'Goldberg', 'Kosut', 'Bang', 'Yan', 'Akinleye', 'Esiebo', 'Muheisen', 'Mohammed', 'Misaka', 'Woodward', 'Touma', 'Papiko', 'Nagato', 'Teekasingh', 'DeAngeli', 'Iyovitch', 'Bennett', 'Kalfus', 'Gruberg', 'Lizarazo', 'Galperina', 'Nakiri ', 'Marui', 'Tadokoro ', 'Chetrit', 'Zhee', 'Urvashi', 'Shamsie', 'Aldini', 'Mito', 'Glass', 'Akasaki', 'Senjougahara', 'Araragi', 'Childan', 'Hanekawa', 'Tugwell', 'Kleintank', 'Sewell', 'Fuente', 'Norgaard', 'Muser', 'Kershner', 'Wang', 'Wong', 'McCormick', 'Walker', 'Rouhani', 'Rafsanjani', 'Pebdani', 'Robado', 'Antonellis', 'Mathis', 'Holloway', 'Vincent', 'Coffey', 'Shelton', 'Burger', 'Rasmussen', 'Harper', 'Tsang', 'Kshash', 'Madoka', 'Homura', 'Waldman', 'Jeong', 'Beery', 'Bhatt'])
        
        self.lt_name = lt_name
        
        self.province_number = random.randint(4,8)
        
        self.provinces = {'0' : 'Al-Hiyal'}
        for x in range(1,self.province_number):
            d[x] = random.choice(['I\'tiraf', 'Al-Fahhas', 'Hawa', 'Hafayah', 'Halwa', 'Kadarasto', 'Kayapasa', 'Gerendira' , 'Jiroyaan','Heridasht', 'Tel Khawah', 'As-Samala', 'Salah al-Arirshut', 'Ghanaqadah', 'Dawasfan', 'Al-Qadeidmi', 'As-Saiyda', 'Marirakh', 'Mneefira', 'Al-Hasalkhad', 'El Atsat', 'Mesmene', 'Mulid', 'Jute', 'Kachidia', 'Maguig', 'En Nagana', 'Um Kera', 'Sota', 'Médenah', 'Ruwaidhat', 'Matariq', 'Al-Aalia', 'Ru’aysah', 'Al-Huwaiyit'])
        
        
    def get_Country(self):
        return self._country
        
    def get_Branch(self):
        return self._branch
        
    def get_Rank(self):
        return self._rank
        
    def get_LTName(self):
        return self._lt_name