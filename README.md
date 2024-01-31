# Structify-TakeHome
Code for Stuctify Take Home Assessment
## **Algorithm**
1. First create two hashmaps - source and destination from the two lists provided in the input array. Each of these hashmaps have the  identifier as the key and radian measure as the value.
2. Using the hashmaps create a list of chords as `[start, end]` and each chord is setup such that the start point is less than the end.
3. Next, sort this array of chords. Since this is a 2-tuple, it is sorted by the first element of the tuple. In this case it is the start point of the chord.
4. Next traverse through these chords by using the end point of the current chord for comparison.
5. Use a nested loop to traverse through the following chords in the array. Since the chords are sorted in ascending order, the start point of the following chords will be greater than the start point of the current chord. 
6. If the start point of the chosen following chord is less than the end point of the current chord. And, the end point of the chosen following chord is greater than the end point of the current chord, increment count by 1 as there is an intersection.
7. If the start point of the chosen following chord is greater than the end point of the current chord that means it is out of the range of the current chord and there can be no further intersections so break out of the inner loop. There is no point checking the further chords since the start points for them will be greater than the chosen chord. 


## **Execution Steps**
1. Execute the code using the command `python code.py`.
2. In main there are different test cases in the main function, those can be changed or uncommented to see the test results.


## **Time Complexity**

The time complexity of the code is 0(n<sup>2</sup>) where n is the size of the input array.

In order to create the mapping of the start and end of the chord to its radian measures the time complexity is 0(n). 

Next I sorted these chords by the using starting point of the chord as the key. Time complexity for that is 0(nlogn).

When traversing through the chords array, I used nested for loop and the time complexity for that is 0(n)*0(n-1) which is 0(n<sup>2</sup>).

So, the total time complexity is 0(n) + 0(nlogn) + 0(n<sup>2</sup>) = 0(n<sup>2</sup>).

## **Space Complexity**

I have used two dictionaries, chords array and the count variable so the space complexity is 0(3n) + 0(1) = 0(n).


