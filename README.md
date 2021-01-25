# Overview  
The project examines two different solutions for solving a modelling problem related to how students select and change strategies over a period of time and discusses an extension to the problem. The first solution explores modelling the changes in student dynamics by differential equations. The second approach investigates the use of agent-based modelling. 

# Problem Description  
● A population of students is working on group projects. Students can follow two strategies (S): work hard for the project (S=H) or free-ride (S=L)  

● In every course, groups of size N are formed at random. Students use the strategy determined at the beginning of the course (i.e. S=H or S=L) in their group work.  

● Total group effort is determined by the composition of the group. In a group with h hard workers and l=n-h lazy workers total group effort is e=h*H+l*L (H and L being the effort put in by hard/lazy workers).  

● When group projects are marked, every student in a group gets the same mark. The lecturer determines this mark as m=e/n (that is, by dividing total group effort by the number of students in a group; the larger this number the better the mark.)  

● At the end of the semester groups are dissolved and every student rethinks his strategies for the next semester. They do this by selecting another student (a reference student) at random and comparing a measure Pi based on marks and effort, Pi=m-a*S (where a is a parameter and S=H or S=L depending on strategy). The measure accounts for the mark obtained, but is lowered by the amount of effort spent. Very good marks without effort maximise the performance measure. If the reference student selected for comparison got a higher performance measure Pi, the selected student will imitate the reference student's strategy in the next semester with a probability that is proportional to the difference in the performance measure Pi. Students will not imitate strategies from other students with worse performance measures.  

● Students study forever and they follow the same procedure (as outlined above) for every course they take.  

# Research Questions Addressed by the Project
● Assuming we start with equal numbers of hard working and lazy workers, what is the composition ofthe group  
– After 4 years (i.e. 8 courses) if H=1 and L=0 and a=0.5.  
– In the long run (after an “infinite” number of years)?  
– How quickly is this equilibrium state reached?  

● How do the following parameters influence results:  
– Initial composition of the population  
– Group size (n)  
– Cost of effort, a  
– Contribution of hard workers to group effort (i.e. H and L)  
