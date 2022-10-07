"""Module will create a graphic using the letter H."""


class Graphic:
    """Representation of an ASCII letter graphic."""

    def __init__(self, thickness: int, letter: str) -> None:
        """Initialize a Graphic type instance."""

        self.thickness = thickness
        self.letter = letter

        self.less_thick = thickness - 1
        self.more_thick = thickness + 1
        self.half_thick = self.more_thick // 2

        self.left_thick = thickness * 2
        self.right_thick = thickness * 6

        self.letters = letter * thickness
        self.middle_letters = self.letters * 5

        self.parts = (
            self.upper_top(),
            self.upper_mid(),
            self.middle(),
            self.lower_mid(),
            self.lower_bot()
        )

    def __len__(self):
        """Representation of Graphic type instance length."""

        return len(self.parts)

    def __iter__(self):
        """Representation of Graphic type instance iterable."""

        for part in self.parts:
            yield part

    def __str__(self):
        """Representation of Graphic type instance string."""

        return "\n".join(self)

    def upper_top(self):
        """Create the top cone of the graphic."""

        # number of iterations
        loop_count = self.thickness

        layers = []
        for index in range(loop_count):

            # graphic layer data
            thick = self.letter * index
            right = thick.rjust(self.less_thick)
            left = thick.ljust(self.less_thick)
            layer = right + self.letter + left

            layers.append(layer)

        string = "\n".join(layers)

        return string

    def upper_mid(self):
        """Create the top pillar of the graphic."""

        # number of iterations
        loop_count = self.more_thick

        layers = []
        for _ in range(loop_count):

            # graphic layer data
            left = self.letters.center(self.left_thick)
            right = self.letters.center(self.right_thick)
            layer = left + right

            layers.append(layer)

        string = "\n".join(layers)

        return string

    def middle(self):
        """Create the middle of the graphic"""

        # number of iterations
        loop_count = self.half_thick

        layers = []
        for _ in range(loop_count):

            # graphic layer data
            layer = self.middle_letters.center(self.right_thick)

            layers.append(layer)

        string = "\n".join(layers)

        return string

    def lower_mid(self):
        """Create the bottom pillar of the graphic"""

        # number of iterations
        loop_count = self.more_thick

        layers = []
        for _ in range(loop_count):

            # graphic layer data
            left = self.letters.center(self.left_thick)
            right = self.letters.center(self.right_thick)
            layer = left + right

            layers.append(layer)

        string = "\n".join(layers)

        return string

    def lower_bot(self):
        """Create the bottom cone of the graphic"""

        # number of iterations
        loop_count = self.thickness

        layers = []
        for index in range(loop_count):

            # graphic layer data
            width = self.less_thick - index
            letters = self.letter * width
            left = letters.rjust(self.thickness)
            right = letters.ljust(self.thickness)
            layer_raw = left + self.letter + right
            layer = layer_raw.rjust(self.right_thick)

            layers.append(layer)

        string = "\n".join(layers)

        return string


def main():
    """Provides input for functions"""

    thickness = int(input())
    letter = "H"

    graphic = Graphic(thickness, letter)
    print(graphic)


if __name__ == '__main__':
    main()
