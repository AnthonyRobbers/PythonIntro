import urllib

def get_text():
    contents_of_file = raw_input("The text to be converted:")
    # raw_input is required since it tries to execute anything given not get a string
    
    profane_or_pirate = input("1 for profanity check and 2 for pirate conversion.")
    if profane_or_pirate == 1:
        check_profanity(contents_of_file)
    elif profane_or_pirate == 2:
        make_it_piraty(contents_of_file)
    else:
        print("that was not a 1 or 2")

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


get_text()

