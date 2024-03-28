from SimplerLLM.tools.text_chunker import chunk_by_paragraphs
from scipy.spatial.distance import cosine
import time 
import resources
import openai

def search_semantically_similar(text):
    """
    This function takes a piece of text and calculates its plagiarism score
    against another text by comparing the semantic similarity of their chunks.
    """
    chunks = chunk_by_paragraphs(text)  # Divide the input text into chunks/paragraphs
    article_paragraphs = chunk_by_paragraphs(resources.article_two)  # Divide the second text into chunks/paragraphs for comparison
    all_comparisons = 0  # Initialize a counter for all comparison attempts
    plagiarised_chunks = 0  # Initialize a counter for chunks found to be plagiarised based on similarity threshold

    for chunk in chunks.chunks:  # Iterate over each chunk in the first text
        chunk_vector = convert_to_vector(chunk.text)  # Convert the chunk text to a vector using an embedding model
            
        for paragraph in article_paragraphs.chunks:  # Iterate over each paragraph in the second text
            if paragraph.text.strip():  # Ensure the paragraph is not just whitespace
                all_comparisons += 1  # Increment the total comparisons counter
                paragraph_vector = convert_to_vector(paragraph.text)  # Convert the paragraph text to a vector
                similarity = calculate_cosine_similarity(chunk_vector, paragraph_vector)  # Calculate the cosine similarity between vectors
                
                if is_similarity_significant(similarity):  # Check if the similarity score is above a certain threshold
                    plagiarised_chunks += 1  # If so, increment the count of plagiarised chunks
        
    plagiarism_score = ((plagiarised_chunks / all_comparisons) * 100)  # Calculate the percentage of chunks considered plagiarised
    return plagiarism_score  # Return the plagiarism score

def convert_to_vector(text):
    """
    Converts a given piece of text into a vector using OpenAI's embeddings API.
    """
    text = text.replace("\n", " ")  # Remove newlines for consistent embedding processing
    response = openai.embeddings.create(
        input=[text],
        model="text-embedding-3-small"
    )
    return response.data[0].embedding  # Return the embedding vector

def calculate_cosine_similarity(vec1, vec2):
    """
    Calculates the cosine similarity between two vectors, representing the similarity of their originating texts.
    """
    return 1 - cosine(vec1, vec2)  # The cosine function returns the cosine distance, so 1 minus this value gives similarity

def is_similarity_significant(similarity_score):
    """
    Determines if a cosine similarity score indicates significant semantic similarity, implying potential plagiarism.
    """
    threshold = 0.7  # Define a threshold for significant similarity; adjust based on empirical data
    return similarity_score >= threshold  # Return True if the similarity is above the threshold, False otherwise

#MAIN SECTION
start_time = time.time()  # Record the start time of the operation

text_to_check = resources.article_one  # Assign the text to check for plagiarism

plagiarism_score = search_semantically_similar(text_to_check)  # Calculate the plagiarism score

end_time = time.time()  # Record the end time of the operation
runtime = end_time - start_time  # Calculate the total runtime

# Output the results
print(f"Plagiarism Score: {plagiarism_score}%")  # Print the calculated plagiarism score
print(f"Runtime: {runtime} seconds")  # Print the total runtime of the script