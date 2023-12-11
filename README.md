Abstract Animal Faces AI Art Final Documentation

James Owen – T00704318

# Introduction
The contents of this document describe the final findings of the Abstract Animal faces AI Art project for James Owen. This document discusses seven main topics and finally concludes and summarizes the project. The first section is the problem description which goes over the style for the art and the generative method being used. Second, this document goes over the method which will discuss the generative process and previous works using similar methods. The third section is the materials used for this project which discusses the physical, and digital tools used for this project. Fourth section is the evaluation where this document goes over the output and how this project went about finding the best possible solution. Fifth, this document discuses the limitations of the project and how they were overcome. The sixth section goes over the gallery of art that was produced in this project. The seventh section titled next steps describes the possible next parts for the project as well as how it can be improved. Finally, this document will conclude and summarize discussing the final findings of the Abstract Animal Faces AI Art project for James Owen.

# Problem Description
This project was aimed at creating Abstract Animal Face art using AI. The animal faces that are being referenced was to be of those typically found in British Columbia (BC) Canada. These animals where to be based off real photographs taken in BC. The animals chosen were a bear, Canadian goose, and a moose. To achieve these three pieces of art a genetic algorithm was used. 

To create abstract art using a genetic algorithm from real life photos there needed to be a process that the genetic algorithm would break down. Artists Network defines abstract art as distancing of an “idea from object references” [1]. For this project the object is the animal faces, and the distancing is the dots or genes. The dots would correspond to vectors on a canvas that would be initialized randomly. The canvas’ are evaluated by how close they match the original image. Over generations of mutating and crossing over the best solution it creates abstract dot art of the animal face from the image. 

To find the best solution for the image the idea is to iterate the genetic algorithm until a piece of art is created that looks like the animal it was based off. To many iterations and this could create the exact image back, so it is also advantageous to limit the search a bit. Since genetic algorithms work very well with the problem of iterating overtime to create the best solution it makes it a favourable method to create abstract art. Given this genetic algorithm is an excellent method to use for this project and continuing why it is so the next section discusses this method.

# Method
The method used for creating AI art from faces of animals located in British Columbia (BC) is using a genetic algorithm. This section discusses genetic algorithms by first describing what a genetic algorithm is, second how it is used for this project, and third reference other works that use a genetic algorithm. Finally, this section will conclude and summarize the use of a genetic algorithm in this project for creating abstract art of animal faces.

A genetic algorithm initializes a population through randomly generating data sets called chromosomes. These chromosomes are then assessed for there fitness or how close they are to the target. The parts of the population that have chromosomes that represent the target the best is selected for breeding the rest are discarded. The population that is selected for breeding then crossed over by combining multiple of the fit population to create a new chromosome. The populated is then mutated by altering an aspect of the chromosome. This is then repeated from the fitness evaluation until the algorithm has created a desired outcome. This is the genetic algorithm and is method used for this project of generating abstract art from animal faces.

To create abstract art of faces of animals located in British Columbia (BC) Canada using a genetic algorithm this project references real animal photos for the target. The algorithm starts by generating a population of canvas’. These canvas’ has chromosomes in the form of dots. These dots will be randomly assigned a radius in pixels, colour, and position on the canvas. The canvas’ are then assessed for how well they match the target image through the fitness function. The best half of canvas’ is selected for breeding and worst are discarded. The best is then bred through the crossed over function by taking two chromosomes and adding half the genes from one and half from the other. The population is then mutated. To mutate the algorithm either adds a dot or deletes one to slightly change the canvas. The algorithm will then repeat from the fitness function until the art represents the target image. This method is also used in other works.

Using a genetic algorithm to create abstract art has had many implementations. One of these is by Chris Cummins that generates abstract art based off photos [2]. Chris has set up a website that contains a list of different images that a user can generate abstract art from in real time. This is a great for this project since Chris’ project is very similar to this one. This gives a great base for the project which since it shows each generation and how the project should look after few and many generations.

