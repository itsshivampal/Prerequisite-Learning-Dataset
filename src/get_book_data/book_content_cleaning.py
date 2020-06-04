import pandas as pd


def book_section(line):
    if "file_data" in line and line[:9] == "file_data":
        return True
    else:
        return False


def handle_special_char(word):
    new_word = ""
    punctuations = "\"&()+-*.:?{|}"
    for ch in word:
        if ch in punctuations or ord(ch) >= 97 and ord(ch) <= 122 or ord(ch) >= 65 and ord(ch) <= 90 or ord(ch) >= 48 and ord(ch) <= 57:
            new_word += ch
    if len(new_word) > 1:
        return new_word
    else:
        return ""



def clean_text(content_text):
    content = " ".join(content_text.split("\n"))
    words = content.split(" ")
    final_content = ""
    for word in words:
        word = handle_special_char(word)
        if word != "":
            final_content += word + " "
    return final_content


def get_content(current_info, content_text):
    data = {
        "section" : current_info[0],
        "title" : current_info[1],
        "page_no" : current_info[2],
        "content" : clean_text(content_text)
    }
    return data


def save_csv_file(data, output_file):
    columns = ["section", "title", "page_no", "content"]
    df = pd.DataFrame(columns = columns)
    for i in range(len(data)):
        df = df.append(data[i], ignore_index = True)
    df.to_csv(output_file)
    return True


def save_text_file(data, output_file):
    file = open(output_file, "w+")
    for i in range(len(data)):
        line = data[i]["section"] + "|" + data[i]["title"] + "|" + data[i]["page_no"] + "\n"
        file.write(line)
        file.write(data[i]["content"])
        file.write("\n---------------------------------------------------------\n\n")
    file.close()
    return True

def get_book_data(file_name):
    file = open(file_name, "r")
    content_collect = False
    current_info = []
    content = ""
    all_data = {}
    index = 0
    for line in file:
        if book_section(line):
            if content_collect:
                all_data[index] = get_content(current_info, content)
                index += 1
                content = ""
            else:
                content_collect = True
            current_info = line[11:].strip().split("|")
        else:
            content += line
    return all_data

def main_function(input_file, output_csv_file):
    all_data = get_book_data(input_file)
    save_csv_file(all_data, output_csv_file)
    # save_text_file(all_data, output_txt_file)
    return True



input_file = "geometry_book.txt"
output_csv_file = "geometry_book_content.csv"

main_function(input_file, output_csv_file)
