from bs4 import BeautifulSoup

def generateCSV(inputFilename, outputFilename, element, tags):
    inputData = []
    outputData = ""

    for tag in tags:
        inputData.append(tag)
        outputData += tag + ","
    outputData = outputData[:-1]  # Removes final, unnecessary comma from header row

    with open(inputFilename, "rb") as inputFile, open(outputFilename, "w") as outputFile:
        outputFile.write(outputData + "\n")

        for line in inputFile:
            soup = BeautifulSoup(line, "lxml")
            currentElement = soup.find_all(element)

            isEmpty = 1
            outputData = "\""

            for x in range(0, len(tags)):
                try:
                    inputData[x] = currentElement[0].find_all(tags[x])[0].get_text()

                    if tags[x] == "text":
                        inputData[x] = inputData[x].replace(",", "")
                        inputData[x] = inputData[x].replace("\"", "")

                    if(inputData[x] != ""):
                        isEmpty = 0

                    outputData += inputData[x] + "\",\""
                except IndexError:
                    "Error with line..."

            if isEmpty == 0:
                outputData = outputData[:-3]
                outputData += "\"\n"
                outputFile.write(outputData)

twitterTweet = "tweet"
tagSet1 = ["term", "handle", "id", "time", "text"]
# generateCSV("isis.txt", "isis.csv", twitterTweet, tagSet1)
generateCSV("isis_sample.txt", "isis_sample.csv", twitterTweet, tagSet1)

tagSet2 = ["term", "handle", "location", "language", "default_image", "follower_count", "friend_count", "status_count", "id", "time", "retweet_count", "text"]
generateCSV("NewUserTweets.txt", "NewUserTweets.csv", twitterTweet, tagSet2)

tagSet3 = ["term", "handle", "location", "language", "default_image", "follower_count", "friend_count", "status_count", "id", "time", "retweet_count", "text", "l1score", "l2score"]
generateCSV("ProcessedTweets.txt", "ProcessedTweets.csv", twitterTweet, tagSet3)

# redditSubmission = "submission"
# tagSet4 = ["username", "postid", "time", "title", "subreddit", "score", "num_comments", "text"]
# generateCSV("AllRedditSubmissions.txt", "AllRedditSubmissions.csv", redditSubmission, tagSet4)

# tagSet5 = ["username", "postid", "time", "title", "subreddit", "score", "num_comments", "text", "plistscore"]
# generateCSV("ProcessedSubmissions.txt", "ProcessedSubmissions.csv", redditSubmission, tagSet5)

redditComment = "comment"
tagSet6 = ["username", "postid", "time", "subreddit", "score", "gold", "text"]
generateCSV("AllRedditComments.txt", "AllRedditComments.csv", redditComment, tagSet6)

tagSet7 = ["username", "postid", "time", "subreddit", "score", "gold", "text", "plistscore"]
generateCSV("ProcessedComments.txt", "ProcessedComments.csv", redditComment, tagSet7)