This section has shown the proposed method of generating abstract art from faces of animals located in BC using a genetic algorithm. To show how this method worked for this project this section first explained how a genetic algorithm works, then how this project implemented it, and finally discussed other works that use a genetic algorithm. Also explained was why this method is a good use case for the project and how it is being used to generate abstract art. The next section will go over the materials used for this project.

# Materials
The materials used for creating AI abstract art from the faces of animals are digital assets in the form of photos to train the art and physical in the form of coding skills from the development team. For the photos of animal faces this project uses three different photos taken in British Columbia (BC) Canada. These are a photo of BC animal faces are of a bear [3], Canadian goose [4], and of a moose [5]. The bear, goose, and moose images will be used as the target image for the generations though with some alterations to the photo for the digital assets. The physical assets will be coding skills from the development team. This is through the team’s skill with using the python programming language and creating a genetic algorithm.  These skills have been obtained through discussions with other classmates and course material as well as trial and error. By using images in the form of digital materials and coding skills for physical materials this project has been completed to show AI abstract art from faces of animals. The next section will go over the evaluation for this project.

# Evaluation
To evaluate the abstract art of animal faces the use of a fitness function is be used. As mentioned in the proposed method section canvas’ have dots throughout to try to best match the target photo. To achieve this the program uses a fitness function. The fitness function assesses the difference of each pixel by each color between the target and the canvas. The closer the score is to zero the better the closer it is to the target. To do this the steps are shown below:

1. Send each chromosome to the fitness function for evaluation.
1. Get the bitmap red, green, blue values (0-255 for each) from both the target and the canvas.
1. Find the absolute value of the difference between the target and the canvas’ colors for each point in the arrays.
1. Divide by 255 and multiply by 100 to get the percentage.
1. Add all the averages up and divide by the size of the array to get the average.
1. Continue to mutate and cross over functions.
1. Repeat from step 1 until the canvas represents the target in the form of abstract dot art.

To calculate the percentage as mentioned in step 4 previously the following formula labelled Equation 1 is used:

P=xy×100

P = percentage result from 0-100

x = |canvas - target|

y = 255

<a name="_ref152798310"></a><a name="_toc153132879"></a>*Equation 1. Percentage Formula*

Once the percentage of each pixel is calculated the percentages are added together and divided by the total pixels as mentioned in step 5 previously. The formula to calculate the average is shown in Equation 2 below:

A=1ni=1nai

A = mean (average)

n = number of pixels

ai = value of P from Equation 1

<a name="_ref152798470"></a><a name="_toc153132880"></a>*Equation 2. Average Calculation Formula.*

The result from “A” in Equation 2 is used as the fitness score. Using both formulas from Equation 1 and Equation 2 create the score to find the fitness for each chromosome in the population. The chromosomes with the higher number scores are then discarded and the ones with the lowest scores are kept for breeding. This is used to find the best possible results for the project using the fitness level of each chromosome. To continue the discussion of generating AI abstract art of animal faces the next section discusses the limitations that where had throughout the project.

# Limitations
This project of creating abstract AI art of animal faces has some limitations. One of the limitations was the generation time for each photo. It took many hours just to generate one image and sometimes was required to run the algorithm over night. To overcome this to get all the photos done before the deadline the algorithm was ran simultaneously for each photo on different cores of the CPU. Another limitation was the algorithm crashed while in the process for generating the photos. This set the project back since the generation had to be restarted from the beginning. To rectify this the project was restarted but this time with a more powerful computer. These to limitations though difficult where able to be over come through perseverance of this project. To continue about the process, for creating abstract art of animal faces the next section goes over the gallery of art generated.

# Gallery
The creations for this project used three different photos. The photos are a photo of a bear [3], goose [4], and moose [5]. These are photos taken in British Columbia Canada depicted in figures 1, 2, and 3 below:


<a name="_toc153132885"></a>*Figure 1. Bear Photo [3]**



<a name="_toc153132886"></a>*Figure 2. Goose Photo [4]**

<a name="_toc153132887"></a>*Figure 3. Moose photo [5]**

