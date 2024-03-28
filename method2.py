from scipy.spatial.distance import cosine
import time 
import resources
import openai

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

def search_semantically_similar(text_to_check):
    """
    Compares the semantic similarity between the input text and a predefined article text.
    It returns a list containing the similarity score and a boolean indicating whether
    the similarity is considered significant.
    """
    result = []  # Initialize an empty list to store the similarity score and significance flag

    input_vector = convert_to_vector(text_to_check)  # Convert the input text to a vector using an embedding model
        
    article_text = resources.article_two  # texts.two contains the text of the article to compare with
        
    article_vector = convert_to_vector(article_text)  # Convert the article text to a vector
        
    similarity = calculate_cosine_similarity(input_vector, article_vector)  # Calculate the cosine similarity between the two vectors
        
    result.append(similarity)  # Append the similarity score to the list
    result.append(is_similarity_significant(similarity))  # Append the result of the significance check to the list
    
    return result  # Return the list containing the similarity score and significance flag
    
def calculate_plagiarism_score(text):
    """
    Calculates the plagiarism score of a given text by comparing its semantic similarity
    with a predefined article text. The score is expressed as a percentage.
    """
    data = search_semantically_similar(text) # Obtain the similarity data for the input text
    data[0] = data[0] * 100  # Convert the first item in the data list (similarity score) to a percentage
    
    return data  # Return the plagiarism score and significance

#MAIN SECTION
start_time = time.time()  # Record the start time of the operation

text_to_check = resources.article_one  # Assign the text to check for plagiarism

plagiarism_score = calculate_plagiarism_score(text_to_check)[0]
significance = calculate_plagiarism_score(text_to_check)[1]

end_time = time.time()  # Record the end time of the operation
runtime = end_time - start_time  # Calculate the total runtime

# Output the results
print(f"Plagiarism Score: {plagiarism_score}%")  # Print the calculated plagiarism score
print(f"Is result Significant: {significance}")  # Print the signficance of the score
print(f"Runtime: {runtime} seconds")  # Print the total runtime of the script