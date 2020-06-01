import pandas as pd
#
def extract_topics(line):
    topics = line.split(",")
    a = " ".join(topics[0].split("_")).strip()
    b = " ".join(topics[1].split("_")).strip()
    # if a == "Motion (geometry)":
    #     a = "Motion"
    # if b == "Motion (geometry)":
    #     b = "Motion"
    return a, b


def get_value(line):
    features = line.split()
    val = int(features[0])
    return val


def save_data(topic_a, topic_b, relation, output_location):
    columns = ["topic_a", "topic_b", "relation"]
    df = pd.DataFrame({'topic_a': topic_a, 'topic_b': topic_b, 'relation': relation})
    df.to_csv(output_location)



def get_labeled_data(pairs_file, features_file, output_location):
    f1 = open(pairs_file, "r")
    f2 = open(features_file, "r")
    topic_a = []
    topic_b = []
    relation = []

    for line in f1:
        a, b = extract_topics(line)
        topic_a.append(a)
        topic_b.append(b)

    for line in f2:
        val = get_value(line)
        relation.append(val)

    save_data(topic_a, topic_b, relation, output_location)
    return True


pairs_file = "../../dataset/geometry.pairs"
features_file = "../../dataset/geometry.features"
output_location = "../../output_files/geometry_labeled_pairs.csv"

get_labeled_data(pairs_file, features_file, output_location)