The starting background is set to a default of all white so to get the best possible output the backgrounds for the target photos should also be white. To do this the photos have been edited for use as target photos as seen below in figures 4, 5, and 6:


<a name="_toc153132888"></a>*Figure 4. Bear Photo Edited*

<a name="_toc153132889"></a>*Figure 5. Goose Photo Edited*


<a name="_toc153132890"></a>*Figure 6. Mose Photo Edited*

Using the photos as the target as mentioned in Figure 4, 5, and 6 the following output was created in figure 7, 8, and 9 after 60000 generations of each:


<a name="_toc153132891"></a>*Figure 7: Bear Abstract Art Result*

<a name="_toc153132892"></a>*Figure 8: Goose Abstract Art Result*

<a name="_toc153132893"></a>*Figure 9: Moose Abstract Art Result*

As seen above is the final output for the abstract art of animal faces. To continue what the next steps for this project could be the next section continues the discussion.

# Next Steps
The project of generating AI abstract art of animal faces is finished however this section discusses possible improvements. Though the algorithm that was created can generate art fine there are a few things that would make the project even better. A few of these are creating a way to save progress, testing a better way to find the solution, and use triangles instead of dots. These three things would result in a better project overall.

The three improvements given extra time are save progress of generation, testing a better solution, and use of triangles instead of dots. For saving progress this would use a file format to save the data during different generations such as json. This would negate issues mentioned earlier in limitations about how the computer crashed. With saving to a outside file if the computer crashes than the saved file would still contain the data so the progress could start from where it left off rather than restart from the beginning. For testing a better way to find the solution the project would use different mutation methods and output every few generations the average fitness to see which mutation method works the best to find the result faster. Finally, using triangles instead of dots would make for more variance in the art in terms of styles. This would make the final product more interesting by having more to show once completion. To conclude this project on generating AI abstract art of animal faces the next section will conclude and summarize this document.

# Conclusion
This document has shown the process of generating AI abstract art of animal faces done for the corresponding project to this document. The project has been shown through describing its, problem description, method, materials, evaluation, limitations, gallery, and next steps. Described these sections was the execution for this project and how it came to fruition and what improvements can be made for the future. By completing the steps described in each section this project was able to create AI abstract art.
# References


|[1] |D. Nimmer, "Artist Network," 2020. [Online]. Available: https://www.artistsnetwork.com/art-inspiration/what-is-abstract-art/.|
| :- | :- |
|[2] |C. Cummins, "Genetic Algorithms & Generative Art," Chris Cummins, 2020. [Online]. Available: https://chriscummins.cc/s/genetics/#. [Accessed 2023].|
|[3] |J. Lloyd and Tatum Lenberg, "Discovery," 14 September 2021. [Online]. Available: https://www.discovery.com/science/facial-recognition-for-grizzly-bears. [Accessed 6 December 2023].|
|[4] |V. News, "CTV News," 26 January 2021. [Online]. Available: https://bc.ctvnews.ca/council-approves-canada-goose-cull-in-b-c-city-1.5282813. [Accessed 6 December 2023].|
|[5] |C. Correia, "CBC News," 15 October 2017. [Online]. Available: https://www.cbc.ca/news/canada/british-columbia/hunters-upset-moose-hunt-closure-cariboo-1.4352036. [Accessed 6 December 2023].|


# Tables and Figures
[Equation 1. Percentage Formula	4](#_toc153132879)

[Equation 2. Average Calculation Formula.	4](#_toc153132880)



[Figure 1. Bear Photo \[3\]	5](#_toc153132885)

[Figure 2. Goose Photo \[4\]	5](#_toc153132886)

[Figure 3. Moose photo \[5\]	5](#_toc153132887)

[Figure 4. Bear Photo Edited	5](#_toc153132888)

[Figure 5. Goose Photo Edited	5](#_toc153132889)

[Figure 6. Mose Photo Edited	5](#_toc153132890)

[Figure 7: Bear Abstract Art Result	6](#_toc153132891)

[Figure 8: Goose Abstract Art Result	6](#_toc153132892)

[Figure 9: Moose Abstract Art Result	6](#_toc153132893)


