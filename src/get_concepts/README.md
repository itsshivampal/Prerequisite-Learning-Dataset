## Code 1: get_key_concepts.py

pairs_file = "../../dataset/geometry.pairs"
wiki_terms = "../../dataset/geometry-grade.wikis_clean"
output_location = "geometry_concepts.csv"

This code read pairs file and wiki_terms, and output geometry_concepts.csv in the same directory

-------------------------------------------------------

## Next Step: Copy "geometry_concepts.csv" as "geometry_key_concepts.csv"
Edit this file manually and remove useless terms

-------------------------------------------------------

Code 2: concept_disambiguation.py

key_concepts_file = "geometry_key_concepts.csv"
output_location = "../../output_files/geometry_concepts_ambiguity.csv"

This code read key_concepts_file and save final output in output_files directory as output_location
