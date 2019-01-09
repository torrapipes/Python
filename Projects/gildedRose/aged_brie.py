class aged_brie():

    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def setSell_in(self):
        self.sell_in = self.sell_in - 1

    # Override metodo setQuality de NormalItem
    def setQuality(self, valor):

        if self.quality + valor <= 50:
            self.quality = self.quality + valor
        else:
            self.quality = 50
        # NormalItem.setQuality(self, valor)
        assert 0 <= self.quality <= 50, "quality de %s fuera de rango" % self.__class__.__name__

    # Override metodo update_quality de la Interfaz
    def update_quality(self):

        if self.sell_in > 0:
            self.setQuality(1)
        else:
            self.setQuality(2)
        self.setSell_in()

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


if __name__ == '__main__':

    item = AgedBrie("Aged Brie", 2, 0)
    print(item)

    # test update_quality
    for dia in range(1, 10):
        item.update_quality()
        print(item)

    # test update_quality incorret input
    item = AgedBrie("Aged Brie", 2, 100)
    for dia in range(1, 10):
        item.update_quality()
        print(item)