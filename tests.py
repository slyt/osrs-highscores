# Test functions

import helpers

helpers.request_page(skill='DeFENCE', page=1)



# Test helpers.page_number_to_rank_range
exit() # TODO: Remove to test
page_numbers = [0, 1, 2, 45, 80_000, -1, -349587, 80_001, 98435982094507]
for page_number in page_numbers:
    rank_range = helpers.page_number_to_rank_range(page_number=page_number)
    print("Page number {} has ranks {} to {}".format(page_number, rank_range[0], rank_range[1]))


