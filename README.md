# GloVeFastDistanceGPU
Python classs to compute and order the distances provided by cosine similarity over the GloVe model in O(n) time. Can be sped up by using binary files instead of processing the text based GloVe file.

To work, it requires the common crawl 300 dimensions glove model, though other models can be used if the CUDA kernels are modified to use other dimensions, though it is optimized to 300 dimensions. The model can be found at https://nlp.stanford.edu/projects/glove/
