def distance(p1, p2):
    return ((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)**0.5

def stripClosest(strip, d, p1, p2):
    min_dist = d
    closest_pair = (p1, p2)
    strip = sorted(strip, key = lambda x: x[1])
    for i in range(len(strip)):
        for j in range(i+1, len(strip)):
            if (strip[j][1] - strip[i][1]) >= min_dist:
                break
            if distance(strip[i], strip[j]) < min_dist:
                min_dist = distance(strip[i], strip[j])
                closest_pair = (strip[i], strip[j])
    return closest_pair[0], closest_pair[1], min_dist

def closest_pairs(points):
    if len(points) == 2:
        d = distance(points[0], points[1])
        return points[0], points[1], d
    elif len(points) == 3:
        d1 = distance(points[0], points[1])
        d2 = distance(points[1], points[2])
        d3 = distance(points[2], points[0])
        if d1<=d2 and d1<=d3:
            return points[0], points[1], d1
        elif d2<=d1 and d2<=d3:
            return points[1], points[2], d2
        else:
            return points[2], points[0], d3
    else:
        points = sorted(points, key = lambda x: x[0])
        mid = len(points)//2
        midpoint = points[mid]
        lp1, lp2, dl = closest_pairs(points[:mid])
        rp1, rp2, dr = closest_pairs(points[mid:])
        d = 0
        closest_pair = ()
        if dl<dr:
            d = dl
            closest_pair = (lp1,lp2)
        else:
            d = dr
            closest_pair = (rp1,rp2)

        strip = []
        for i in range(len(points)):
            if abs(points[i][0] - midpoint[0]) < d:
                strip.append(points[i])

        strip1, strip2, strip_dist = stripClosest(strip, d, closest_pair[0], closest_pair[1])

        if d <= strip_dist:
            return closest_pair[0], closest_pair[1], d
        else:
            return strip1, strip2, strip_dist

        

l = [(1,2),(3,5),(6,9),(8,12),(10,15)]
print("List: ", l)
p1, p2, d = closest_pairs(l)
print("The Closest Pairs: ", p1, ", ", p2)
