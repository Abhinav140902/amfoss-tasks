# Geddit

## Task
The task is to write a script using golang that can:
- Perform a search for subreddits using 'memes' as search query
- Pick the subreddit that occurs as the first search result
- Upvote posts posted in the last week (100 posts at max).

## Installation
- Firstly I have installed go by entering the following command: `$ sudo wget https://golang.org/dl/go1.15.5.linux-amd64.tar.gz`
- The latest version of go-reddit can be installed by entering the following command: `go get github.com/vartanbeno/go-reddit`
- After installing, you can check the version of go using the following command: `$ go version`

## Method of Approach
- Initially I have created an account in the reddit and logged in.
- After logging in, I have created an app in this [website](https://www.reddit.com/prefs/apps).
- After creating the app, I have got my client id and secret id by the following [steps](https://www.geeksforgeeks.org/how-to-get-client_id-and-client_secret-for-python-reddit-api-registration/).
-The I have wrote the code to set the search query as 'memes' and set the time as week and limit upto 100 posts.
-So that all the 100 top posts are obtained and are upvoted.
-Enter the client id, Secret, Username and password just after the variables.

That's it!! The task is done.
