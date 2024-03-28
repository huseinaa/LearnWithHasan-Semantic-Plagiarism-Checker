from SimplerLLM.tools.text_chunker import chunk_by_paragraphs
from SimplerLLM.language.llm import LLM, LLMProvider
import time 
import resources
import json

def compare_chunks(text_chunk):
    """
    Compares a text chunk with an article text and generates a response using a OpenAI's Model
    """
    article_text = resources.article_two  # The text to compare against

    prompt = resources.prompt3  # A template string for creating the comparison prompt
    final_prompt = prompt.format(piece=text_chunk, article=article_text)  # Formatting the prompt with the chunk and article texts

    llm_instance = LLM.create(provider=LLMProvider.OPENAI)  # Creating an instance of the language model
    response = llm_instance.generate_text(final_prompt)  # Generating text/response from the LLM

    response_data = json.loads(response)  # Parsing the response into a JSON object

    return response_data  # Returning the parsed response data

def calculate_plagiarism_score(text):
    """
    Calculates the plagiarism score of a text by comparing its chunks against an article text
    and evaluating the responses from OpenAI's Model
    """
    text_chunks = chunk_by_paragraphs(text)  # Split the input text into chunks using SimplerLLM built-in method
    total_chunks = text_chunks.num_chunks  # The total number of chunks in the input text

    similarities_json = {}  # Dictionary to store similarities found
    chunk_index = 1  # Index counter for naming the chunks in the JSON
    plagiarised_chunks_count = 0  # Counter for the number of chunks considered plagiarised
    total_scores = 0  # Sum of scores from the LLM responses

    for chunk in text_chunks.chunks:
        response_data = compare_chunks(chunk.text)  # Compare each chunk using the LLM
        total_scores += response_data["score"]  # Add the score from this chunk to the total scores

        if response_data["score"] > 6:  # A score above 6 indicates plagiarism
            plagiarised_chunks_count += 1
            similarities_json[f"chunk {chunk_index}"] = response_data["article"]  # Record the article text identified as similar
            json.dumps(similarities_json)  # Convert the JSON dictionary to a string for easier storage
            chunk_index += 1  # Increment the chunk index

    plagiarism_result_json = {}  # Dictionary to store the final plagiarism results
    plagiarism_score = (plagiarised_chunks_count / total_chunks) * 100 if total_chunks > 0 else 0  # Calculate the plagiarism score as a percentage

    plagiarism_result_json["Score"] = plagiarism_score
    plagiarism_result_json["Similarities"] = similarities_json # Adding where we found similaritites
    plagiarism_result_json["IsPlagiarised"] = (total_scores > total_chunks * 6)  # Recording if the response is really plagiarised

    json.dumps(plagiarism_result_json)  # Convert the final results dictionary to a JSON string

    return plagiarism_result_json  # Return the plagiarism results as a dictionary

#MAIN SECTION
start_time = time.time()  # Record the start time of the operation

text_to_check = resources.article_one  # Assign the text to check for plagiarism

plagiarism_score = calculate_plagiarism_score(text_to_check)
formatted_plagiarism_score = json.dumps(plagiarism_score, indent=2) # Format the output for better readability

end_time = time.time()  # Record the end time of the operation
runtime = end_time - start_time  # Calculate the total runtime

# Output the results
print(f"Plagiarism Score: {formatted_plagiarism_score}")  # Print the calculated plagiarism score
print(f"Runtime: {runtime} seconds")  # Print the total runtime of the script