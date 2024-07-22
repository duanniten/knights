from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
    Or(AKnight, AKnave),
    Not(And(AKnight, AKnave)),


    Or(AKnave, And(AKnight,AKnave))
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    Or(AKnight, AKnave),
    Or(BKnight, BKnave),
    Or(And(AKnave, BKnave), AKnave),
    Implication(AKnave, BKnight)
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    Or(AKnight, AKnave),
    Or(BKnight, BKnave),
    Implication(AKnight, And(AKnight, BKnight)),
    Biconditional(BKnight, AKnave),

)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    Or(AKnight, AKnave), # A is a Knight or a Knave
    Not(And(AKnight, AKnave)),
    
    Or(BKnight, BKnave), # B is a Knight or a Knave
    Not(And(BKnight, BKnave)),
    
    Or(CKnight, CKnave), # C is a Knight or a Knave
    Not(And(CKnight, CKnave)),

    Or(
        And(CKnight, AKnight),   #If C is a Knight A is a Knight
        And(CKnave, AKnave)      #If C is a Knave A is a Knave
    ),

    Or(
        And(BKnight, CKnave),   #If B is Knight C is a Knave 
        And(CKnight, BKnave)   #If B is Knight C is a Knave
    ),

    Or(
        And(BKnight, And(AKnight, AKnave)),
        BKnave
    )

)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
