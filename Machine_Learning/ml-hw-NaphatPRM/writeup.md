# Assignment 4 - Machine Learning!

  

## Part 3 - Written Questions

  

1.  **Question**: Explain your K-Means algorithm. What are the parts of your algorithm, and how do they work together to divide your samples into different clusters?

	**Answer**:
	
	For the K-Means algorithm I implements, it starts by randomly chooses the centroid point (or the mean point of the data). Then, based on these centroids, we run through all points in the data and then compare to each of the centroid and find which centroid is the nearest for this data. Then we  can categorize it into that "group". We keep working like this until all data are considered. Then, we adjust the cnetroid to make the optimum clustering (such that the grouping makes the most sense/have the lease difference between in-group data.
	
	This K-Means composes of 3 main part : initiate centroids part, finding the closest centroid part, and re-initialize the centroid part. The program will work together as the initialization of the first centroid will be random. Then, the finding the centroid part will categorize all data points based on the nearest centroid using the euclidean distance formula. Finally, the centroid list will be re-initialized using the mean of the data 

------------------------------  

2.

- **Question**: What is each data point that is being divided into clusters? what does each cluster represent?

	 **Answer**: *Your answer here*

    - Each data point in the cluster could be the three channel of color (RGB) of each point of the picture.
    - Each cluster may represent the tone of the color (such as orange tone, white tone)
  

- **Question**: How does changing the number of clusters impact the result of the song dataset and the image compression dataset?

	**Answer**: 
	
	- With the higher number of cluster in the songs, the songs will be categorized in the more delicate fashion (from genres -> sub-genres for example)
	- With the higher number of cluster in the songs, the image data will be categorized into the narrower color tone (such as from grouping the pale orange and orange together to differentiate them from each other)

------------------------------

3.

- **Question**: What is the difference between supervised classification, supervised regression, and unsupervised learning?

	**Answer**: 
	- Supervised Classification : The learning process with label that finds a function which helps in dividing the dataset into classes based on different parameters.
	- Supervised Regression : a process of finding the correlations between dependent and independent variables.
	- Unsupervised Learning : The learning process "without" label that finds a function which helps in dividing the dataset into classes based on different parameters.

- **Question**: Give an example of an algorithm under each, specifying the type of data that the algorithm takes in and the goal of the algorithm, and an explanation for why they are a supervised classification/supervised regression/unsupervised algorithm.

	**Answer**: 
	- Supervised Classification : Logistic Regression, Random Forest Classification, Naive Bayes Classification
	- Supervised Regression : Multiple Linear Regression, Support Vector Regression, Polynomial Regression
	- Unsupervised Learning : K-Means Clustering, Hierarical Clustering

------------------------------

4. **Question**: Give an overview of how you would modify your Kmeans class to implement Fair K-Means in  `kmeans.py`. Describe any methods you would add and where you would call them. You don’t need to understand the mathematical details of the Fair K-Means algorithm to have a general idea of the key changes necessary to modify your solution.

	**Answer**: 
	
	Apart from the existing implementation of regular K-Means, I would consider adding the filter part that considers the attributes used in the clustering, and then making the weight of similarities based on how sensitive that attribute is. For example, I may weight less on the race/ nationality if I want to promote the diversity (or at least decreases the problem in discrimination). 

    Another design I would add could be considering the correlation between the sensitive data (gender, race) and other attributes to nullify the hidden factor of these sensitive data in the data analysis/ML.


------------------------------

5. **Question**:  How does the Fair K-means algorithm define fairness? Describe a situation or context where this definition of fairness might not be appropriate, or match your own perception of fairness.

	**Answer**: In this case, they define ‘fairness’ as “the action related to the protection of people who share sensitive attributes, such as age, gender, ethnicity, relationship status and so on”, or “group fairness”. Although I agree that fairness should include the consideration of other attributes to make a reasonable, diversified group after clustering, this idea could make an “individual unfairness” too. For example, if two people have the same characteristics and effort on the work, they should be grouped together. However, with the inclusion of the sensitive attributes, some of them could be downgraded in terms of the impressiveness of their work.

    Another situation that could be considered is the case when these sensitive attributes are unrelated, but the unfairness still occurs, which is normally related to the financial disparity. For example, we consider clustering that separates the candidates between “accept” and “reject”. Some people could be overestimated if they have the profile of working with a huge industry (which sometimes this opportunity comes from the ancestor’s connection, etc.)

------------------------------

6. **Question**: Are there any situations in which even a perfectly fair ML system might still cause or even exacerbate harm? Are there other metrics or areas of social impact you might consider? Justify your opinion.

	**Answer**: In my opinion, the “perfectly fair ML system” is too vague on its own since if we consider the definition of “fairness” as 2.), there could be a debate on the qualification of “sensitive information”. However, if we really solve the case of clarifying the definition and create the perfect ML, some cases could still be harmful. The basic example lies on the “false positive” and “false negative” notion. Even though the ML system casts a perfect fairness, it doesn’t mean that they make a perfect classification, so these small errors will cause criticism. 

