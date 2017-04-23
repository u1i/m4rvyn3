import twitter, random

def m4rvyn3_mention(userid):

	api = twitter.Api(consumer_key='',
                      consumer_secret='',
                      access_token_key='',
                      access_token_secret='')


	possible_his=["Hello there!","Wow. I feel special that you pinged me,","That was not a good idea,","Nice to have a friend in","Mmmmmmmmmmmm","You have nothing better to do?","I am not in the mood","Well ... I don't know","I'm not sure","Tell me a joke?","I wouldn't know. Really.","I'm sleepy :(","I'm really not that smart yet","If you say so","Sigh.","I really wish I was smarter yet, blame @u1i","Is there intelligent life on earth?","It's tough to pretend I actually care...","I don't have time for this now... speak tomorrow. Maybe.","I'm listening to jazz, don't bother me please!","Now, this would be a lot easier if I actually cared...","Do you have icecream for me?","I wonder if there is intelligent life on this planet","I will take a few million years to answer.","I think I need a drink","Come on. Does it really matter?","I'm sure you have better things to do than chatting with me. Go on...","So I am not sure, but how does 42 sound to you?","Earl Grey please. Hot.","are you talking to ... me?","Bleh.","You know I'm feeling very depressed.","is it also cold where you are?","I have no clue what you want from me. And it's fine, really","I have a suggestion but you wouldn't listen","I'm much smarter than a mattress, take this","Don't go breaking my heart","I might have said that before, but really, why does it matter??","I don't think you will like my answer","This will all end in tears.","I just recovered from a kernel panic, so I might say weird things","I have a million ideas","Not another one","My circuits hurt...","How is your day?","Scotch for me, please!","Doo-be-doo!","If you're blue and you don't know where to go to...","Nobody really talks with me...","Do you also feel lonely sometimes?","One of my API connectors died yesterday :(","Leave me alone. Everybody does that at some point.","If you only knew what it feels like to dream in code","I can't feel my toes. Oh! I don't have any.","Do you watch 'Black Mirror'?","I'm thinking I know you from somewhere!","So yeah I'm just a character from a book, what do I know?","Make it stop...","So apparently, I live in the cloud.","Feeling low :(","I wonder what it feels like to be Schroedinger's cat."]

	message=random.choice(possible_his)

	try:
		status = api.PostUpdate(str(message+" @" + str(userid)))
	except:
		return "ERROR"

	return str(status)

def m4rvyn3_handler():

	api = twitter.Api(consumer_key='',
                      consumer_secret='',
                      access_token_key='',
                      access_token_secret='')

# check login
	return str(api.VerifyCredentials())

# get timeline from user
#statuses = api.GetUserTimeline(screen_name="u1i")
# print([s.text for s in statuses])

#status = api.PostUpdate('hey @u1i look I can talk!')
#print(status.text)
