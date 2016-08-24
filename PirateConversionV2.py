import urllib

def get_text():
    contents_of_file = raw_input("The text to be converted:")
    # raw_input is required since it tries to execute anything given not get a string
    return contents_of_file

def read_text():
    quotes = open("C:\Python27\movie_quotes.txt")
    contents_of_file = quotes.read()
    #print(contents_of_file)
    quotes.close()    
    return contents_of_file


def check_profanity(text_to_check):
    connection = urllib.urlopen("http://www.wdylike.appspot.com/?q="+text_to_check)
    output = connection.read()
    print(output)
    connection.close()
    
# for pirate contersion - http://isithackday.com/arrpi.php?text=
# for profanity check - http://www.wdylike.appspot.com/?q=


def make_it_piraty(text_to_check):
    connection = urllib.urlopen("http://isithackday.com/arrpi.php?text="+text_to_check)
    output = connection.read()
    print(output)
    connection.close()

def Output_step(text_to_check):
    profane_or_pirate = input("1 for profanity check and 2 for pirate conversion.")
    if profane_or_pirate == 1:
        check_profanity(text_to_check)
    elif profane_or_pirate == 2:
        make_it_piraty(text_to_check)
    else:
        print("that was not a 1 or 2")

def decide():
    file_or_type = input("1 for reading from a prompt and 2 for read from file.")
    if file_or_type == 1:
        Output_step(get_text())
    elif file_or_type == 2:
        Output_step(read_text())
    else:
        print("that was not a 1 or 2")


        
decide()

