"""Print out all the melons in our inventory."""


from melons import melon_info


def print_melon(melon_info):
    """Print each melon with corresponding attribute information."""

for melon, items in melon_info.items():
    print(melon.upper())
    for item, value in items.items():
        print(f"{item}: {value}")