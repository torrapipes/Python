if __name__ == '__main__':

    # CREATED AN OBJECT
    Duck = RegularItem(0, 4)

    # TEST CASES
    assert Duck.setSell_in() == -1
    assert Duck.update_quality() == -2