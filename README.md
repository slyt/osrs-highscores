# OSRS-Highscores

This is a hobby data analytics project based on the Old School Runescape (OSRS) highscores.

It leverages the [osrs-highscores](https://pypi.org/project/osrs-highscores/) python package. Not to be confused with the [OSRS-Highscores](https://pypi.org/project/OSRS-Hiscores/) package which is not as fully features.

## Interesting points
There are no requirements to be shown on the HiScores other than being ranked in the top 2,000,000 players in a category.

Given that there are 25 usernames per highscore page, that means there are 2M / 25 = 80,000 pages of OSRS highscores.

The URL used to request highscores is in the format:
`https://secure.runescape.com/m=hiscore_oldschool/overall?table=1&page=80000`

Where table cooresponds with a cooresponding skill:
| Table index | Skill | 
| -- | ------ |
| 0 | Overall |
| 1 | Attack |
| 2 | Defence |
| 3 | Strength |
| 4 | Hitpoints |
| 5 | Ranged |
| 6 | Prayer |
| 7 | Magic |
| 8 | Cooking |
| 9 | Woodcutting |
| 10 | Fletching |
| 11 | Fishing |
| 12 | Firemaking |
| 13 | Crafting |
| 14 | Smithing |
| 15 | Mining |
| 16 | Herblore |
| 17 | Agility |
| 18 | Thieving |
| 19 | Slayer |
| 20 | Farming |
| 21 | Runecraft |
| 22 | Hunter |
| 23 | Construction |

Non-skill highscores are stored where `category_type=1`

## How to setup environment

1. Create a virtual environment: `python3 -m venv env`

2. Activate virtual environment:
- Window Powershell: `.\env\Scripts\activate`

3. Install dependencies: `pip install -r requirements.txt`

4. Run scripts or Jupyter Notebooks
