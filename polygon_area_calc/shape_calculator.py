class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    def get_area(self):
        area = self.width * self.height
        return area

    def get_perimeter(self):
        perimeter = (2 * self.height) + (2 * self.width)
        return perimeter

    def get_diagonal(self):
        diagonal = (self.height ** 2 + self.width ** 2) ** 0.5
        return diagonal

    def get_picture(self):
        if self.width and self.height > 50 or self.width > 50 or self.height > 50:
            return "Too big for picture."

        picture = ""
        for A in range(self.height):
            line = '*' * self.width
            picture = picture + line + "\n"
        return picture

    def get_amount_inside(self, shape):
        w = self.width // shape.width
        h = self.height // shape.height
        amount = w * h
        return amount

    def __str__(self):
        return "Rectangle(width=" + str(self.width) + ", height=" + str(self.height) + ")"


class Square(Rectangle):

    def __init__(self, side, width, height):
        super().__init__(width, height)
        self.width = side
        self.height = side

    def set_side(self, side):
        self.width = side
        self.height = side

    def __str__(self):
        return "Square(side=" + str(self.width) + ")"
