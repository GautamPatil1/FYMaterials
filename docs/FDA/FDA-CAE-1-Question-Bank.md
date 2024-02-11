# Question Bank Solution FDA

## 1.  **Main Components of a Generic NLP System:**

- **Tokenization:** Tokenization involves breaking down text into smaller units, such as words, phrases, or symbols. It's a fundamental step in NLP as it provides the basic units for further analysis.
  - **Part-of-Speech (POS) Tagging:** This process involves assigning grammatical tags to each token in a text, indicating its part of speech (noun, verb, adjective, etc.). POS tagging is essential for many downstream tasks such as parsing and named entity recognition.
  - **Parsing:** Parsing involves analyzing the syntactic structure of a sentence to determine its grammatical components and how they relate to each other. Dependency parsing and constituency parsing are common approaches.
  - **Named Entity Recognition (NER):** NER involves identifying and classifying named entities such as names of people, organizations, locations, etc., within a text. It's crucial for information extraction tasks.
  - **Semantic Analysis:** This component aims to extract the meaning from the text. It may involve tasks like sentiment analysis, semantic role labeling, or coreference resolution.
  - **Pragmatic Analysis:** This component deals with understanding the context and intention behind the text. It includes tasks such as discourse analysis and speech act recognition.

    Each of these components contributes to processing natural language by breaking down the input text into meaningful units, understanding its grammatical structure, identifying important entities and their relationships, and ultimately extracting the intended meaning.

2. **Levels of NLP and Associated Tasks:**

    - **Syntactic Level:** Tasks at this level focus on the grammatical structure of language, such as POS tagging, parsing, and syntactic dependency parsing.
    - **Semantic Level:** Tasks here involve understanding the meaning of language, including semantic role labeling, word sense disambiguation, and semantic similarity.
    - **Discourse and Pragmatic Level:** This level deals with understanding context, discourse structure, and pragmatic aspects of language, including coreference resolution, sentiment analysis, and speech act recognition.
3. **NLP Pipeline:** An NLP pipeline is a series of processing steps applied to a text document to extract useful information. Typical stages in an NLP pipeline include:

    - **Text Preprocessing:** This involves tasks like tokenization, lowercasing, and removing stopwords and punctuation.
    - **Feature Extraction:** Extracting features relevant to the task at hand, such as bag-of-words representations or word embeddings.
    - **Model Application:** Applying a trained model to perform specific NLP tasks like POS tagging, NER, or sentiment analysis.
    - **Post-processing:** This involves any additional steps needed to refine the output or make it more interpretable, such as filtering or normalization.
4. **Common Challenges in NLP and Solutions:**

    - **Ambiguity:** Natural language is inherently ambiguous, leading to challenges in interpretation. Contextual information and machine learning techniques can help disambiguate.
    - **Lack of Data:** NLP models often require large amounts of annotated data for training. Techniques like data augmentation and transfer learning can help address this challenge.
    - **Domain Specificity:** Language usage varies across different domains, making it challenging to build general-purpose models. Domain adaptation techniques can help tailor models to specific domains.
5. **Comparison of Approaches in NLP:**

    - **Rule-Based Approaches:** These approaches rely on manually crafted rules to process language. They excel in tasks where linguistic rules are well-defined, such as POS tagging or simple text normalization.
    - **Statistical Approaches:** Statistical methods use probabilistic models trained on large corpora of text. They are effective in tasks like machine translation, where the relationship between input and output can be learned from data.
    - **Deep Learning Approaches:** Deep learning models, particularly neural networks, have achieved state-of-the-art performance in many NLP tasks. They excel in tasks like sentiment analysis, named entity recognition, and machine translation, often by learning hierarchical representations of language.
