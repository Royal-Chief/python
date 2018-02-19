golf_course = ['stone canyon','winterstone','shoal creek','tiffany greens']
print("Here are some of my favorite golf courses: \n" + golf_course[0].title() + "\n" + golf_course[1].title() + "\n" + golf_course[2].title() + "\n" + golf_course[3].title())
best_score = 76
worst_score = 99
good_round = "\nI played my best round at " + golf_course[3].title() + " with a score of " + str(best_score) + "."
bad_round = "\nI played my worst round at " + golf_course[0].title() + " with a score of " +str(worst_score) + "."
print(good_round)
print(bad_round)
print("\n" + golf_course[0].title() + " will be removed from my list.\n")
del golf_course[0]
print("Here are the remaining courses in order from best to worst: \n" + golf_course[2].title() + "\n" + golf_course[1].title() + "\n" + golf_course[0].title())