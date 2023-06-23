"""
A program that implements the Rosenberg self-esteem scale.
"""

def main():
    questions = [
        ('I feel that I am a person of worth, at least on an equal plane with others.', True),
       ( 'I feel that I have a number of good qualities.', True),
        ('All in all, I am inclined to feel that I am a failure.', False),
        ('I am able to do things as well as most other people.', True),
       ( 'I feel I do not have much to be proud of.', False),
        ('I take a positive attitude toward myself.', True),
        ('On the whole, I am satisfied with myself.', True),
       ( 'I wish I could have more respect for myself.', False ),
        ('I certainly feel useless at times.', False),
        ('At times I think I am no good at all.', False)
        ]
    score = 0
    for number, (question, positive) in enumerate(questions):
        print(f"{number + 1}. {question}")
        response = str(input("   Enter D, d, a, or A: "))
        if response.lower() not in ['d', 'a']:
            raise Exception('Enter a valid letter')
        score += compute_score(response, positive)
    
    print(f"\nYour Score is {score}.")
    print("A score below 15 may indicate problematic low self-esteem.")


def compute_score(letter: str, postive: True):
    """
    Compute score for an answer
    Parameters:
        letter: answer from user
        positive: True if statement of the answer is positive else False
    Returns: score
    """
    match letter:
        case 'D':
            return 0 if postive else 3
        case 'd':
            return 1 if postive else 2
        case 'a':
            return 2 if postive else 1
        case 'A':
            return 3 if postive else 0


if __name__ == "__main__":
    main()