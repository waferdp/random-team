# random-team #
Team randomizer for remote daliy standup
Many scrum masters will observe that non-developers like to talk during daily standup.
Sometimes the non-developers will talk more than the developers themselves. 
The daily standup is a meeting for the team to self-organize.
There is a risk that completely shutting the door for non-developers expands an already existing gap between "business people and developers". This script will always prioritize developers first.

## Setup ##
Copy "config_template.json" to "config.json", change team member names to appropriate ones

## config.json ##

### developers ###
The developers list holds a list of developer names, these names will always be part of the result

### dynamic ###
The dynamic list contains Scrum Master and PO, as well as any team stakeholders. 

### developer or dynamic? ###
The rule of thumb is: "Is the person making working with the teams sprint backlog"?
If they are, they are in the developer list, if they are not, they should be in the dynamic list.

### special case: Scrum master sometimes does backlog work ###
It's not unusual that scrum masters are split between developer and scrum master.
This means they are sometimes working with something other than the sprint goal.
Make sure this persons name is in both developer and dynamic lists.
Any name listed in both developers and dynamic will only appear once in the randomized result.

## Running ##

### Basic ###
```python team.py```
Will print a list with randomized order from the list of developers

### Advanced ###
Consider the list in config_template.json
```python team.py gc```
Will print two lists, one for developers, and one from given dynamic members.
'g' will match "Garrison", and 'c' will match Chef. 

```python team.py s```
In this case, "Stan" is both developer and dynamic. The logic of the script is that names given as arguments should always end up in the dynamics list, so Stan will be listed as dynamic (and not as a developer).
If 's' had been omitted, Stan would have been in the developers list.