from regularItem import RegularItem

class backstage(RegularItem):

    def update_quality(self):
        if self.sell_in > 10:
            self.setQuality(+1)
        else:
            self.setQuality(+2)
        self.setSell_in()


if __name__ == '__main__':

    # CREATED OBJECT
    backstage = backstage("backstage", 9, 3)
    backstage.update_quality()

    # TEST CASES
    assert backstage.getQuality() == 5
    assert backstage.getSell_in() == 8

