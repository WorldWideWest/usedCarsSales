import pandas as pd

class TestingValue:

    def __init__(self, dataFrame):
        self.dataFrame = dataFrame
        

    def Check(self, brand):
        ## Checking the missing value count
        self.brand = brand
    
        bus = self.dataFrame[
            (self.dataFrame['vehicleType']=='bus') &
            (self.dataFrame['brand']==self.brand) &
            (self.dataFrame['price']==0)
            ].count()

        # Number of missing values for the cabrio vehicleType 
        cabrio = self.dataFrame[
            (self.dataFrame['vehicleType']=='cabrio') &
            (self.dataFrame['brand']==self.brand) &
            (self.dataFrame['price']==0)
            ].count()
            
        # Number of missing values for the coupe vehicleType 
        coupe = self.dataFrame[
            (self.dataFrame['vehicleType']=='coupe') &
            (self.dataFrame['brand']==self.brand) &
            (self.dataFrame['price']==0)
            ].count()

        # Number of missing values for the kleinwagen (mini car) vehicleType 
        klein = self.dataFrame[
            (self.dataFrame['vehicleType']=='kleinwagen') &
            (self.dataFrame['brand']==self.brand) &
            (self.dataFrame['price']==0)
            ].count()

        # Number of missing values for the kombi (van) vehicleType 
        kombi = self.dataFrame[
            (self.dataFrame['vehicleType']=='kombi') &
            (self.dataFrame['brand']==self.brand) &
            (self.dataFrame['price']==0)
            ].count()

        # Number of missing values for the limusine vehicleType 
        limo = self.dataFrame[
            (self.dataFrame['vehicleType']=='limusine') &
            (self.dataFrame['brand']==self.brand) &
            (self.dataFrame['price']==0)
            ].count()

        # Number of missing values for the suv vehicleType 
        suv = self.dataFrame[
            (self.dataFrame['vehicleType']=='suv') &
            (self.dataFrame['brand']==self.brand) &
            (self.dataFrame['price']==0)
            ].count()
        

        ## Creating a dataframe to store the missing values
        df = pd.DataFrame({'Vehicle Type':
                                            [
                                                'bus',
                                                'cabrio',
                                                'coupe',
                                                'kleinwagen',
                                                'kombi',
                                                'limusine',
                                                'suv'
                                            ],
                            'Missing values':
                                            [
                                                ## accessing the values by index
                                                bus[9],
                                                cabrio[9],
                                                coupe[9],
                                                klein[9],
                                                kombi[9],
                                                limo[9],
                                                suv[9]
                                            ]
                            })
        return df