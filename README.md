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

We are using as first target, doing word embeddings for Biomedical NLP. The paper we are referencing is:
"How to Train Good Word Embeddings for Biomedical NLP" by Chiu, Crichton, Korhonen and  Pyysalo.
http://aclweb.org/anthology/W/W16/W16-2922.pdf
Code for this can be found in the following Github repo:
https://github.com/cambridgeltl/BioNLP-2016

The biomedical corpus we are using for this is a large corpus of PubMed / PMC (PubMed Central) papers, found here:
ftp://ftp.ncbi.nlm.nih.gov/pub/pmc/oa_bulk/
take the 'comm_use' and txt files ... comm_use.O-Z.txt.tar.gz, comm_use.I-N.txt.tar.gz, comm_use.C-H.txt.tar.gz, comm_use.0-9A-B.txt.tar.gz
if you download these and unpack, you will have  5455 directories of different Journals,
with text documents, each document is a research paper.  838,383 total documents/files taking up 35GB total.


Reference papers to be used include:
Medical Vectors -
* Learning Low-Dimensional Representations of Medical Concepts.  Y. Choi, Y. Chiu, D. Sontag.  To appear in Proceedings of the AMIA Summit on Clinical Research Informatics (CRI), 2016. The  embeddings and open-source code to reproduce the results are available at http://clinicalml.org and on github at https://github.com/clinicalml/embeddings.

* Multi-layer Representation Learning for Medical Concepts. Edward Choi, Mohammad Taha Bahadori, Elizabeth Searles, Catherine Coffey, Michael Thompson, James Bost, Javier Tejedor-Sojo, Jimeng Sun.  Proceeding KDD '16 Proceedings of the 22nd ACM SIGKDD International Conference on Knowledge Discovery and Data Mining Pages 1495-1504.

* Exploiting Convolutional Neural Network for Risk Prediction with Medical Feature Embedding. Zhengping Che, Yu Cheng, Zhaonan Sun, Yan Liu.  NIPS 2016 Workshop on Machine Learning for Health (ML4HC).

* RETAIN: Interpretable Predictive Model in Healthcare using Reverse Time Attention Mechanism. Edward Choi, Mohammad Taha Bahadori, Andy Schuetzy, Walter F. Stewarty, Jimeng Sun. 

* Deep EHR: A Survey of Recent Advances in Deep Learning Techniques for Electronic Health Record
(EHR) Analysis. Benjamin Shickel1, Patrick J. Tighe2, Azra Bihorac3, and Parisa Rashidi. 

PDFs of these papers is shared on google drive.

Some high-level/basic primers on the topic of word vectors and how CNNs use
vector representations to perform classification:
https://joshuakyh.wordpress.com/2017/11/30/introduction-to-word-embeddings/
https://joshuakyh.wordpress.com/2017/12/02/understanding-how-convolutional-neural-network-cnn-perform-text-classification-with-word-embeddings/

Milestones for completing this project:
1. Collect data for project and share research papers.  
2. Medical vector coding - based on "Med2Vec" and 'low dimensional representations' paper
and word2vec/GloVe word vector construction.
3. ICD-10 coding from clinical reports (CNN-based arch) 
4.  Diagnostic classifier from clinical reports (LSTM-based?) Sept.

