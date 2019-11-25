import random

class Dice( object ):
    def __init__( self, strategy ):
        self.strategy= strategy
        self.lastRoll= None
    def roll( self ):
        self.lastRoll= self.strategy.roll()
        return self.lastRoll
    def total( self ):
        return reduce( lambda a,b:a+b, self.lastRoll, 0 )


class DiceStrategy( object ):
    def roll( self ):
        raise NotImplementedError

class DiceStrategy1( DiceStrategy ):
    def roll( self ):
        return ( random.randrange(6)+1, random.randrange(6)+1 )
    
class DiceStrategy2( DiceStrategy ):
    
    class Die:
        def __init__( self, sides=6 ):
            self.sides= sides
        def roll( self ):
            return random.randrange(self.sides)+1
    def __init__( self, set=2, faces=6 ):
        self.dice = tuple( DiceStrategy2.Die(faces) for d in range(set) )
    def roll( self ):
        return tuple( x.roll() for x in self.dice )
    
class MakeDice( object ):
    def newDice( self, strategyChoice ):
        if strategyChoice == 1: 
            strat= DiceStrategy1()
        else: 
            strat= DiceStrategy2()
        return Dice( strat )
    

dice1 = Dice( DiceStrategy1() )
dice2 = Dice( DiceStrategy2() )
