from math import prod


def dist(nsec_held, race_duration):
    return nsec_held * (race_duration - nsec_held)




with open("input6.txt") as f:
    for line in f:
        if "Time" in line:
            times = [int(x) for x in line.split(":")[-1].split()]
        if "Distance" in line:
            distances = [int(x) for x in line.split(":")[-1].split()]


races = zip(times, distances)
nwinners = []

for t, d in races:
    xs = range(t + 1)
    ds = []
    for x in xs:
        ds.append(dist(x, t))
    winners = [a for a in ds if a > d]
    nwinners.append(len(winners))

print(prod(nwinners))