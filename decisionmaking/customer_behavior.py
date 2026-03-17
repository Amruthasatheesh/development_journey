"""

dispaly rating is <4.0 unsatisfied
dispaly rating is>=4.0 and <4.5 as neutral
otherwise satisfied

"""
rating=float(input("enter the rating:"))

if rating<4.0:#5<4.5
    print("unsatisfied")

elif rating>=4.0 and rating<4.5:#5>=4.5
     print("neutral")

else:
     print("satisfied")         # 5 satisfies the rating here


