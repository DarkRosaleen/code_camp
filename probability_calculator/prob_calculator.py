import copy
import random


class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for key, value in kwargs.items():
            for a in range(value):
                self.contents.append(key)

    def draw(self, amount):
        draw_list = []
        if amount >= len(self.contents):
            return self.contents
        for i in range(amount):
            name = self.contents.pop(random.randrange(len(self.contents)))
            draw_list.append(name)
        return draw_list


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    final_count = 0
    for _ in range(num_experiments):
        copy_hat = copy.deepcopy(hat)
        temp_list = copy_hat.draw(num_balls_drawn)
        success = True
        for key, value in expected_balls.items():
            if temp_list.count(key) < value:
                success = False
                break
        if success:
            final_count += 1
    probability = final_count / num_experiments
    return probability
