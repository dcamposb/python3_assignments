# Project 2; Course 2; Prj: Sentiment Analysis
# Special thanks to RichardDanielOliva, some of his code was used as reference
# While the assignments request for several functions to made and nested
# I have changed the assignment code considerably with newly learned conventions
# from ladder courses

#### Local Parameters and Variables
# Opening the Twitter Dataset to Read & Output File to Write On
twitter_data_file = open("twitter_data.csv","r")
visualization_data = open("viz_data.csv","w")

# Getting Punctuation Characters 
punctuation_character_list = [
    "'", '"', 
    ",", ".",
    "!", ":",
    ";", '#','@'
]

# Create an Empt Dictionary of Positive Words 
# Make a List of the positive words in the documents we have created separately 
dictionary_characters = {}
character_list = [
    "positive.txt", 
    "negative.txt"
]

#### Functions
# Create a function that gets the Punctuation
def strip_punctuations(word_lines, punctuation_character_list):
    """
    Strips a line from specified punctuations by replacing the
    punctuation with "" and empty character.

    :param word_lines:  the line that needs eliminating punctuation
    :return:  a linew withouth punctuation

    """
    # Dropping punctuations each sentence line
    for punctuation in punctuation_character_list: # for the desired punctuations
        word_lines = word_lines.replace(punctuation, "")

    return word_lines.split() # punctuation-less sentence

def get_sentiment_count(word_lines, punctuation_character_list):
    """
    Gets the count of positive and negatives words in a line, and store them in
    a dictionary as a list to the positive or negative key.

    :param word_lines: sentence to be analyzed
    :param punctuation_character_list: a list of excluded punctuations
    :return: a dictionary with the count of positive and negative values
    """

    # Stripping Punctuations from Sentences
    word_lines = strip_punctuations(word_lines,punctuation_character_list)
    word_lines = word_lines.split() # a list of words from each sentence without punctuation

    # Dictionary Counts of Negative and Positive Elements
    count_dictionary = {
        "positive.txt": 0 ,
        "negative.txt": 0
    }

    # For loop that count the number of positive and negative words
    for sentiment in dictionary_characters.keys():
        for word in word_lines:
            if word in dictionary_characters[sentiment]:
                count_dictionary[sentiment] += 1

    return count_dictionary

def create_count_document(visualization_data,twitter_data_file):
    """
    Funtion reads individual lines in a document, specificly a twitter api csv with
    retweens, responses and word information. The function then counts the number of
    positives and negatives and writes it down in a csv file which will be used
    for visualizaiton.

    :param visualization_data:  file in which you want to write your data to  plot
    :param twitter_data_file:  file from which you are reading the lines
    :return: a tabl with Number of Retweens, Replies, Positives Scores , Negatie Scores and Net Scores
    Columns detailing the quantified values from each linea, and from the previously detailed functions

    """

    #Prepping the Output Document
    visualization_data.write("Number of Retweets, Replies, Positive Score, Negative Score, Net Score")
    visualization_data.write("\n")

    # Reading
    all_document_lines = twitter_data_file.readlines()
    all_document_lines.pop(0)

    # Reading Data in the Document
    for lines in all_document_lines:
        lines = lines.strip().split(",")

        # Variables for Each line
        retweents = lines[1]
        replies = lines[2]
        positive_count = get_sentiment_count(lines[0], punctuation_character_list)["positive.txt"]
        negative_count = get_sentiment_count(lines[0], punctuation_character_list)["negative.txt"]

        # Writing to Document Columns
        visualization_data.write(
            f"{retweents},{replies},{positive_count},{negative_count},{positive_count-negative_count}"
        )

#### Operations
# This for loop stores the positive and negative characters
#  as list values in a empty dictionary which keys hold the positive or negative identifier 
for character_type in character_list: 
    if character_type not in dictionary_characters: 
        dictionary_characters[character_type] = []

    with open(character_type) as character_type_list: 
        for i in character_type_list: 
            if i[0] != ';' and i[0] != '\n': 
                dictionary_characters[character_type].append(i.strip())


# Creating the Viz Document & Closing Files
create_count_document(visualization_data,twitter_data_file)
twitter_data_file.close()
visualization_data.close()