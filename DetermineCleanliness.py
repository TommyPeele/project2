import pandas as pd

dataFrame = pd.read_csv("isis_sample.csv", sep=",", encoding="latin1")
print("isis_sample.csv Cleanliness Evaluation")

validTerms = dataFrame[dataFrame["Term"].notnull()]
validHandles = dataFrame[dataFrame["Handle"].notnull()]
validIDs = dataFrame[dataFrame["ID"].notnull()]
validTimes = dataFrame[dataFrame["Time"].notnull()]
validTexts = dataFrame[dataFrame["Text"].notnull()]

print("Number of tweets with missing Term values:", len(dataFrame) - len(validTerms))
print("Number of tweets with missing Handle values:", len(dataFrame) - len(validHandles))
print("Number of tweets with missing ID values:", len(dataFrame) - len(validIDs))
print("Number of tweets with missing Time values:", len(dataFrame) - len(validTimes))
print("Number of tweets with missing Text values:", len(dataFrame) - len(validTexts))

dataFrame = pd.read_csv("NewUserTweets.csv", sep=",", encoding="latin1")
print("NewUserTweets.csv Cleanliness Evaluation")

validTerms = dataFrame[dataFrame["Term"].notnull()]
validHandles = dataFrame[dataFrame["Handle"].notnull()]
validLocations = dataFrame[dataFrame["Location"].notnull()]
validLanguages = dataFrame[dataFrame["Language"].notnull()]
validDefaultImages = dataFrame[dataFrame["Default Image"].notnull()]
validFollowerCount = dataFrame[dataFrame["Follower Count"].notnull()]
validFriendCount = dataFrame[dataFrame["Friend Count"].notnull()]
validStatusCounts = dataFrame[dataFrame["Status Count"].notnull()]
validIDs = dataFrame[dataFrame["ID"].notnull()]
validTimes = dataFrame[dataFrame["Time"].notnull()]
validRetweetCounts = dataFrame[dataFrame["Retweet Count"].notnull()]
validTexts = dataFrame[dataFrame["Text"].notnull()]

print("Number of tweets with missing Term values:", len(dataFrame) - len(validTerms))
print("Number of tweets with missing Handle values:", len(dataFrame) - len(validHandles))
print("Number of tweets with missing Location values:", len(dataFrame) - len(validLocations))
print("Number of tweets with missing Language values:", len(dataFrame) - len(validLanguages))
print("Number of tweets with missing Default Image values:", len(dataFrame) - len(validDefaultImages))
print("Number of tweets with missing Follower Count values:", len(dataFrame) - len(validFollowerCount))
print("Number of tweets with missing Friend Count values:", len(dataFrame) - len(validFriendCount))
print("Number of tweets with missing Status Count values:", len(dataFrame) - len(validStatusCounts))
print("Number of tweets with missing ID values:", len(dataFrame) - len(validIDs))
print("Number of tweets with missing Time values:", len(dataFrame) - len(validTimes))
print("Number of tweets with missing Retweet Count values:", len(dataFrame) - len(validRetweetCounts))
print("Number of tweets with missing Text values:", len(dataFrame) - len(validTexts))
