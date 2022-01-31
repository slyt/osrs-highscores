# OSRS-Highscores

This is a hobby data analytics project based on the Old School Runescape (OSRS) highscores.

It leverages the [osrs-highscores](https://pypi.org/project/osrs-highscores/) python package. Not to be confused with the [OSRS-Highscores](https://pypi.org/project/OSRS-Hiscores/) package which is not as fully features.


## How to setup environment

1. Create a virtual environment: `python3 -m venv env`

2. Activate virtual environment:
- Window Powershell: `.\env\Scripts\activate`

3. Install dependencies: `pip install -r requirements.txt`

4. Run scripts or Jupyter Notebooks

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

Non-skill highscores are stored where `category_type=1`. For example, Clue Scroll (hard) is at `https://secure.runescape.com/m=hiscore_oldschool/overall?category_type=1&table=7#headerHiscores`

| Table index | Table Name | 
| -- | ------ |
| 1 | Bounty Hunter - Hunter           |
| 2 | Bounty Hunter - Rogue            |
| 3 | Clue Scrolls (all)               |
| 4 | Clue Scrolls (beginner)          |
| 5 | Clue Scrolls (easy)              |
| 6 | Clue Scrolls (medium)            |
| 7 | Clue Scrolls (hard)              |
| 8 | Clue Scrolls (elite)             |
| 9 | Clue Scrolls (master)            |
| 10 | LMS - Rank                       |
| 11 | Soul Wars Zeal                   |
| 12 | Abyssal Sire                     |
| 13 | Alchemical Hydra                 |
| 14 | Barrows Chests                   |
| 15 | Bryophyta                        |
| 16 | Callisto                         |
| 17 | Cerberus                         |
| 18 | Chambers of Xeric                |
| 19 | Chambers of Xeric: Challenge Mode|
| 20 | Chaos Elemental                  |
| 21 | Chaos Fanatic                    |
| 22 | Commander Zilyana                |
| 23 | Corporeal Beast                  |
| 24 | Crazy Archaeologist              |
| 25 | Dagannoth Prime                  |
| 26 | Dagannoth Rex                    |
| 27 | Dagannoth Supreme                |
| 28 | Deranged Archaeologist           |
| 29 | General Graardor                 |
| 30 | Giant Mole                       |
| 31 | Grotesque Guardians              |
| 32 | Hespori                          |
| 33 | Kalphite Queen                   |
| 34 | King Black Dragon                |
| 35 | Kraken                           |
| 36 | Kree'Arra                        |
| 37 | K'ril Tsutsaroth                 |
| 38 | Mimic                            |
| 39 | Nex                              |
| 40 | Nightmare                        |
| 41 | Phosani's Nightmare              |
| 42 | Obor                             |
| 43 | Sarachnis                        |
| 44 | Scorpia                          |
| 45 | Skotizo                          |
| 46 | Tempoross                        |
| 47 | The Gauntlet                     |
| 48 | The Corrupted Gauntlet           |
| 49 | Theatre of Blood                 |
| 50 | Theatre of Blood: Hard Mode      |
| 51 | Thermonuclear Smoke Devil        |
| 52 | TzKal-Zuk                        |
| 53 | TzTok-Jad                        |
| 54 | Venenatis                        |
| 55 | Vet'ion                          |
| 56 | Vorkath                          |
| 57 | Wintertodt                       |
| 58 | Zalcano                          |
| 59 | Zulrah                           |
