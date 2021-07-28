import random
min = 1
max = 100
def num_gen():
    for _ in range(1):
        value = int(randint(min, max))
        if 0 < value <= 25:
            token = "Zebra"
        elif 25 < value <= 50:
            token = "Horse"
        elif 50 < value <= 90:
            token = "😢😢 Donkey 😢😢"
        elif 90 < value <= 100:
            token = "🦄🦄 Unicorn 🦄🦄"


