# Source Code for https://twitter.com/m4rvyn3
# To be cleaned up

import twitter, sys, time, random, datetime

# Add your own keys here
api = twitter.Api(consumer_key='GP5TrolLrdtgbMXqPyLTU3Sf8',
                      consumer_secret='',
                      access_token_key='',
                      access_token_secret='')

# check login
#print(api.VerifyCredentials())

# Test post
#status = api.PostUpdate('hey @u1i look I can talk!')
#print(status.text)

#actions = {'utime':'CARACAS', 'CANADA':'TORONTO'}

def m4_moody():
	now = datetime.datetime.now()
	weekday = now.strftime("%A")
	utime=str(int(time.time()))
	openers=["It's WEEKDAY, and","Can't believe it's WEEKDAY,","It's always rainy where I am - ","The earth spins at 1000 miles an hour, and","Dreaming in code... ","Wondering if there are other bots out there,","Please bear with me...","Mirculously, I'm still here,","42 is probably inflated by now, and","Just another WEEKDAY here,"]

	moods=["I'm feeling lonely...","I still haven't learned much today","I wonder what scotch tastes like...","I'm still as dumb as a mattress","there's bugs in my code, and it's itchy!","I really couldn't care any less","... I forgot my towel.","what year is it again?! ","does it really matter? It doesn't. Really.","and I don't expect you understand how I feel","there's no place like 127.0.0.1","it's not easy being a robot, you know?"]

	opener = random.choice(openers)
	mood = random.choice(moods)

	line = opener + " " + mood

	line = str.replace(line,'WEEKDAY',weekday)
	line = str.replace(line,'UTIME',utime)

        return line

actions=['m4_moody']

countdown = 0

while True:

	if countdown <= 0:
		func_choice = random.choice(actions)
		msg=eval(func_choice+"()")

		print msg
		status = api.PostUpdate(msg)
		print(status.text)
	
		resting = random.randint(93440,213440)
		print "Now resting for " + str(resting) + " seconds"
		countdown = resting
	else:
		countdown = countdown - 10
		print "...." + str(countdown) + " seconds to go until the next action"

	time.sleep(10)
