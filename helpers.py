# helper functions

from email.mime import base


base_url = "https://secure.runescape.com/m=hiscore_oldschool/overall"

default_skills = {
    "overall":0,
    "attack":1,
    "defence":2,
    "strength":3,
    "hitpoints":4,
    "ranged":5,
    "prayer":6,
    "magic":7,
    "cooking":8,
    "woodcutting":9,
    "fletching":10,
    "fishing":11,
    "firemaking":12,
    "crafting":13,
    "smithing":14,
    "mining":15,
    "herblore":16,
    "agility":17,
    "thieving":18,
    "slayer":19,
    "farming":20,
    "runecraft":21,
    "hunter":22,
    "construction":23,
}

def request_page(skill='overall', page=1):

    skill_index = default_skills.get(skill.lower(), -1)
    if skill_index == -1:
        print("Error, invalid skill name supplied!")
    print("Requesting skill {} (skill_index {}) page {}".format(skill, skill_index, page))

    request_url = base_url + '?table=' + str(skill_index) + '&' + 'page=' + str(page)
    print('request_url: ', request_url)

def page_number_to_rank_range(page_number=1):
    # 1 = (1,25) 25-1 = 24
    # 2 = (26, 50) 50-26 = 24

    if page_number > 80_000 or page_number < 0:
        print("Error, page_number must be between 0 and 80,000. 0 and 1 are treated as the same page.")
        return (-1,-1)

    if page_number == 0: # 0 and 1 are treated the same page index on highscores
        page_number = 1
    last_rank_on_page = page_number * 25
    first_rank_on_page = last_rank_on_page - 24

    return (first_rank_on_page, last_rank_on_page)

def rank_to_page_number(rank):
    # 1 = page 1
    # 25 = page 1
    # 26 = page 2
    # 50 = page 2
    page_number = rank % 25 # 25 ranks per page
    return page_number




