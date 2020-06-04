import pandas as pd


def extract_toc_data(line):
    data = line.split(" ")
    toc_no = data[0].strip()
    toc_page = data[-1].strip()
    title = " ".join(data[1:-1]).strip()
    toc_data = {
        "index": toc_no,
        "title": title,
        "page_no": toc_page
    }
    return toc_data

def save_toc_data(data, output_file):
    columns = ["index", "title", "page_no"]
    df = pd.DataFrame(columns = columns)
    for i in range(len(data)):
        df = df.append(data[i], ignore_index = True)
    df.to_csv(output_file)
    return True


def export_txt_file(data, output_txt_file):
    file = open(output_txt_file, "w+")
    for i in range(len(data)):
        line = "file_data: " + data[i]["index"] + "|" + data[i]["title"] + "|" + data[i]["page_no"] + "\n\n\n"
        file.write(line)
    return True



def get_toc_data(file_name, output_file, output_txt_file):
    file = open(toc_file, "r")
    all_data = {}
    index = 0
    for line in file:
        data = extract_toc_data(line)
        all_data[index] = data
        index += 1
    export_txt_file(all_data, output_txt_file)
    save_toc_data(all_data, output_file)
    return True


toc_file = "../../dataset/geometry.toc"
output_file = "geometry_toc.csv"
output_txt_file = "geometry_toc.txt"

get_toc_data(toc_file, output_file, output_txt_file)
