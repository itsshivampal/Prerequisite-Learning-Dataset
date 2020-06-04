# Wikipedia Data Extraction for concepts

This code mainly contains 2 functions, one for getting wiki_data_extraction and another for correcting_extracted_data

## Function 1

concepts_file = "../../output_files/physics_concepts_ambiguity.csv"
output_file = "physics_wikipedia_data.csv"

extract_wiki_data(concepts_file, output_file)

This function save the output in the current directory

## Function 2

original_file = output_file
updated_file = "../../output_files/physics_correct_wikipedia_data.csv"

correct_extracted_dataset(original_file, updated_file)

This function saves the final output in output_files directory
