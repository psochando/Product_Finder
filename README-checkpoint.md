# PRODUCT FINDER


## Context
When receiving a new batch of products, we may have toruble storing them properly, since these articles often come mislabeled. Especially important for this task is the EAN of the article. However, provided an article from a new batch, it's not rare to find there was already another one with the same EAN but being different. And even more problematic is the case of already having such article but not being able to identify it because the EAN, and even the name, price, cost, etc., are slightly modified.

## Goal
To solve this problem, allowing a clean and efficient classification of every new article. This will bring a clear understanding about both what the company has and what the company needs.

## The algorithm
It measures the "distance" between two articles to determine if they are close enough to be the same. This algorithm compares every new article with all the stored ones and, in case there are possible matches, it will show a short list of them to the user, giving different options on how to add it to the database.

