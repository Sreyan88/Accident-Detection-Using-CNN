def convert_to_numeric(score):
    converted_score = float(score)
    return converted_score
def sum_of_middle_three(score1,score2,score3,score4,score5):
    maximum = max(score1,score2,score3,score4,score5)
    minimum = min(score1,score2,score3,score4,score5)
    return (score1+score2+score3+score4+score5-maximum-minimum)
def score_to_rating_string(average_score):
    if(average_score >=0 and average_score < 1):
        return "Terrible"
    if(average_score >=1 and average_score<2):
        return "Bad"
    if(average_score >=2 and average_score<3):
        return "OK"
    if(average_score >=3 and average_score<4):
        return "Good"
    if(average_score >=4 and average_score<=5):
        return "Excellent"
def scores_to_rating(score1,score2,score3,score4,score5):
    """
    Turns five scores into a rating by averaging the
    middle three of the five scores and assigning this average
    to a written rating.
    """
    #STEP 1 convert scores to numbers
    score1 = convert_to_numeric(score1)
    score2 = convert_to_numeric(score2)
    score3 = convert_to_numeric(score3)
    score4 = convert_to_numeric(score4)
    score5 = convert_to_numeric(score5)

    #STEP 2 and STEP 3 find the average of the middle three scores
    average_score = sum_of_middle_three(score1,score2,score3,score4,score5)/3

    #STEP 4 turn average score into a rating
    rating = score_to_rating_string(average_score)

    return rating

a= scores_to_rating(1,1,1,1,1)
print(a)
