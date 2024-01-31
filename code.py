from collections import defaultdict
def noOfIntersections(inputs):
    #Edge case
    if len(inputs) == 0:
        return 0

    source = defaultdict(int)
    destination = defaultdict(int)

    # Mapping the radian measures with the start and end chords
    for a, b in zip(inputs[0], inputs[1]):
        if 's' in b:
            source[int(b[1:])] = a
        elif 'e' in b:
            destination[int(b[1:])] = a

    # Edge case
    if len(source) != len(destination):
        return 0

    # Creating a list of chords with each chord represented as (start, end).
    # To simplify number of cases, chords are now stored as the start point being less than end.
    chords = []
    for s_index in source:
        if s_index in destination:
            minimum = min(source[s_index], destination[s_index])
            maximum = max(source[s_index], destination[s_index])
            chords.append([minimum, maximum])

    # Sorting the chords with key as the start of the chord
    chords.sort()

    #Finding the number of intersections
    count = 0
    for i in range(len(chords)):
        end = chords[i][1]
        for s_j, e_j in chords[i+1:]:
            if end < s_j:
                break
            if s_j < end and end < e_j:
                count += 1
    return count

if __name__ == '__main__':
    inputs=[]
    #inputs=[(0.78, 0.88, 1.77, 1.74), ("s1", "s2", "e1", "e2")]
    #inputs=[(0.9, 1.3, 1.70, 2.92), ("s1", "e1", "s2", "e2")]
    #inputs=[(0.78, 1.47, 1.77, 3.92), ("s1", "s2", "e1", "e2")]
    #inputs=[(0.78, 0.88, 1.77, 1.74), ("s1", "s2", "e1", "e2")]
    #inputs=[(0.9, 1.3, 1.70, 2.92), ("s1", "e1", "s2", "e2")]
    #inputs=[(1, 2, 3, 2.50, 3, 4), ("s1", "s2", "e1", "e2", "s3", "e3")]
    #inputs=[(0.78, 1.47, 1.77, 3.92, 1.80, 4.50, 0.88, 1.74), ("s1", "s2", "e1", "e2", "s3", "e3", "s4", "e4")]
    #inputs=[(0.78, 1.47, 1.77, 3.92, 1.80, 4.50, 0.88, 1.74), ("s1", "e2", "e1", "s2", "s3", "e3", "s4", "e4")]
    #inputs=[(0.78, 1.47, 1.77, 3.92, 1.80, 2.30, 0.88, 1.74), ("s1", "s2", "e1", "e2", "s3", "e3", "s4", "e4")]
    print("The number of intersections is: {}".format(noOfIntersections(inputs)))