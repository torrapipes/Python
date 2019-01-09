from regularItem import RegularItem

class Backstage(RegularItem):

    def update_quality(self):
        if self.sell_in >= 10:
            self.setQuality(+1)
        else:
            self.setQuality(+2)
        self.setSell_in()


if __name__ == '__main__':

    # CREATED OBJECT
    backstage = Backstage("backstage", 9, 3)
    backstage.update_quality()

    # TEST CASES
    assert backstage.getQuality() == 5
    assert backstage.getSell_in() == 8

