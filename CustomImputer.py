import pandas as pd

class CheckingForValues:

    def __init__(self, targetDataFrame):
        self.targetDataFrame = targetDataFrame
        

    def Check(self, targetBrand, value=0):
        ## Checking the missing value count
    
        bus = self.targetDataFrame[
            (self.targetDataFrame['vehicleType']=='bus') &
            (self.targetDataFrame['brand']==targetBrand) &
            (self.targetDataFrame['price']==value)
            ].count()

        # Number of missing values for the cabrio vehicleType 
        cabrio = self.targetDataFrame[
            (self.targetDataFrame['vehicleType']=='cabrio') &
            (self.targetDataFrame['brand']==targetBrand) &
            (self.targetDataFrame['price']==value)
            ].count()
            
        # Number of missing values for the coupe vehicleType 
        coupe = self.targetDataFrame[
            (self.targetDataFrame['vehicleType']=='coupe') &
            (self.targetDataFrame['brand']==targetBrand) &
            (self.targetDataFrame['price']==value)
            ].count()

        # Number of missing values for the kleinwagen (mini car) vehicleType 
        klein = self.targetDataFrame[
            (self.targetDataFrame['vehicleType']=='kleinwagen') &
            (self.targetDataFrame['brand']==targetBrand) &
            (self.targetDataFrame['price']==value)
            ].count()

        # Number of missing values for the kombi (van) vehicleType 
        kombi = self.targetDataFrame[
            (self.targetDataFrame['vehicleType']=='kombi') &
            (self.targetDataFrame['brand']==targetBrand) &
            (self.targetDataFrame['price']==value)
            ].count()

        # Number of missing values for the limusine vehicleType 
        limo = self.targetDataFrame[
            (self.targetDataFrame['vehicleType']=='limusine') &
            (self.targetDataFrame['brand']==targetBrand) &
            (self.targetDataFrame['price']==value)
            ].count()

        # Number of missing values for the suv vehicleType 
        suv = self.targetDataFrame[
            (self.targetDataFrame['vehicleType']=='suv') &
            (self.targetDataFrame['brand']==targetBrand) &
            (self.targetDataFrame['price']==value)
            ].count()
        

        ## Creating a dataframe to store the missing values
        df = pd.DataFrame({'Vehicle Type':['bus', 'cabrio', 'coupe', 'kleinwagen', 'kombi', 'limusine', 'suv'],
                           ## accessing the values by index
                           'Missing values':[bus[9], cabrio[9], coupe[9], klein[9], kombi[9], limo[9], suv[9]]
                            })
        return df

