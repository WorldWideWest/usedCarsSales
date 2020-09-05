import pandas as pd

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
            (self.targetDataFrame['vehicleType']=='limusine') &
            (self.targetDataFrame['brand']==targetBrand) &
            (self.targetDataFrame['price']==value)].index

        self.targetDataFrame.loc[
            (self.targetDataFrame['vehicleType']=='limusine') &
            (self.targetDataFrame['brand']==targetBrand) &
            (self.targetDataFrame['price']==value)] = self.targetDataFrame.loc[
                (self.targetDataFrame['vehicleType']=='limusine') &
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
                'vehicleType':['bus',
                                'cabrio',
                                'coupe',
                                'kleinwagen',
                                'kombi',
                                'limusine',
                                'suv'],
                'Index':[bus,
                        cabrio,
                        coupe,
                        klein,
                        kombi,
                        limo,
                        suv]
            })
            return dataFrame
        else:
            pass