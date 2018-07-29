# DeepDoctor

Med2Vec and deep learning classification project.
The team doing this is with "Call to code AI" meetup, part of Austin BigData AI.

The project is learning project, and the project goal is to read and understand
medical records and perform some basic NLP and deep learning based classification
tasks, following / replicating results of some recently published research papers on the topic.

We will be using python-based libraries, including Spacy.io (NLP), Tensorflow w/ Keras (deep learning), other libraries
(Numpy, pandas, etc.) as needed.
Medical records have additional challenges in terms of data and ontologies/terminologies,
datasets will be obtained for this project.

Reference papers to be used include:
Medical Vectors -
* Learning Low-Dimensional Representations of Medical Concepts.  Y. Choi, Y. Chiu, D. Sontag.  To appear in Proceedings of the AMIA Summit on Clinical Research Informatics (CRI), 2016. The  embeddings and open-source code to reproduce the results are available at http://clinicalml.org and on github at https://github.com/clinicalml/embeddings.

* Multi-layer Representation Learning for Medical Concepts. Edward Choi, Mohammad Taha Bahadori, Elizabeth Searles, Catherine Coffey, Michael Thompson, James Bost, Javier Tejedor-Sojo, Jimeng Sun.  Proceeding KDD '16 Proceedings of the 22nd ACM SIGKDD International Conference on Knowledge Discovery and Data Mining Pages 1495-1504.

* Exploiting Convolutional Neural Network for Risk Prediction with Medical Feature Embedding. Zhengping Che, Yu Cheng, Zhaonan Sun, Yan Liu.  NIPS 2016 Workshop on Machine Learning for Health (ML4HC).

* RETAIN: Interpretable Predictive Model in Healthcare using Reverse Time Attention Mechanism. Edward Choi, Mohammad Taha Bahadori, Andy Schuetzy, Walter F. Stewarty, Jimeng Sun. 

* Deep EHR: A Survey of Recent Advances in Deep Learning Techniques for Electronic Health Record
(EHR) Analysis. Benjamin Shickel1, Patrick J. Tighe2, Azra Bihorac3, and Parisa Rashidi. 

Some high-level/basic primers on the topic of word vectors and how CNNs use
vector representations to perform classification:
https://joshuakyh.wordpress.com/2017/11/30/introduction-to-word-embeddings/
https://joshuakyh.wordpress.com/2017/12/02/understanding-how-convolutional-neural-network-cnn-perform-text-classification-with-word-embeddings/

Milestones:
1. Collect data for project and share research papers.  8/10
2. Medical vector coding - based on "Med2Vec" and 'low dimensional representations' paper
and word2vec/GloVe word vector construction.  8/25
3. ICD-10 coding from clinical reports (CNN-based arch)  9/10
4.  Diagnostic classifier from clinical reports (LSTM-based?) Sept.

I will also create a google drive to share papers and data. documents.
To train up for this, will also share articles on word2vec and using
CNNs to classify sentences, which inspired the work on medical
