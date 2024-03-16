# Movie-recommendation-and-sentiment-analysis-using-Machine-Learning

## Overview

This project aims to provide movie recommendations and sentiment analysis based on user reviews using machine learning techniques. By analyzing the sentiment of reviews, the system can recommend movies that are likely to be enjoyed by the user. This README file provides an overview of the project, including its objectives, functionality, installation instructions, and usage guidelines.

## Objectives

- To develop a movie recommendation system based on user preferences and sentiments.
- To perform sentiment analysis on movie reviews to understand user opinions.
- To provide personalized movie recommendations to users based on their historical preferences and sentiments.

## Functionality

The project consists of the following components:

- Data Collection: Gathering movie data including titles, genres, and user reviews.
- Preprocessing: Cleaning and preparing the data for analysis by removing noise and irrelevant information.
- Sentiment Analysis: Analyzing the sentiment of user reviews to determine whether they are positive, negative, or neutral.
- Recommendation System: Building a recommendation system that suggests movies based on user preferences and sentiments.
- User Interface: Developing a user-friendly interface for users to input preferences, view recommendations, and explore movie details.

## Installation
To run the project locally, follow these steps:

- Clone the repository : git clone https://github.com/your_username/repo_name.git
- Install dependencies: pip install -r requirements.txt
- Download necessary datasets or use APIs to collect movie data.
- Preprocess the data and train machine learning models as per the project requirements.
- Run the application and test the functionality.

## Usage
- Data Collection: Use APIs or web scraping techniques to collect movie data including titles, genres, and user reviews.
- Preprocessing: Clean the data by removing duplicates, handling missing values, and performing text preprocessing (e.g., tokenization, stemming, and stop word removal).
- Sentiment Analysis: Train a sentiment analysis model using machine learning or deep learning techniques. Classify reviews into positive, negative, or neutral sentiments.
- Recommendation System: Implement collaborative filtering, content-based filtering, or hybrid recommendation algorithms to suggest movies to users based on their preferences and sentiments.
- User Interface: Develop a user interface where users can input their preferences, view recommended movies, and explore additional movie details.

## Architecture
![Screenshot 2024-03-16 165112](https://github.com/cyrus0001/Movie-recommendation-and-sentiment-analysis-using-Machine-Learning/assets/142567773/84c786f2-7795-44e4-be35-f2a0c51926bc)
![Achitecture](https://github.com/cyrus0001/Movie-recommendation-and-sentiment-analysis-using-Machine-Learning/assets/142567773/21d01f00-28e4-4b81-9fc8-6bb738399716)

# Similarity Measures

How does it decide which item is most similar to the item user likes? Here come the similarity scores.

It is a numerical value ranges between 0 to 1 which helps to determine how much two items are similar to each other on a scale of zero to one. This similarity score is obtained measuring the similarity between the text details of both of the items. So, similarity score is the measure of similarity between given text details of two items. This can be done by cosine-similarity.

# What is Cosine Similarity?

Cosine similarity is a measure used to determine the similarity between two vectors in a multi-dimensional space. It calculates the cosine of the angle between the vectors, which represents their orientation in the space. Mathematically, cosine similarity is defined as:

![Screenshot 2024-03-17 025950](https://github.com/cyrus0001/Movie-recommendation-and-sentiment-analysis-using-Machine-Learning/assets/142567773/249380d0-83eb-469b-a17d-eff92c4963a2)

​here a and b are represent the vectors being compared,and n is the dimensionality of the vectors.

![cosine similarity](https://github.com/cyrus0001/Movie-recommendation-and-sentiment-analysis-using-Machine-Learning/assets/142567773/901cdde8-6ef4-4b09-8248-54beae1ed9d0)