class FillMissingValues:
    def __init__(self, sourceDataFrame, targetDataFrame):
        self.sourceDataFrame = sourceDataFrame # dataFrame from which we derive the Values
        self.targetDataFrame = targetDataFrame # dataFrame that has missing Values
        
    def InputMissingValue(self, targetBrand, sourceBrand, value=0, returnArg=True):
        targetBrand=targetBrand # the brand that we search for in the targetDataFrame
        sourceBrand=sourceBrand # the brand that is derived to fill the missing values


        ## Filling missing values for the vehicle Type bus
        bus = self.targetDataFrame.loc[
            (self.targetDataFrame['vehicleType']=='bus') &
            (self.targetDataFrame['brand']==targetBrand) &
            (self.targetDataFrame['price']==value)].index

        self.targetDataFrame.loc[
            (self.targetDataFrame['vehicleType']=='bus') &
            (self.targetDataFrame['brand']==targetBrand) &
            (self.targetDataFrame['price']==value)] = self.targetDataFrame.loc[
                (self.targetDataFrame['vehicleType']=='bus') &
                (self.targetDataFrame['brand']==targetBrand) &
                (self.targetDataFrame['price']==value)
            ].replace(
                [value],
                [self.sourceDataFrame.loc[0, sourceBrand]]
            )
        
        ## Filling missing values for the vehicle Type cabrio
        cabrio = self.targetDataFrame.loc[
            (self.targetDataFrame['vehicleType']=='cabrio') &
            (self.targetDataFrame['brand']==targetBrand) &
            (self.targetDataFrame['price']==value)].index

        self.targetDataFrame.loc[
            (self.targetDataFrame['vehicleType']=='cabrio') &
            (self.targetDataFrame['brand']==targetBrand) &
            (self.targetDataFrame['price']==value)] = self.targetDataFrame.loc[
                (self.targetDataFrame['vehicleType']=='cabrio') &
                (self.targetDataFrame['brand']==targetBrand) &
                (self.targetDataFrame['price']==value)
            ].replace(
                [value],
                [self.sourceDataFrame.loc[1, sourceBrand]]
            )
        
        ## Filling missing values for the vehicle Type coupe
        coupe = self.targetDataFrame.loc[
            (self.targetDataFrame['vehicleType']=='coupe') &
            (self.targetDataFrame['brand']==targetBrand) &
            (self.targetDataFrame['price']==value)].index

        self.targetDataFrame.loc[
            (self.targetDataFrame['vehicleType']=='coupe') &
            (self.targetDataFrame['brand']==targetBrand) &
            (self.targetDataFrame['price']==value)] = self.targetDataFrame.loc[
                (self.targetDataFrame['vehicleType']=='coupe') &
                (self.targetDataFrame['brand']==targetBrand) &
                (self.targetDataFrame['price']==value)
            ].replace(
                [value],
                [self.sourceDataFrame.loc[3, sourceBrand]]
            )

        ## Filling missing values for the vehicle Type kleinwagen/ mini car
        klein = self.targetDataFrame.loc[
            (self.targetDataFrame['vehicleType']=='kleinwagen') &
            (self.targetDataFrame['brand']==targetBrand) &
            (self.targetDataFrame['price']==value)].index

        self.targetDataFrame.loc[
            (self.targetDataFrame['vehicleType']=='kleinwagen') &
            (self.targetDataFrame['brand']==targetBrand) &
            (self.targetDataFrame['price']==value)] = self.targetDataFrame.loc[
                (self.targetDataFrame['vehicleType']=='kleinwagen') &
                (self.targetDataFrame['brand']==targetBrand) &
                (self.targetDataFrame['price']==value)
            ].replace(
                [value],
                [self.sourceDataFrame.loc[3, sourceBrand]]
            )

            ## Filling missing values for the vehicle Type kombi/van
        kombi = self.targetDataFrame.loc[
            (self.targetDataFrame['vehicleType']=='kombi') &
            (self.targetDataFrame['brand']==targetBrand) &
            (self.targetDataFrame['price']==value)].index

        self.targetDataFrame.loc[
            (self.targetDataFrame['vehicleType']=='kombi') &
            (self.targetDataFrame['brand']==targetBrand) &
            (self.targetDataFrame['price']==value)] = self.targetDataFrame.loc[
                (self.targetDataFrame['vehicleType']=='kombi') &
                (self.targetDataFrame['brand']==targetBrand) &
                (self.targetDataFrame['price']==value)
            ].replace(
                [value],
                [self.sourceDataFrame.loc[4, sourceBrand]]
            )

            ## Filling missing values for the vehicle Type limusine
        limo = self.targetDataFrame.loc[
            (self.targetDataFrame['vehicleType']=='limousine') &
            (self.targetDataFrame['brand']==targetBrand) &
            (self.targetDataFrame['price']==value)].index

        self.targetDataFrame.loc[
            (self.targetDataFrame['vehicleType']=='limousine') &
            (self.targetDataFrame['brand']==targetBrand) &
            (self.targetDataFrame['price']==value)] = self.targetDataFrame.loc[
                (self.targetDataFrame['vehicleType']=='limousine') &
                (self.targetDataFrame['brand']==targetBrand) &
                (self.targetDataFrame['price']==value)
            ].replace(
                [value],
                [self.sourceDataFrame.loc[5, sourceBrand]]
            )

            ## Filling missing values for the vehicle Type suv
        suv = self.targetDataFrame.loc[
            (self.targetDataFrame['vehicleType']=='suv') &
            (self.targetDataFrame['brand']==targetBrand) &
            (self.targetDataFrame['price']==value)].index

        self.targetDataFrame.loc[
            (self.targetDataFrame['vehicleType']=='suv') &
            (self.targetDataFrame['brand']==targetBrand) &
            (self.targetDataFrame['price']==value)] = self.targetDataFrame.loc[
                (self.targetDataFrame['vehicleType']=='suv') &
                (self.targetDataFrame['brand']==targetBrand) &
                (self.targetDataFrame['price']==value)
            ].replace(
                [value],
                [self.sourceDataFrame.loc[6, sourceBrand]]
            )
        if returnArg==True:
            dataFrame = pd.DataFrame({
                'vehicleType':['bus', 'cabrio', 'coupe', 'kleinwagen', 'kombi', 'limusine', 'suv'],
                'Index':[bus, cabrio, coupe, klein, kombi, limo, suv]
            })
            return dataFrame
        else:
            pass

class FillMissingValuesPower:
    def __init__(self, targetDataFrame):
        self.targetDataFrame = targetDataFrame
    
    def avgPowerInput(self, avgValue, value=0, returnArg=True):
        
        index = self.targetDataFrame[
            self.targetDataFrame['powerPS']==value
        ].index

        self.targetDataFrame[
            self.targetDataFrame['powerPS']==value
        ] = self.targetDataFrame[
            self.targetDataFrame['powerPS']==value
        ].replace(
            [value],
            [avgValue]
        )
        if returnArg == True:
            return index
        else:
            pass

class CustomLabelEncoder:
    def __init__(self, dataFrame, column, brand, value):
        self.dataFrame = dataFrame
        self.brand = brand
        self.value = value
        self.column = column

    #topBrands=['volksWagen','bmw','opel','mercedes_benz','audi','ford', 'renault','peugeot','fiat','seat']

    def fit_transform(self):
        self.dataFrame[self.dataFrame[self.column]==self.brand]=self.dataFrame[
            self.dataFrame[self.column]==self.brand].replace(
                [self.brand],
                [self.value]
            )
        return 