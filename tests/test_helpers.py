# Test helper functions
import helpers

# Generate the URL for the specific skill and page
helpers.request_page(skill='DeFENCE', page=1)

# TODO: Test rank_to_page_number()
ranks = [1, 2, 25, 26, 50, 51, 2_000_000, 1_999_999, 2_000_001, 9_999_999_999, 0, -1, -2_000_001]
for rank in ranks:
    page_number = helpers.rank_to_page_number(rank)
    print("Rank {} is on page {}".format(rank, page_number))


# Test helpers.page_number_to_rank_range
exit() # TODO: Remove to test
page_numbers = [0, 1, 2, 45, 80_000, -1, -349587, 80_001, 98435982094507]
for page_number in page_numbers:
    rank_range = helpers.page_number_to_rank_range(page_number=page_number)
    print("Page number {} has ranks {} to {}".format(page_number, rank_range[0], rank_range[1]))


