# Basic UFC Fight Prediction API

Written in python using flask
Currently using a single data file - should eventually switch to using a database of some sort, but this will do for submission on monday. 

Prediction engine uses random forests for now. 

Api is pretty basic, takes in an event id for an upcoming fight, spits out the data json about the fighters in the fight from our data and the prediction. 