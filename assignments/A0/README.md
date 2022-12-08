# Assignment A1.1: Feature extraction

## Scenario

You have been hired by a company as a data scientist, and you need to help build a spam classifier.  That is, create a model that can correctly classify the incoming emails to company email accounts as either spam or genuine non-spam ("ham") emails.

## Task

Before getting the data, as a warm-up to more challenging parts of the assignment coming later, you can begin by implementing functions for simplistic feature extraction that will be used by the classifier in later assignments.

## Assignment scoring

Complete each coding section according to instructions. There is a test section following each coding section. Make sure that your code passes all the tests. Passing the tests that you can see will mean you should get points for the assignment.  

## Submission deadline

The deadline for submitting this assignment is **09/09 16:00**.

## Specific steps

Implement two functions that will be used to extract feature vectors from raw text documents. 

### Extract feature vectors from documents

First, implement `get_word_frequencies()`, which takes a string `doc` as input and returns a Python dictionary (`dict`) where the tokenized words in the `doc` string are the keys, and the number of times that word occurs in `doc` is the corresponding value. You need to split words based on whitespaces and punctuation marks (specifically: `,`, `.`, `:`, `;`, `?`, `!`).

### Create feature vectors

Second, implement `get_word_feature_vector()`, which takes `word_frequencies` and `vocabulary` as input. `vocabulary` is a list of tokens in a specific order, representing the vocabulary over the entire corpus. Return a list with the same length as `vocabulary`, with the frequencies of each word in the specified order, and 0 in all other elements. 

Out-of-vocabulary terms should be ignored.