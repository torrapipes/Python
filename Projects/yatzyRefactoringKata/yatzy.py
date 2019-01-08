class Yatzy:

    @staticmethod
    def chance(*args):
        total = 0
        for dice in args:
            total += dice
        return total

    @staticmethod
    def yatzy(*dice):
        reference = dice[0]
        for die in dice:
            if die != reference:
                return 0        
        return 50
    
    @staticmethod
    def ones(*dice):
        sum = 0
        for die in dice:
            if die == 1:
                sum += 1
        return sum
    

    @staticmethod
    def twos( *dice):
        sum = 0
        for die in dice:
            if die == 2:
                sum += 2
        return sum
    
    @staticmethod
    def threes( *dice):
        sum = 0
        for die in dice:
            if die == 3:
                sum += 3
        return sum
    

    def __init__(self, d1, d2, d3, d4, _5):
        self.dice = [0]*5
        self.dice[0] = d1
        self.dice[1] = d2
        self.dice[2] = d3
        self.dice[3] = d4
        self.dice[4] = _5
    
    def fours(*dice):
        sum = 0
        for die in dice:
            if die == 4:
                sum += 4
        return sum
    

    def fives(*dice):
        sum = 0
        for die in dice:
            if die == 5:
                sum += 5
        return sum
    

    def sixes(*dice):
        sum = 0
        for die in dice:
            if die == 6:
                sum += 6
        return sum
    
    @staticmethod
    def pair(*dice):
        repeated = []
        for die in dice:
            if dice.count(die) > 1:
                repeated.append(die)
        if repeated != []:    
            maxDie = max(repeated)
            return maxDie * 2
        else:
            return 0
    
    @staticmethod
    def two_pair(*dice):
        pairs = []
        score = 0
        for die in dice:
            if dice.count(die) > 1 and die not in pairs:
                pairs.append(die)
        if len(pairs) > 1:
            score = pairs[0] * 2 + pairs[1] * 2
        return score  

    @staticmethod
    def three_of_a_kind(*dice):
        score = 0
        three = 3
        for die in dice:
            if dice.count(die) >= three:
                score = die * three
                break
        return score


    @staticmethod
    def four_of_a_kind(*dice):
        score = 0
        four = 4
        for die in dice:
           if dice.count(die) >= four:
               score = die * four
               break
        return score

    @staticmethod
    def smallStraight(*dice):
        for number in range(1,6):
            if dice.count(number) != 1:
                return 0
        return 15

    @staticmethod
    def largeStraight( d1,  d2,  d3,  d4,  d5):
        tallies = [0]*6
        tallies[d1-1] += 1
        tallies[d2-1] += 1
        tallies[d3-1] += 1
        tallies[d4-1] += 1
        tallies[d5-1] += 1
        if (tallies[1] == 1 and
            tallies[2] == 1 and
            tallies[3] == 1 and
            tallies[4] == 1
            and tallies[5] == 1):
            return 20
        return 0
    

    @staticmethod
    def fullHouse( d1,  d2,  d3,  d4,  d5):
        tallies = []
        _2 = False
        i = 0
        _2_at = 0
        _3 = False
        _3_at = 0

        tallies = [0]*6
        tallies[d1-1] += 1
        tallies[d2-1] += 1
        tallies[d3-1] += 1
        tallies[d4-1] += 1
        tallies[d5-1] += 1

        for i in range(6):
            if (tallies[i] == 2): 
                _2 = True
                _2_at = i+1
            

        for i in range(6):
            if (tallies[i] == 3): 
                _3 = True
                _3_at = i+1
            

        if (_2 and _3):
            return _2_at * 2 + _3_at * 3
        else:
            return 0

if __name__ == '__main__':

    # CHANCE TEST CASES
    assert Yatzy.chance(1,2,3,4,5) == 15
    assert Yatzy.chance(2,2,3) == 7
    assert Yatzy.chance(4,6,3,1,2,5) == 21

    # YATZY TEST CASES
    assert Yatzy.yatzy(1,1,1,1,1) == 50
    assert Yatzy.yatzy(1,1,1,3,1) == 0
    assert Yatzy.yatzy(1,1,1,2,2) == 0

    # ONES TEST CASES
    assert Yatzy.ones(1,1,1,1,1,1) == 6
    assert Yatzy.ones(1,2,1,1) == 3
    assert Yatzy.ones(2,3,5,4) == 0

    # TWOS TEST CASES
    assert Yatzy.twos(2,2,2,2,2,2) == 12
    assert Yatzy.twos(2,2,2,1,5,6) == 6
    assert Yatzy.twos(1,3,4,5,6) == 0

    # THREES TEST CASES
    assert Yatzy.threes(3,3,3,3,3,3) == 18
    assert Yatzy.threes(3,3,3,1,2,4) == 9
    assert Yatzy.threes(2,4,4,5,5) == 0

    # FOURS TEST CASES
    assert 12 == Yatzy.fours(4,4,4,5,5)
    assert 8 == Yatzy.fours(4,4,5,5,5)
    assert 4 == Yatzy.fours(4,5,5,5,5)

    # FIVES TEST CASES
    assert 10 == Yatzy.fives(4,4,4,5,5)
    assert 15 == Yatzy.fives(4,4,5,5,5)
    assert 20 == Yatzy.fives(4,5,5,5,5)

    # SIXES TEST CASES
    assert 0 == Yatzy.sixes(4,4,4,5,5)
    assert 6 == Yatzy.sixes(4,4,6,5,5)
    assert 18 == Yatzy.sixes(6,5,6,6,5)

    # PAIR TEST CASES
    assert 6 == Yatzy.pair(3,4,3,5,6)
    assert 10 == Yatzy.pair(5,3,3,3,5)
    assert 12 == Yatzy.pair(5,3,6,6,5)

    # TWO PAIR TEST CASES
    assert 16 == Yatzy.two_pair(3,3,5,4,5)
    assert 18 == Yatzy.two_pair(3,3,6,6,6)
    assert 0 == Yatzy.two_pair(3,3,6,5,4)

    # THREE OF A KIND TEST CASES
    assert 9 == Yatzy.three_of_a_kind(3,3,3,4,5)
    assert 15 == Yatzy.three_of_a_kind(5,3,5,4,5)
    assert 9 == Yatzy.three_of_a_kind(3,3,3,3,5)

   # FOUR OF A KIND TEST CASES
    assert 12 == Yatzy.four_of_a_kind(3,3,3,3,5)
    assert 20 == Yatzy.four_of_a_kind(5,5,5,4,5)
    assert 12 == Yatzy.four_of_a_kind(3,3,3,3,3)
    assert 0  == Yatzy.four_of_a_kind(3,3,3,2,1)

    # SMALL STRAIGHT TEST CASES
    assert 15 == Yatzy.smallStraight(1,2,3,4,5)
    assert 15 == Yatzy.smallStraight(2,3,4,5,1)
    assert 0 == Yatzy.smallStraight(1,2,2,4,5)

    # LARGE STRAIGHT TEST CASES
    assert 20 == Yatzy.largeStraight(6,2,3,4,5)
    assert 20 == Yatzy.largeStraight(2,3,4,5,6)
    assert 0 == Yatzy.largeStraight(1,2,2,4,5)
  