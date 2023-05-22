# Microplastic-Transport
Python code established to generate different rainfall conditions based on Curve Number, Rainfall Intensity (following IDF curves), and velocity. 
Looking at a case study in Houston, TX

If you would like to use this file you may do so by changing variables to inputs you have available.

First: Change the curve number array to curve numbers that you will be using
*Data set available for Global Curve Numbers in GIS here:Jaafar, Hadi; Ahmad, Farah (2019): GCN250, global curve number datasets for hydrologic modeling and design. figshare. Dataset. https://doi.org/10.6084/m9.figshare.7756202.v1 

Then the code will compute retention max/storage and create an S array. You will now have S values to use in your iterations. 
The code will then compute intial abstraction using I=.2S for every possible condition and create an array of these values.

Rainfall intensity table was created using the City of Houston Storm Management Plan. If this is available to you for your city you may change the data in the table or delete that section and create your own equations based on the IDF curves for your location.

The code will then generate a rainfall intensity (you can change this TC=time of concentration to be more or less based on your location's comprehensive plan). The values produced are in in/hr then you can multiply by your storm event (an "arbitrary" number of hours, minutes of rainfall you want to consider as a rainfall event). 

*If you need guidance on picking this number you can download rainfall data off gauges around you and open the spread sheet to visualize what would be the most common number of hours that rainfall persists the most in your area. I have another code available on my github if you want to condense the data into your rainfall event by inputting CSV files and it is currently set to 6 hours events. (This can be changed when the code is downloaded): https://github.com/marcela-strane/RainfallPatterns

If you would like to identify a rainfall runoff, Q, in inches the code will generate all runoff possible for each condition and this is stored in a Qmatrix as well as iterated as 1 value, depending on what you would like to use it for. 

You are able to change the land slope, manning's coefficient (ours is based on Bermuda Grass) to identify the maximum sheet flow length you will need to be in the sheet flow regime. 

Then you are able to find the time of travel it takes from point A to point B across your sheet flow regime and then find the velocity.
