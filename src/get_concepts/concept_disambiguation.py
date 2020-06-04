import pandas as pd

def clean_terms(terms):
    new_list = []
    for term in terms:
        term = term.split("(")[0]
        term = term.lower().strip()
        new_list.append(term)
    new_list = list(set(new_list))
    return new_list


def extract_data(concept, wiki_term):
    if wiki_term.isna().values[0] == False:
        terms = wiki_term.values[0]
        terms = terms.split("|")
    else:
        terms = []
    terms.append(concept)
    terms = clean_terms(terms)
    terms = "|".join(terms)
    data = {
        "concept": concept,
        "key_terms": terms
    }
    return data


def read_csv_file(key_concepts):
    df = pd.read_csv(key_concepts, encoding = "utf-8")
    length = df.shape[0]
    data = {}
    for i in range(length):
        concept = df[["concept"]].iloc[i].values[0]
        wiki_term = df[["wiki_terms"]].iloc[i]
        data[i] = extract_data(concept, wiki_term)
    return data

def save_data(data, output_location):
    columns = ["concept", "key_terms"]
    df = pd.DataFrame(columns = columns)
    for i in range(len(data)):
        df = df.append(data[i], ignore_index = True)
    df.to_csv(output_location)
    return True


def main_function(key_concepts_file, output_file):
    data = read_csv_file(key_concepts_file)
    save_data(data, output_file)


key_concepts_file = "geometry_concepts.csv"
output_location = "../../output_files/geometry_concepts_ambiguity.csv"

main_function(key_concepts_file, output_location)
