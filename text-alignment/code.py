"""Module will create a graphic using the letter H."""


def top_cone(thickness, letter):
    """Create the top cone of the graphic."""

    width = thickness - 1

    layers = []
    for index in range(thickness):
        thick = letter * index
        right = thick.rjust(width)
        left = thick.ljust(width)

        layer = right + letter + left
        layers.append(layer)

    string = "\n".join(layers)

    return string


def top_pillar(thickness, letter):
    """Create the top pillar of the graphic."""

    width = thickness * 2
    height = thickness * 6

    layers = []
    for _ in range(thickness + 1):
        letters = letter * thickness

        layer = letters.center(width) + letters.center(height)
        layers.append(layer)

    string = "\n".join(layers)

    return string


def mid_belt(thickness, letter):
    """Create the middle of the graphic"""

    width = thickness * 6

    layers = []
    for _ in range((thickness+1)//2):
        letters = letter * thickness * 5

        layer = letters.center(width)
        layers.append(layer)

    string = "\n".join(layers)

    return string


def bot_pillar(thickness, letter):
    """Create the bottom pillar of the graphic"""

    width = thickness * 2
    height = thickness * 6

    layers = []
    for _ in range(thickness + 1):
        letters = letter * thickness

        layer = letters.center(width) + letters.center(height)
        layers.append(layer)

    string = "\n".join(layers)

    return string


def bot_cone(thickness, letter):
    """Create the bottom cone of the graphic"""

    height = thickness * 6

    layers = []
    for index in range(thickness):
        width = thickness - index - 1
        letters = letter * width
        right = letters.rjust(thickness)
        left = letters.ljust(thickness)
        botcone = right + letter + left

        layer = botcone.rjust(height)
        layers.append(layer)

    string = "\n".join(layers)

    return string


def draw(thickness, letter):
    """Create the graphics based on the parts"""

    parts = [
        top_cone(thickness, letter),
        top_pillar(thickness, letter),
        mid_belt(thickness, letter),
        bot_pillar(thickness, letter),
        bot_cone(thickness, letter)
    ]
    string = "\n".join(parts)

    print(string)


def main():
    """Provides input for functions"""

    thickness = int(input())
    letter = "H"

    draw(thickness, letter)


if __name__ == '__main__':
    main()
