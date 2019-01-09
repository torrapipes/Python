from regularItem import RegularItem

class AgedBrie(RegularItem):


    def update_quality(self):

        if self.sell_in > 0:
            self.setQuality(1)
        else:
            self.setQuality(2)
        self.setSell_in()


if __name__ == '__main__':

    agedBrie = AgedBrie("agedBrie", 2, 0)
    agedBrie.update_quality()

    assert agedBrie.getQuality() == 1
    