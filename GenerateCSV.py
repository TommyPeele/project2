from bs4 import BeautifulSoup

inputFile = open("isis_sample.txt", "rb")
outputFile = open("isis_sample.csv", "w")

outputFile.write("Term,Handle,ID,Time,Text\n")
for line in inputFile:
    soup = BeautifulSoup(line, "lxml")
    tweet = soup.find_all("tweet")
    try:
        term = tweet[0].find_all("term")[0].get_text()
        handle = tweet[0].find_all("handle")[0].get_text()
        id = tweet[0].find_all("id")[0].get_text()
        time = tweet[0].find_all("time")[0].get_text()
        text = tweet[0].find_all("text")[0].get_text()
        text = text.replace(",", "")
        output = "\"" + term + "\",\"" + handle + "\",\"" + id + "\",\"" + time + "\",\"" + text + "\"\n"
        outputFile.write(output)
    except IndexError:
        "Error with line..."

inputFile.close()
outputFile.close()

inputFile = open("NewUserTweets.txt", "rb")
outputFile = open("NewUserTweets.csv", "w")

outputFile.write("Term,Handle,Location,Language,Default Image,Follower Count,Friend Count,Status Count,ID,Time,Retweet Count,Text\n")

for line in inputFile:
    soup = BeautifulSoup(line, "lxml")
    tweet = soup.find_all("tweet")
    try:
        term = tweet[0].find_all("term")[0].get_text()
        handle = tweet[0].find_all("handle")[0].get_text()
        location = tweet[0].find_all("location")[0].get_text()
        language = tweet[0].find_all("language")[0].get_text()
        default_image = tweet[0].find_all("default_image")[0].get_text()
        follower_count = tweet[0].find_all("follower_count")[0].get_text()
        friend_count = tweet[0].find_all("friend_count")[0].get_text()
        status_count = tweet[0].find_all("status_count")[0].get_text()
        id = tweet[0].find_all("id")[0].get_text()
        time = tweet[0].find_all("time")[0].get_text()
        retweet_count = tweet[0].find_all("retweet_count")[0].get_text()
        text = tweet[0].find_all("text")[0].get_text()
        text = text.replace(",", "")
        output = "\"" + term + "\",\"" + handle + "\",\"" + location + "\",\"" + language + "\",\"" + default_image + "\",\"" + follower_count + "\",\"" + friend_count + "\",\"" + status_count + "\",\"" + id + "\",\"" + time + "\",\"" + retweet_count + "\",\"" + text + "\"\n"
        outputFile.write(output)
    except IndexError:
        "Error with line..."

inputFile.close()
outputFile.close()