------------------------------

7. **Question**:
	Based on the text, “Algorithms, if left unchecked, can create highly skewed and homogenous clusters that do not represent the demographics of the dataset. ”

	a. Identify a situation where an algorithm has caused significant social repercussions (you can talk about established companies or even any algorithms that you have encountered in your daily life).
	
	**Answer**:
	
	Some of the existing algorithms that could deteriorate the representation of homogenous clusters would be as simple as a simple k-means clustering, or as complex as the neural network/NLP. For example from https://theconversation.com/upheaval-at-google-signals-pushback-against-biased-algorithms-and-unaccountable-ai-151768 , there is a case of using the machine learning (clustering) to accept employees based on the resume only. 

    Even though this program doesn’t consider the “sensitive” information such as gender, race, there is a difference in acceptance between two groups of people (male vs female, etc.). We later know that this disparity comes from the hidden factor of gender. For example, the achievement could distinguish between male and female (sometimes as easy as “Winner of Hackathon, Men’s Category”, or as hard as “Summa cum laude of X”, which X is the all-girls school, etc.). 

    Another case could be the training to get the model itself such as NLP that could misunderstand the role of male/female and make a discrimination by itself. For example, there is the idea of word2vec that changes the word into a vector, which does a job normally for no-gender words (such as “Rome” - “Italy” + “France” = “Paris”). However, when we use gender-related words, it’ll make a mistake such as [“doctor” - “male” + “female” = “nurse”].
	
	b. Based on your secondary knowledge of the situation what happened, why do you think it happened, and how would you do things differently (if you would). Justify your choices.

	**Answer**: 
	
	These situations occur because there is not enough cleaning process or sufficient rule of what the model should be beware of. Also, it’s because the perspective of model/AI could be different compared to humans, so the idea of getting rid of the skewed data will be somehow different. For example, the word “Winner of Hackathon, Men’s Category” may be biased for getting into work by itself (human label data). Therefore, when computers detect this information, they will think this is the label for the qualified people, leading to grouping it with the other accepted people.
	
------------------------------


8. **Question**:
	Read the article and answer the following questions:

	a. How did Google respond to this? 
	
    **Answer**: 
    
    - Google will now be taking down any Autocomplete predictions that either endorse or oppose a certain political party. These measures will only apply to Autocomplete, however, as anyone can still search for information surrounding the candidates or parties they choose.
    - Some of the search that could lead to the discrimination is not appeared in the search engine already (if you search “Why black woman is so” in the search engine now, no suggestion will appear). 

	b. Experiment with the autocomplete feature of Google now. What do you notice now? How do you feel about the way Google handled this solution? List one area in which Google can still improve.

	**Answer**: 
	
	The autocomplete doesn’t appear when we search for the sensitive information (I try “White people”,”White women”, “Black Women”, etc.) which is beneficial in terms of preventing the discrepancy such that there is no opinion from Google whatsoever. However, this idea seems to show ignorance rather than solving the concerns of the minorities. One idea that Google could do is really have the autocorrect that displays only the good sides on any sensitive information.