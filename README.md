## Bowling Coding Challenge


### My Solution

My solution includes the following testcases with a good mix of Strikes and Spares in order to test for edge cases:
- X-X-X-X-X-X-X-X-X-XXX
- 5-54-36-27-09-63-81-18-90-72
- 3/-7/-1/-8/-7/-8/-3/-5/-5/-5/
- X-X-X-X-X-X-X-X-X-X3/
- X-5/-X-8/-X-9/-X-2/-X-X3/


Additional cases can be added by adding to the score_List

## To Run 
- CD into the src directory 
- On Python version less than 3 use ``` python BowlingScorer.py```
- On Python version higher than 3 use ``` python3 BowlingScorer.py```

### Problem Description

Create a program, which, given an integer array of a valid sequence of throws for one game
of American Ten-Pin Bowling, produces the total score for the game. Your code will become
the core of a bowling score management system, so make sure it’s production-quality.
Your input should be a string like the examples below.

Stuff That’s Out of Scope
Here are some things that the program does not need to do (today):

* check for valid throws (like scores that add to 11)

* check for the correct number of throws and frames

* provide any intermediate scores – it only has to provide the final score

The Rules
To briefly summarize the scoring for this form of bowling:

* One game of bowling is made up of ten frames.

* In each frame, the bowler has two throws to knock down all the pins.

## Possible results for a frame:

* Strike (‘X’): the bowler knocks down all 10 pins on the first throw.
The frame is over early. The score for the frame is 10 plus the total pins
knocked down on the next two throws.

* Spare (‘/’): the bowler knocks down all 10 pins using two throws.
The score for the frame is 10 plus the number of pins knocked down on the
next throw.

* Open frame: the bowler knocks down less than 10 pins with his two throws.
The score for the frame is the total number of pins knocked down.

* The game score is the total of all frame scores.

## Special rules for the 10thframe:

* A strike in the tenth frame gives the bowler two bonus throws, to fill out the
scoring formula for the last frame.

* A spare in the tenth frame gives the bowler one bonus throw, to fill out the
scoring formula for the last frame.

* These throws count as part of the 10th frame.

* The process does not repeat – for example, knocking down all 10 pins on a
bonus throw does not provide any additional bonus throws.
