# ut_dataminingPosterProject
Poster project for UT course Data Mining 2017/18

Authors:

Leiger Virro
Mart Simisker
Karl-Martin Uiga


Business understanding
1.1. Identifying business goals

Background:
Crime is an everyday part of life. The single criminal events have been documented, however looking at all of the data, it is impossible for a human to make meaningful conclusions. The people in Law Enforcement wish to reduce crime rates to make living in Estonia safer. With the aid of Data Mining, it is possible to find more connections between the single events, and with these conclusions even come up with solutions to decrease the crime rate. 

Business goals:
Identify areas with the highest crime rate.
Classify crimes with their severity level and identify where and at what time the most severe crimes happen.
Identify locations where new security cameras should be implemented to discover crimes.
Information for law enforcement where to show more presence to reduce crime rate.
Make Estonia safer for its residents and visitors.
Find out the days with the biggest number of recorded crime cases.


Business success criteria:

Results will be measured with plots and a heat map of Estonia. On the map there would be areas with a hot color where crime rate is high and areas with a cold color (blueish) where crime rate is low. Another map would be a heat map but this time instead of using amount of crimes to describe an area we would use a crime classification. With the help of these maps, it will be possible to organize crime prevention to the areas, with high probability of crime. The real success criteria will be visible after a while. As time passes, crime rates in the defined area should start to drop.

For a measure, if a similar study will be carried out after two years, there should be a drop in crime rates in the defined areas if action has been taken.
The knowledge about times with higher criminal activity can be taken into account, when making the work schedules of law enforcers, the heatmaps, when planning patrol routes.


1.2. Assessing situation
1.2.1. Inventory of resources
Available resources for this project:
Dataset on criminal offence cases against property in public space (2016-2017);
Dataset on criminal offence cases against property in public space (2011-2015);
Explanation letter for the datasets;
Police and Border Guard Board website;
Penal Code of Estonia;
Course materials (lectures, practical sessions) for the Data Mining (MTAT.03.183) course;
RStudio - a free and open-source integrated development environment for R, a programming language for statistical computing and graphics;
Human resources (the team, supervisors).

1.2.2. Requirements, assumptions, and constraints
The due date for this project is Jan. 8, when the final poster session will be held.
There are no legal or security obligations since both of the datasets are open to the public and free to use. It has to be noted, that the datasets consist of data from operational level and might change after the proceedings. The datasets are updated once a week on Tuesday.
Our team has access to the datasets.

1.2.3. Risks and contingencies
Contingency plan:
Risk
Solution
Power outage in our workspace.
Find someplace else with access to power (school, library).
Network connectivity problems.
Relocate to either school, library or another place with internet access.
PBGB (Police and Border Guard Board) decides to make the datasets private and/or applies legal restrictions to the data.
We will have to contact them and enquire about the usage of their data. In worse case scenario, we will have to change the topic of this project.
One or more members of the team is unable to work for a period of time.
The other member(s) will do their work and if the situation demands, then we will contact the supervisors of this course to work out a solution.
Underestimating the effort and time that is required to finish the project.
Either make compromises within the project and reschedule or just work hard and do tasks at the first possible opportunity.

In all other scenarios, where the situation is not under our control, we will contact the course supervisors and find the solution.

1.2.4. Terminology

PBGB - Police and Border Guard Board;
Open data - data that has been made public and therefore is available for everybody to use;
Public space - a piece of land, a building, a room or public transport that has no restrictions on who can use them;
Penal code - document which compiles all, or a significant portion, of a particular jurisdiction's criminal law;
L-EST - planar rectangular coordinate system, geographical coordinates X and Y are represented as an interval, where the difference of start and end is in meters;
Data classification - process of organizing data into relevant categories for its most efficient use;
Sequential patterns - method for identifying trends or regular occurrences of similar events.

1.2.5. Costs and benefits
Costs
Disk storage - data sets, working data, images, plots, resulting files
Man hours spent on the project
Electricity spent during the project 
Psychological trauma caused by discovering crime
Benefits
Saved monetary value from prevented crimes
Secure community
Better management of resources needed to organize public supervision

1.3. Defining data-mining goals

Data-mining goals:
Group the data according to geographical location.
Classify the data according to the crime severity.
Visualise the data to identify the highest crime rate areas.
Find out abnormalities (e.g there are many crimes happening on the first day of the year)

Data-mining success criteria:
A heatmap describing areas with higher crime rates (the quality of the criteria will be assessed by the collective of our team)
Subsets of data according to the classes of crime severity (decided during work, assessed by the team)
Heatmaps for defined crime types (crime types will be decided during the work - the quality of the criteria will be assessed by the collective of our team)
Other visualisations (decided on during work, assessed by the collective of our team)
Comparisons of different crimes according to some attribute such as lost resources or crime severity
Plot of crime occurrences by daytime 
Report of results containing the conclusion and abnormalities (assessed by our team)
