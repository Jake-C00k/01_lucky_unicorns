from random import randint

def num_gen():
    for _ in range(1):
        value = int(randint(1, 100))
        if 0 < value <= 25:
            token = "Zebra"
        elif 25 < value <= 50:
            token = "horse"
        elif 50 < value <= 90:
            token = "donkey"
        elif 90 < value <= 100:
            token = "unicorn"
    print("You got a {}".format(token))

while True:
    num_gen()
