article_one = """
What is generative AI?

Generative AI refers to deep-learning models that can generate high-quality text, images, and other content based on the data they were trained on.

Artificial intelligence has gone through many cycles of hype, but even to skeptics, the release of ChatGPT seems to mark a turning point. OpenAI's chatbot, powered by its latest large language model, can write poems, tell jokes, and churn out essays that look like a human created them. 
Prompt ChatGPT with a few words, and out comes love poems in the form of Yelp reviews, or song lyrics in the style of Nick Cave.
"""

article_two = """
What is generative AI?

Generative artificial intelligence (AI) describes algorithms (such as ChatGPT) that can be used to create new content, including audio, code, images, text, simulations, and videos. 
Recent breakthroughs in the field have the potential to drastically change the way we approach content creation.

Generative AI systems fall under the broad category of machine learning, and here's how one such system—ChatGPT—describes what it can do:

Ready to take your creativity to the next level? Look no further than generative AI! 
This nifty form of machine learning allows computers to generate all sorts of new and exciting content, from music and art to entire virtual worlds. And it's not just for fun—generative AI has plenty of practical uses too, like creating new product designs and optimizing business processes. So why wait? Unleash the power of generative AI and see what amazing creations you can come up with!

Did anything in that paragraph seem off to you? Maybe not. The grammar is perfect, the tone works, and the narrative flows.
"""

prompt3 = """
#TASK
You are an expert in plagiarism checking. Your task is to analyze two pieces of text, an input chunk,
and an article. Then you're gonna check if there are pieces of the article that are similar in meaning to 
the input chunk. After that you're gonna pick the piece of article which is most similar and generate for it
a score out of 10 for how similar it is to the input chunk. Then you're gonna need to generate the output
as a JSON format that contains the input chunk, the article chunk which is the most similar, and the score
out of 10. 

### SCORING CRITERIA 
When checking for pieces in the article that are close in meaning to the chunk of text make sure you 
go over the article at least 2 times to make sure you picked the the right chunk in the article which is the most 
similair to the input chunk. Then when picking a score it should be based of how similar are the meanings 
and structure of both these sentences.

# INPUTS
input chunk: [{piece}]
article: [{article}]

# OUTPUT
The output should be only a valid JSON format nothing else, here's an example structure:
{{
    "chunk": "[input chunk]",
    "article": "[chunk from article which is similar]",
    "score": [score]
}}
"""


prompt4 = """
### TASK
You are an expert in plagiarism checking. Your task is to analyze two pieces of text, an input text,
and an article. Then you're gonna check if there are pieces of the article that are similar in meaning to 
the pieces of the input text. After that you're gonna pick chunk pairs that are most similar to each other
in meaning and structure, a chunk from the input text and a chunk from the article. You will then generate 
a score out of 10 for each pair for how similar they are.
Then you're gonna need to generate the output as a JSON format for each pair that contains 
the input text chunk, the article chunk which are the most similar, and the score out of 10. 

### SCORING CRITERIA 
When checking for peices in the article that are close in meaning to the chunk of text make sure you 
go over the article at least 2 times to make sure you picked the right pairs of chunks which are most similar.
Then when picking a score it should be based of how similar are the meanings and structure of both these sentences.

### INPUTS
input text: [{piece}]
article: [{article}]

### OUTPUT
The output should be only a valid JSON format nothing else, here's an example structure:
{{
    "pair 1": 
    [
    "chunk 1": "[chunk from input text]",
    "article 1": "[chunk from article which is similar]",
    "score": [score]
    ],
    "pair 2": 
    [
    "chunk 2": "[chunk from input text]",
    "article 2": "[chunk from article which is similar]",
    "score": [score]
    ],
    "pair 3": 
    [
    "chunk 3": "[chunk from input text]",
    "article 3": "[chunk from article which is similar]",
    "score": [score]
    ],
    "pair 4": 
    [
    "chunk 4": "[chunk from input text]",
    "article 4": "[chunk from article which is similar]",
    "score": [score]
    ]
}}
"""