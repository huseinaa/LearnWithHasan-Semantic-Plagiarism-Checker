from SimplerLLM.language.llm import LLM, LLMProvider
import time 
import resources
import json

def compare_chunks(text_chunk):
    """
    Compares a given text chunk with an article to determine plagiarism using a language model.
    
    Returns dict: The response from the language model, parsed as a JSON dictionary.
    """
    article_text = resources.article_two  # The text to compare against

    # Formatting the prompt to include both the input text chunk and the article text
    comparison_prompt = resources.prompt4.format(piece=text_chunk, article=article_text)

    llm_instance = LLM.create(provider=LLMProvider.OPENAI)  # Creating an instance of the language model
    response = llm_instance.generate_response(comparison_prompt)  # Generating response

    response_data = json.loads(response)  # Parsing the response string into a JSON dictionary

    return response_data  # Returning the parsed JSON data

def calculate_plagiarism_score(text_to_analyze):
    """
    Calculates the plagiarism score based on the analysis of a given text against a predefined article text.
    
    Returns dict: A JSON dictionary containing the plagiarism score and the raw data from the analysis.
    """
    plagiarism_results = {}  # Dictionary to store the final plagiarism score and analysis data
    plagiarised_chunk_count = 0  # Counter for chunks considered plagiarised

    analysis_data = compare_chunks(text_to_analyze)  # Analyze the input text for plagiarism
    total_chunks = len(analysis_data)  # Total number of chunks analyzed
    
    for key, value in analysis_data.items():
        # Check if the value is a list with at least one item and contains a 'score' key
        if isinstance(value, list) and len(value) > 0 and 'score' in value[0] and value[0]['score'] > 6:
            plagiarised_chunk_count += 1
        # Check if the value is a dictionary and contains a 'score' key
        elif isinstance(value, dict) and 'score' in value and value['score'] > 6:
            plagiarised_chunk_count += 1

    plagiarism_score = (plagiarised_chunk_count / total_chunks) * 100 if total_chunks > 0 else 0 # Calculate plagiarism score as a percentage
    plagiarism_results["Total Score"] = plagiarism_score  # Add the score to the results dictionary
    plagiarism_results["Data"] = analysis_data  # Add the raw analysis data to the results dictionary

    json.dumps(plagiarism_results)  # Convert the results dictionary to a clear JSON string

    return plagiarism_results  # Return the final results dictionary
    
#MAIN SECTION
start_time = time.time()  # Record the start time of the operation

text_to_check = resources.article_one # Assign the text to check for plagiarism

plagiarism_score = calculate_plagiarism_score(text_to_check)
formatted_plagiarism_score = json.dumps(plagiarism_score, indent=2) # Format the output for better readability

end_time = time.time()  # Record the end time of the operation
runtime = end_time - start_time  # Calculate the total runtime

# Output the results
print(f"Plagiarism Score: {formatted_plagiarism_score}")  # Print the scores
print(f"Runtime: {runtime} seconds")  # Print the total runtime of the script
