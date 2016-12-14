### Summary
Through this visualization I have facilitated the comparison of Titanic disaster survival rate amond different sections,this visualization aims to emphasis the difference survival chance across categories, so that the viewers can compare it easily. Moreover, interactive chart allows the viewers to explore the category of interest on their own.

### Design
* I decided to use Bar Chart to compare survival of titanic passengers drawn bar chart is the best visual to know survival rate in titanic ship disaster measurement values for different categories.
* from the total number of passenger I made visualization on different gender who travelled in different class.

###Chart Selections:

Bar chart is easy to understand and good for comparison. So a bar chart is used to show the differences across the passenger class.
Stacked bar chart uses color to encode the category of data. I use it to present whether one was survived or perished.
Stacked 100% bar chart are used to show the comparison of the chance of survival.
Interaction is used to one more dimension, the category of data aggregated by gender and class.

Visual Encoding:

x position: passenger class.
y position: the survival or the percentage of passenger.
color hue: survived or perished.

additional: interactive chart is used to show data aggregated by gender and class

### Feedback

Shared index.html I got below feed back 

1. What do you notice in the visualization? 

When I first looked at the visualization, I noticed that the blue part of the female columns were higher than for the males 
As I didn't know what each color stood for, I explored. 
Through exploring, using the tooltips, I found that the female survival rate for each class was higher than for men. But the strength of this relationship diminished as the Passenger Class fell from 1st to 3rd. 

2)Looks great!! Nice work!

3)You should also add some commentary and center the visualization and title
2. What questions do you have about the data? 

None, all of the information is available in the chart - however, you have to search for it. 

3. What relationships do you notice? 

As above 

4. What do you think is the main takeaway from this visualization? 
 
As stated in my first point. 

5. Is there something you don’t understand in the graphic? 

The main confusion when I first looked that chart was the legend. What does 0, 1 represent (see below for how to change the legend labels)? I had to explore to find out. 
Why you decided to remove the tooltip for those who perished (using `if (didSurvive(e))`)? 
Why the order of the Passenger Classes is not sequential. 

I incorporated all of theses suggestions by making necessary changes in my last final_index.html



### Resources
* https://github.com/mbostock/d3/wiki/Selections
* https://github.com/PMSI-AlignAlytics/dimple/wiki/dimple.chart