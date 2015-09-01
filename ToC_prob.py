EMPIRICAL_PROBS = \
    [0,
     0.558510638,
     0.260638298,
     0.079787234,
     0.015957447,
     0.053191489,
     0.015957447,
     0.005319149,
     0,
     0,
     0,
     0.010638298]

SMOOTHED_PROBS = [0, .54, .26, .08, .05, .03, .015, .005, .005, .005, .01]
CHAMP_WIN_PROBS = EMPIRICAL_PROBS

assert sum(CHAMP_WIN_PROBS) == 1

MY_WINS = 3
BIGGER_THAN_MY_WIN_PROB = 0.1
GAMES_LEFT = 100
MAX_WINNERS_TO_REMAIN_ELIGIBLE = 1
TOTAL_SITUATIONS = MAX_WINNERS_TO_REMAIN_ELIGIBLE + 2

import numpy as np

output_array = np.zeros((GAMES_LEFT, TOTAL_SITUATIONS))
output_array[0][0] = 1
# print output_array

for i in range(GAMES_LEFT - 1):
    for j in range(len(CHAMP_WIN_PROBS)):
        win_prob = CHAMP_WIN_PROBS[j]
        for k in range(TOTAL_SITUATIONS):
            if i + j >= GAMES_LEFT:
                if j > MY_WINS and i + MY_WINS < GAMES_LEFT:
                    output_array[-1][min(k + 1, TOTAL_SITUATIONS - 1)] += \
                        output_array[i][k] * win_prob
                else:
                    output_array[-1][k] += \
                        output_array[i][k] * win_prob
            elif j <= MY_WINS - 1:
                output_array[i + j][k] += \
                    output_array[i][k] * win_prob
            elif j == MY_WINS:
                output_array[i + j][k] += \
                    output_array[i][k] * win_prob * (1.0 - BIGGER_THAN_MY_WIN_PROB)
                output_array[i + j][min(k + 1, TOTAL_SITUATIONS - 1)] += \
                    output_array[i][k] * win_prob * BIGGER_THAN_MY_WIN_PROB
            else:
                output_array[i + j][min(k + 1, TOTAL_SITUATIONS - 1)] += \
                    output_array[i][k] * win_prob
                # print i
                # print output_array

# print output_array
output_probs = output_array[-1]
assert abs(output_probs.sum() - 1) < .001

output_range = range(TOTAL_SITUATIONS)

format_str = 'Probability of {}{} additional winners in the next {} games: {:.2%}'

output_range_names = [format_str.format(i, '', GAMES_LEFT, output_probs[i]) for i in output_range[:-1]]
output_range_names += [format_str.format(output_range[-1], ' or more', GAMES_LEFT, output_array[-1][-1])]

print '\n'.join(output_range_names)
print '\n=============\n'
print 'ToC Probability: {:.2%}'.format(output_probs[:-1].sum())
