from utils.reels import reel_1, reel_2, reel_3

# slot combinations that result in wins
rewards = {"seven, seven, seven": 200,
           "bar, bar, bar": 100,
           "melon, melon, melon": 100,
           "melon, melon, bar": 100,
           "bell, bell, bell": 18,
           "bell, bell, bar": 18,
           "orange, orange, orange": 14,
           "orange, orange, bar": 14,
           "duck, duck, duck": 10,
           "duck, duck, bar": 10,
           "cherries": 5,
           "cherry": 2}

# iterates through all 3 reels to create all 8000 (20**3) combinations
combos = []
for i in reel_1:
    for j in reel_2:
        for k in reel_3:
            combos.append([i, j, k])

# sums the winning pots across all combinations
overall_winnings = 0
for combo in combos:
    if ", ".join(combo) in rewards:
        overall_winnings += rewards[", ".join(combo) ]
    elif combo[0] == "cherry" and combo[1] == "cherry":
        overall_winnings += rewards["cherries"]
    elif combo[0] == "cherry":
        overall_winnings += rewards["cherry"]

    
print(len(combos))
print(overall_winnings)
# this value is the win rate for the customer (hopefully less than 1)
print(overall_winnings/len(combos))