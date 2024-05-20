# multiagents_traffic_management

## Formulation of the problem
We consider the simplest +-shaped intersections: two single-lane roads intersecting at right angles. Road directions at this intersection:

- N - north
- S - south
- E - east
- W - west

There is a traffic light at the intersection that gives red signals and signals in one of two directions: N-S or E-W

Cars approach the traffic light in four directions: N, S, E, W. They only move straight along it (a limitation of the first version).

A traffic light has a zone of responsibility - a radius within which it understands information about cars.

A traffic light may have neighbors in one direction or another; if the radii intersect, then the area of responsibility is divided proportionally.

Driving cars entering the area of responsibility interact with the traffic light: they report their speed, size and location.

Source data is loaded from a file (Excel)

The simplest protocol is to divide the area of responsibility between traffic lights; the traffic lights must know about the cars within their zone.

## Solution
We create traffic light and car agents. They can exchange messages with each other to make decisions.

## Input data
Specified in a MS Excel-file

## Results
The result of the program is a schedule and protocol of agent negotiations (created in the directory '_activities_')
Example of activity:

```
@startuml
"Scene"	 -> 	"Car\rAgent\rCar1": 	NEW_TIME_MESSAGE\n time_step: 10, \n
"Car1"	 -> 	"Traffic\rLight\rTL1": 	NEW_CAR_MESSAGE\n car: Car Car1, \ntime_to_point: 9.100000000000001, \nfrom: W, \nlocation: (111.11111111111111; 1010.0), \n
"Scene"	 -> 	"Car\rAgent\rCar2": 	NEW_TIME_MESSAGE\n time_step: 10, \n
"Car2"	 -> 	"Traffic\rLight\rTL1": 	NEW_CAR_MESSAGE\n car: Car Car2, \ntime_to_point: 110.0, \nfrom: N, \nlocation: (10.0; 1926.6666666666667), \n
"Scene"	 -> 	"Car\rAgent\rCar3": 	NEW_TIME_MESSAGE\n time_step: 10, \n
"Car3"	 -> 	"Traffic\rLight\rTL2": 	NEW_CAR_MESSAGE\n car: Car Car3, \ntime_to_point: 9.100000000000001, \nfrom: W, \nlocation: (111.11111111111111; 10.0), \n
"Scene"	 -> 	"Car\rAgent\rCar4": 	NEW_TIME_MESSAGE\n time_step: 10, \n
"Car4"	 -> 	"Traffic\rLight\rTL2": 	NEW_CAR_MESSAGE\n car: Car Car4, \ntime_to_point: 9.639999999999999, \nfrom: W, \nlocation: (143.88888888888889; 10.0), \n
"Scene"	 -> 	"Traffic\rLight\rTL1": 	NEW_TIME_MESSAGE\n time_step: 10, \n
"Scene"	 -> 	"Traffic\rLight\rTL2": 	NEW_TIME_MESSAGE\n time_step: 10, \n
"Scene"	 -> 	"Traffic\rLight\rTL3": 	NEW_TIME_MESSAGE\n time_step: 10, \n
@enduml
```
This code can be visualized at https://www.plantuml.com/

