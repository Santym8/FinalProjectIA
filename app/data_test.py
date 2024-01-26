class DataTest:
    def __init__(self, distance_from_home, distance_from_last_transaction, ratio_to_median_purchase_price, repeat_retailer, used_chip, used_pin_number, online_order, fraud):
        self.distance_from_home = distance_from_home
        self.distance_from_last_transaction = distance_from_last_transaction
        self.ratio_to_median_purchase_price = ratio_to_median_purchase_price
        self.repeat_retailer = repeat_retailer
        self.used_chip = used_chip
        self.used_pin_number = used_pin_number
        self.online_order = online_order
        self.fraud = fraud
        


def data_test():
    return [
        DataTest(57.87785658389723,0.3111400080477545,1.9459399775518593,1,1,0,0,0),
        DataTest(2.131955665990563,56.3724005365082,6.358667321630612,1,0,0,1,1),
        DataTest(114.51978939161216,0.7070032526577117,0.516989925221995,1,0,0,0,0),
        DataTest(3.8030573513256023,67.24108052618409,1.8729496143044642,1,0,0,1,1),
        DataTest(5.471113979085435,1.0241780871042283,0.0671805015773473,1,0,0,0,0),
        DataTest(9.598401340573979,0.4545563461632137,6.084828700634962,1,0,0,1,1),
        DataTest(3.2313647628869178,0.3972852820667029,2.095418742983735,1,0,0,1,0),
        DataTest(20.141476291885343,116.56247654457643,1.1729994639657837,1,0,0,1,1),
        DataTest(8.167520581642606,3.289483550056162,0.20941382624946914,1,1,0,0,0),
        DataTest(181.86331424612112,0.48476058390405347,1.9557071972465698,1,0,0,1,1),
    ]