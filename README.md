# DevDay - Cow Positioning System
At Nedap, the market group Livestock Management develops solutions for livestock handling. One of these solutions is the positioning of individual cows in a herd. Radio technology is used to locate individual tags on each animal. 

The Cow Positioning System basically works as follows. Several beacons are positioned along the cowshed’s roof. These beacons send uniquely identifiable radio signals that are received by the tags worn by the animals. In turn, the tags emit various parameters to an endpoint that collects all the data. Using real Nedap hardware, you will build your own Cow Positioning System. 

## Goal
Implement a solution to determine the location of your cow tag in the room as accurately as possible.

## Steps
1. Implement in `solution.py`:
	1. Implement `get_sensor_id()` with your cow tag. This is the code on your cow tag.
	2. Implement `get_team_id()`. Be creative :)
	3. Implement the `calculate_position(b1, b2, b3, b4)`. Check the comments for information on `b1`, `b2`, `b3` and `b4`.
2. Run `client.py`.

Good luck!