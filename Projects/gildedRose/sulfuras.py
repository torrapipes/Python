from regularItem import RegularItem

class Sulfuras(RegularItem):


    def update_quality(self):
        assert self.quality == 80, "Quality de %s no es 80" % self.__class__.__name__
        pass


if __name__ == '__main__':

    item = Sulfuras("Sulfuras, mano de Maradona", 3, 80)

    item.update_quality()
    assert item.getQuality() == 80