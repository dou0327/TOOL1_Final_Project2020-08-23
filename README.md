[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/dou0327/TOOL1_Final_Project2020-08-23/blob/master/project.ipynb/master)
# Dataset and motivation slide
I used the dataset from the Seaborn lib.
and i want to understand the differences between penguins in different environments.
species : penguin species (Adelie, Gentoo, Chinstrap)
island : islands where the penguin was observed (Biscoe, Dream, Torgensen)
bill_length_mm : length of bill (in mm)
bill_depth_mm : bill Depth (in mm)
flipper_length_mm : flipper length (in mm)
body_mass_g : body mass (in g)
sex : gender (male or female)
year : year of observation

#  Actual task definition/research question
I want to predict the weight of the penguin by some of its characteristics, so as to determine whether the penguin is in a healthy state.
input: the species of penguin(Adelie, Chinstrap and Gentoo),  the island where the penguin is(Torgersen,Gentoo,Chinstrap), penguin sex(male,female),
the length of penguin bill(mm), the depth of penguin bill(mm), the legth of penguin flipper(mm).
output:the body mass of penguin(g)

# literature review
Some study focused on the prediction of the body mass of penguins. This however cannot reveal the relationship between body mass and the other features. Althrough I didn't build the model to predict the body mass, but I revealed the correlation of these features and visualized the relationship.
I tried to reveal the possibile relationship between the mass of penguin and other attributes.

# Quality of cleaning

- I didn't find any duplicate rows. I selected the columns with discrete values ("object" data type), and encoded these discrete string columns to int values.
- I dropped the rows containing null values, since almost all of the data in these rows is missing.
- I didn't create any new features, since there's no special data types (such as date, geographical data) in this dataset. I just created some new columns for data type conversion. The dataset contains 333 records of penguins after cleaning. The data summary is shown below:
```
       bill_length_mm  bill_depth_mm  flipper_length_mm  body_mass_g
count      333.000000     333.000000         333.000000   333.000000
mean        43.992793      17.164865         200.966967  4207.057057
std          5.468668       1.969235          14.015765   805.215802
min         32.100000      13.100000         172.000000  2700.000000
25%         39.500000      15.600000         190.000000  3550.000000
50%         44.500000      17.300000         197.000000  4050.000000
75%         48.600000      18.700000         213.000000  4775.000000
max         59.600000      21.500000         231.000000  6300.000000
```

# Visualization
![image](https://github.com/dou0327/TOOL1_Final_Project2020-08-23/blob/master/images/1.png)
The heatmap shows the strongest correlation between flipper_length_mm and body_mass_g, the weakest correlation between bill_depth_mm and flipper_length_mm.

![image](https://github.com/dou0327/TOOL1_Final_Project2020-08-23/blob/master/images/2.png)
The pairplot shows the correlation between any two characteristics in three species, and the difference between Gentoo and the other two species is the most obvious in flipper_length_mm and bill_depth_mm.

![image](https://github.com/dou0327/TOOL1_Final_Project2020-08-23/blob/master/images/3.png)
The pairplot shows the correlation between any two characteristics in three island, and the difference between Biscoe and the other two islands is the most obvious in flipper_length_mm and bill_depth_mm.

![image](https://github.com/dou0327/TOOL1_Final_Project2020-08-23/blob/master/images/4.png)
The boxplot shows the distribution interval of the characteristics of different species. and it is obvious that the body of Gentoo species is larger than other species

![image](https://github.com/dou0327/TOOL1_Final_Project2020-08-23/blob/master/images/5.png)
The boxplot shows the distribution interval of the characteristics of different islands. and it is obvious that the bill of the penguin in Dream island is more widely distributed.

![image](https://github.com/dou0327/TOOL1_Final_Project2020-08-23/blob/master/images/6.png)
The regplot shows a scattergram with the linear model, only shows a few of them, and we can get that the bigger their flippers are, the bigger they are.

- By looking at the dataset statistics, I determined that there're no outlier.

