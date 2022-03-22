# OSRS-Highscores

This is a hobby data analytics project based on the Old School Runescape (OSRS) highscores.




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

## API Parsing

It is possible to scrape the Old School Runescape highscores by parsing the HTML into a Pandas dataframe with:
```Python
import requests
import pandas as pd

base_url = "https://secure.runescape.com/m=hiscore_oldschool/overall"
skill_index = 1 # 1 = Attack
page = 1        # 1 = Frontpage

request_url = base_url + '?table=' + str(skill_index) + '&' + 'page=' + str(page)
response = requests.get(request_url)

df_list = pd.read_html(response.text, skiprows={0,0}) # For some reason row 0 was all NA, so need to skip
df = df_list[0]
df.index += 1 # 1 index instead of 0 to match highscore indexing
df.columns = ['Rank', 'Name', 'Level', 'XP']
print(df)
```

Output:
```
    Rank          Name  Level         XP
1      1          Heur     99  200000000
2      2    Unohdettu2     99  200000000
3      3        Drakon     99  200000000
4      4   Ame Umehara     99  200000000
5      5         Jakee     99  200000000
6      6       Ursadon     99  200000000
7      7        Howson     99  200000000
8      8      Dr PFAFF     99  200000000
9      9  Malt Lickeys     99  200000000
10    10        Burned     99  200000000
11    11    Blue Limes     99  200000000
12    12  Mini Finbarr     99  200000000
13    13    Unohdettu3     99  200000000
14    14      Eslihero     99  200000000
15    15    Lynx Titan     99  200000000
16    16  AndrewWigins     99  200000000
17    17        iMelee     99  200000000
18    18    Portuguese     99  200000000
19    19     MarkoOSRS     99  200000000
20    20         Cairo     99  200000000
21    21      Hey Jase     99  200000000
22    22       H D M P     99  200000000
23    23        Yumemi     99  200000000
24    24        Fiiggy     99  200000000
25    25   Edgecrusher     99  200000000
```

A JSON API exists, but unfortunately the it only shows up to the top 50 players and does not appear to support pageination:

- Front page of attack: `https://secure.runescape.com/m=hiscore_oldschool/ranking.json?m=&table=1&category=0&size=25`
- Top 50 players for attack: `https://secure.runescape.com/m=hiscore_oldschool/ranking.json?m=&table=1&category=0&size=25`
- Accessing a specific page does not work: `https://secure.runescape.com/m=hiscore_oldschool/ranking.json?m=&table=1&category=0&size=25&page=999`

So in order to scrape the entire OSRS highscores, we are left witih the only option: parse HTML, 25 entries at a time.

## Runtime analysis
For a single skill, if we request one page (25 skills) per second, it will take 80,000 seconds ~= 1,333.33 minutes ~= 22.22 hours ~= 0.92 days.

So for 23 skills + overall highscores, it will take about 24 days ~= almost a month to scrape the entire skills highscores.

This can be sped up via making parallel requests thus increasing the request speed. 

Also, instead of scraping the entire population of 2 Million, we can randomly sample a subset of the population. We can also search for "points of interest" within the dataset, for example, try to find the pages where levels transition and extrapolate between them.

## See Also
- OSRS API reference from Wiki: https://runescape.wiki/w/Application_programming_interface
- OSRS API reference for Google Sheets: https://sites.google.com/view/runescapeassistsheets/runescape-api
- [osrs-highscores](https://pypi.org/project/osrs-highscores/) python package (_Note: This library was lacking in that it could only access data per user, not per page of a skill_). Not to be confused with the [OSRS-Highscores](https://pypi.org/project/OSRS-Hiscores/) package which is not as fully features.