import pandas as pd


def extract_topics(line):
    topics = line.split(",")
    a = " ".join(topics[0].split("_")).strip()
    b = " ".join(topics[1].split("_")).strip()
    # if a == "Motion (physics)":
    #     a = "Motion"
    # if b == "Motion (physics)":
    #     b = "Motion"
    return a, b


def save_data(matched_concepts, unmatched_concepts, output_location):
    columns = ["concept", "wiki_terms"]
    df = pd.DataFrame(columns = columns)
    for i in range(len(matched_concepts)):
        df = df.append(matched_concepts[i], ignore_index = True)
    for i in range(len(unmatched_concepts)):
        df = df.append(unmatched_concepts[i], ignore_index = True)
    df.to_csv(output_location)
    return True


def get_topics(pairs_file):
    f1 = open(pairs_file, "r")
    all_topics = []
    for line in f1:
        a, b = extract_topics(line)
        all_topics.append(a)
        all_topics.append(b)

    all_topics = list(set(all_topics))
    return all_topics


def read_wiki_file(wiki_terms):
    file = open(wiki_terms, "r")
    data = []
    for line in file:
        line = line.strip()
        terms = line.split("\t")
        term1 = terms[0]
        if len(terms) > 1: term2 = terms[1]
        else: term2 = ""
        data.append([term1, term2])
    return data



def match(term1, term2):
    term1 = term1.lower()
    term2 = term2.lower()
    if term1 == term2:
        return True
    else:
        return False



def get_wiki_terms(all_topics, wiki_terms):
    data = read_wiki_file(wiki_terms)
    matched_concepts = {}
    index1 = 0
    unmatched_concepts = {}
    index2 = 0
    for topic in all_topics:
        flag = 1
        for terms in data:
            if match(topic, terms[0]):
                matched_concepts[index1] = {
                    "concept": topic,
                    "wiki_terms": terms[1]
                }
                index1 += 1
                flag = 0
                break
        if flag == 1:
            unmatched_concepts[index2] = {
                "concept": topic,
                "wiki_terms": ""
            }
            index2 += 1
    print("matched terms: ", index1)
    print("unmatched terms: ", index2)
    return (matched_concepts, unmatched_concepts)


def main_function(pairs_file, wiki_terms, output_location):
    all_topics = get_topics(pairs_file)
    matched_concepts, unmatched_concepts = get_wiki_terms(all_topics, wiki_terms)
    save_data(matched_concepts, unmatched_concepts, output_location)
    return True



pairs_file = "../../dataset/geometry.pairs"
wiki_terms = "../../dataset/geometry.wikis_clean"
output_location = "geometry_concepts.csv"

main_function(pairs_file, wiki_terms, output_location)
