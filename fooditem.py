class fooditemcw():
    def __init__(self, food, pounds):
        self._food = food
        self._pounds = pounds
        self._standard = 0
        self._calcprice = 0
        self.PriceListcw()

    def PriceListcw(self):
        if self._food == 'Dry Cured Iberian Ham':
            self._standard = 177.80
        elif self._food == 'Wagyu Steaks':
            self._standard = 450.00
        elif self._food == 'Matsutake Mushrooms':
            self._standard = 272.00
        elif self._food == 'Kopi Luwak Coffee':
            self._standard = 306.50   
        elif self._food == 'Moose Cheese':
            self._standard = 487.20 
        elif self._food == 'White Truffles':
            self._standard = 3600.00
        elif self._food == 'Blue Fin Tuna':
            self._standard = 3603.00
        elif self._food == 'Le Bonnotte Potatoes':
            self._standard = 270.81
        else:
            self._standard = 0

    def costcw(self):
        self._calcprice = self._standard * self._pounds
        return self._calcprice