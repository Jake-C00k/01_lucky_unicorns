from random import randint

min = 1
max = 100


def num_gen():
    for _ in range(1):
        value = int(randint(min, max))
        if 0 < value <= 25:
            token = "Zebra"
            statement = "Not bad, could be worse"
        elif 25 < value <= 50:
            token = "Horse"
            statement = "Not bad, could be worse"
        elif 50 < value <= 90:
            token = "😢😢 Donkey 😢😢"
            statement = "Unlucky, hopefully you do better next time"
        elif 90 < value <= 100:
            token = "🦄🦄 Unicorn 🦄🦄"
            statement = "Wow, that's fantastic, you really won big!"
    print("Generating token...")
    print("You got a {}".format(token))
    print(statement)

