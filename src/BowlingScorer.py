def calc_scores(scores):
    scores_by_frame = scores.split("-")
    len_last_frame = len(scores_by_frame[-1])
    # throws is a list that stores the number of pins knocked down at each throw
    throws = list("".join(scores_by_frame))
    total_score = 0

    # Iterate across throws backwards
    for i in range(len(throws) - 1, -1, -1):
        # If current throw is a strike, give score of 10 plus num pins knocked down in next two throws
        if throws[i] == "X":
            throws[i] = 10
            if i < len(throws) - len_last_frame:
                total_score += int(throws[i + 1]) + int(throws[i + 2])
        # If current throw is a spare, give score of remainder plus num pins knocked down in next throw
        elif throws[i] == "/":
            throws[i] = 10 - int(throws[i - 1])
            if i < len(throws) - 1:
                total_score += int(throws[i + 1])
        # Num pins knocked in current throw is added to the total score
        total_score += int(throws[i])
    return total_score


# List of Scores for Testing Purposes
score_List = ["X-X-X-X-X-X-X-X-X-XXX", "45-54-36-27-09-63-81-18-90-72", '3/-7/-1/-8/-7/-8/-3/-5/-5/-5/',
              'X-X-X-X-X-X-X-X-X-X3/', "X-5/-X-8/-X-9/-X-2/-X-X3/"]
for score in score_List:
    print("The score for %s is %d" % (score, calc_scores(score)))
