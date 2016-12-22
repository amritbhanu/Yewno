## Yewno
### Current method is with Doc2vec
- Rerun src.py to see results on console.
- I have considered 3 input strings ['chippewa escobar','trondheim trondheim bergen','notabl sign ninth argentina fire rock']
- A sample dataset was generated and can be seen [here](https://github.com/amritbhanu/Yewno/blob/master/dataset/file).
- if any of the words is not in the original document, then it will raise an exception
- The code is implemented in Python and libraries like gensim, nltk, numpy and scipy are needed to run the code.
- Wrote preprocessing functions which can be of used for text mining.
- The output can be read [here](output.md).

### Q1. Is your system scalable?
- The training model which is using Gensim is already scalable. We will just need multiple machines to distribute the training workload.
- My preprocessing steps could be modified to make them paralysed using spark. (Small snippet of pyspark code can be read [here](spark.py))

### Q2. How could you figure out which are the most informative features for each of the tasks above?
- The sequence in which these words occur in a document gives us the most information.

### Q3. In general, how would you assess the performances of your system?
- First point is the scalability.
- The accuracy of the results.
- And repeatability meaning, we should get similar results when we run the same code again.
- Saving and retraining the model should be possible.

### Other solutions I can think of are:
 - Hidden Markov Model Chain.
 - Bayesian Learning
 - n-gram model
