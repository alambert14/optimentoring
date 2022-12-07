import numpy as np


def generate_random_schedule():
    percentage = np.random.uniform(.2, .8)
    schedule = np.random.choice([0, 1], 210, p=[1-percentage, percentage])
    return [str(avail) for avail in schedule]

    

if __name__ == '__main__':
    print(', '.join(generate_random_schedule()))
