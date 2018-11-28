from heapq import *
data = ["8",
        "NY DC 50 3 560 665 850",
        "NY Orlando 120 4 310 560 785 1225",
        "NY Chicago 120 3 520 750 1035",
        "Orlando Chicago 120 3 465 865 1120",
        "Orlando DC 95 3 480 970 1280",
        "Chicago Nashville 80 2 630 1030",
        "DC Nashville 90 2 600 1125",
        "Orlando NY 120 4 435 535 795 1180",
        "NY DC 270"]
data = ["8","NY DC 50 3 560 665 850","NY Orlando 120 4 310 560 785 1225","NY Chicago 120 3 520 750 1035","Orlando Chicago 120 3 465 865 1120","Orlando DC 95 3 480 970 1280","Chicago Nashville 80 2 630 1030","DC Nashville 90 2 600 1125","Orlando NY 120 4 435 535 795 1180","NY Atlanta 960"]
schedule = []
heap = []
for d in data[1:-1]:
    l = d.split()
    trip = {}
    trip["s"],trip["d"],trip["dr"] = l[:3]
    trip["dr"] = int(trip["dr"])
    trip["time"] = [int(x) for x in l[4:]]
    for t in trip["time"][:]:
        trip["time"].append(t+1440)
    schedule.append(trip)

start,destination,s_time= data[-1].split()
s_time = int(s_time)
shortest = None
# (how long, destination)
heap = [(trip["dr"]+min([t for t in trip["time"] if t > s_time])-s_time,trip["d"]) \
        for trip in schedule\
        if trip["s"] == start]
heapify(heap)
isImppossible = True
while len(heap) > 0:
    length, n_dest = heappop(heap)
    if n_dest == destination:
        isImppossible = False
        print(length)
        break
    n_time = length + s_time
    for trip in schedule:
        if trip["s"] == n_dest and \
                len([t for t in trip["time"] if t > n_time]) > 0:
            n_length = trip["dr"]+min([t for t in trip["time"] if t > n_time])-s_time
            heappush(heap, (n_length, trip["d"]))
if isImppossible:
    print("IMPOSSIBLE")






