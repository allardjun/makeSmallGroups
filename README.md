# makeSmallGroups.py 

Make small groups of students for courses that are taught in "live-action" / "hybrid"

## Quickstart

1. Put the list of student first names in studentList_XXXX.xlsx where XXXX is the course code.

2. Edit course in `makeSmallGroups.py` so the room coords, numThinkers are appropriate.

3. Run `python3 makeSmallGroups.py`

It is possible that you get an error that is due to a the version of drawSVG package. 
This works with `drawSvg==1.9.0`. 
To build an environment with this package, do

0. run

``` python3 -m pip -r requirements.txt ```
