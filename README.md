# Jeopardy ToC Probability Computer

Right now, there are 4 parameters:

1. The number of wins that your favorite champ has right now (`CHAMP_WINS`)
2. The number of regular Jeopardy! games left before the next ToC (`GAMES_LEFT`)
3. The probability that your favorite champ will be passed (in dollars) 
   by someone with the same number of wins (`PROBABILITY_CHAMP_WON_LESS_MONEY_WITH_SAME_VICTORIES`)
4. The maximum number of new champions who could pass your favorite champ (`MAX_STRONGER_CHAMPS_TO_REMAIN_ELIGIBLE`)
   for them to still remain eligible for the ToC.


For example, if your favorite champ is in 10th place, and there's a teachers champion and a college champ,
then potentially there are 13 spots available to regular Jeopardy! contestants. That means that there
could be at most 2 more champions from regular Jeopardy! for your favorite champ to remain eligible.