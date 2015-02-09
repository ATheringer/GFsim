# This is the girlfriend.py source code. Feel free to edit it
# to get personalized girlfriends. Enjoy your feels ;-;
# 
# Created by The Ringer

import sys

def formatter():
	print()
	print()
	print()
	print()
	print()
	print()
	print()
	print()
	print()
	print()
	print()
	print()
	print()
	print()
	print()
	
def choice1(x, gf):
	if x == 'a':
		formatter()
		print(gf, ": Oh wonderful! You know I've missed you SOOO much while you were gone. \n",\
			"So where are you taking me for Valentine's Day? \n",\
			"a. Fancy Dinner \n b. Fancy Diner \n c. Let's just stay home and cuddle \n",\
			"d. Your ass is mine tonight")
	elif x == 'b':
		formatter()
		print(gf, ": No good? I'm sorry, sweetie. I know! Let's go have some Valentine's Day \n",\
			" fun to cheer you up! Where should we go? \n",\
			"a. Fancy Dinner \n b. Fancy Diner \n c. Let's just stay home and cuddle \n",\
			"d. Your ass is mine tonight")
	else: naughty()
	
def choice2(x, gf):
	if (x == 'a') or (x == 'b'):
		formatter()
		print(gf, ": Yay! A night out on the town! But I need something to wear. What do you \n",\
		"think? The red dress or the black dress? \n",\
		"a. Red Dress \n b. Black Dress \n c. You look good either way \n",\
		"d. You look better with a bag over your head")
		c3 = input()
		choice3a(c3, gf)
	elif x == 'c':
		formatter()
		print(gf, ": Ooh, staying home? That's fine with me. What should we do first? \n",\
		"a. Let's make popcorn and watch movies with Bill Murray \n",\
		"b. Rape Time. Get upstairs. \n c. Internetttttt \n d. INTERNETTTTT")
		c3 = input()
		choice3b(c3, gf)
	elif x == 'd':
		formatter()
		print(gf, ": No. Your ass is mine tonight. \n Your gf hunches over and huge wings",\
			" erupt from her back, spread out, and fill the room.\n Her face twists and",\
			" contorts and becomes a hideous forray of teeth, scales, and drool. She",\
			" screams a bloodcurdling scream and devours you whole. You are now dead.",\
			" \n Bad end. Play again?")
		play = input("y/n: ")
		if play == 'y': main()
		elif play == 'n': sys.exit()
		
	else: naughty()
	
	
def choice3a(x, gf):
	if x == 'a':
		formatter()
		print(gf, ": Ah, what do you know? I'm going with the black one. \n",\
			"You drive with your gf to the restaurant. When you get there \n",\
			"you are immediately seated. A waiter comes and asks what you \n",\
			"would like to drink.\n",\
			"a. Champagne \n b. Red Wine \n c. BEER! \n d. Gallons of semen")
		c4 = input()
		choice4(c4, gf)
	elif (x == 'b') or (x == 'c'):
		formatter()
		print(gf, ": Ah, what do you know? I'm going with the red one. \n",\
			"You drive with your gf to the restaurant. When you get there \n",\
			"you are immediately seated. A waiter comes and asks what you \n",\
			"would like to drink.\n",\
			"a. Champagne \n b. Red Wine \n c. BEER! \n d. Gallons of semen")
		c4 = input()
		choice4(c4, gf)
	elif x == 'd':
		formatter()
		print(gf, ": Funny. I was going to say the same thing. \n",\
			"Your gf proceeds to suffocate you with a plastic bag. Panicked, \n",\
			"you start flailing your arms wildly to escape her grasp. Unfortunately, \n",\
			"you bludgeon your gf to death because your hands are cinderblocks. \n",\
			"The cops arrive shortly after and you are charged with manslaughter, \n",\
			"put in prison and raped by Big Black Steve on a regular basis. \n"
			"Your asshole now whistles when it's windy outside.\n",\
			" \n Bad end. Play again?")
		play = input("y/n: ")
		if play == 'y': main()
		elif play == 'n': quit()
	else: naughty()

def choice3b(x, gf):
	if x == 'a':
		formatter()
		print(gf, ": OMG I LOVVVEEE BILL MURRAY!! Let me go get some movies! \n",\
			"Your gf leaves to peruse the DVD stack upstairs. While she is \n",\
			"upstairs, Bill Murray himself comes in through the front door \n",\
			"buck-naked and smoking a cuban cigar shaped like a penis. When \n",\
			"he sees you, he charges you, slams you on the ground, and begins \n",\
			"to force you to smoke the cigar, yelling \"Take it, take it!\" \n",\
			"You scream as he puts a rag over your mouth and it all went black.\n",\
			" When you come to you are bound to a chair wearing a corset and fishnet\n",\
			"stockings with a pair of crotchless french cut panties. Lipstick is \n",\
			"crudely smeared over your mouth and a man in a balaclava is \n",\
			"standing before you with one of those foam pool noodles. \n",\
			"He puts a tape in your vcr and it plays this Thai midget tranny porn \n",\
			"and he begins to hit your genitals with the pool noodle, yelling \n",\
			"\"Say you're a sissy little schoolgirl who wants her daddy!\" \n",\
			"Eventually you succumb to the humiliation and pain and cry out \n",\
			"\"I'm a sissy little schoolgirl who wants her daddy!\" \n",\
			"The man in the balaclava smiles then forcefully grabs you \n",\
			"and kisses you hard and long on the lips. He then takes off his \n",\
			"mask and reveals that he is Bill Murray. As he climbs out the window \n",\
			"he looks back and winks and says \"Nobody will ever believe you\" \n",\
			" \n Murray end. Play again?")
		play = input("y/n: ")
		if play == 'y': main()
		elif play == 'n': quit()
	elif x == 'b':
		formatter()
		print(gf, ": Rape time? I agree.\n",\
			"Your gf rapes you to death. You die in a pool of your own ass blood.\n",\
			" \n Bad end. Play again?")
		play = input("y/n: ")
		if play == 'y': main()
		elif play == 'n': quit()
	elif (x == 'c') or (x == 'd'):
		formatter()
		print(gf, ": YES INTERNETTTT \n",\
			"You and your gf shitpost on 4chan for hours. What a wonderful world.\n",\
			" \n Good end. Play again?")
		play = input("y/n: ")
		if play == 'y': main()
		elif play == 'n': quit()
	else: naughty()
			
def choice4(x, gf):
	if (x == 'a') or (x == 'b') or (x == 'c'):
		formatter()
		print("Waiter: Certainly. And for you mam? \n", gf,\
			" : I'll have the same. \n",\
			"Waiter: Right away. *he leaves* \n", gf,\
			" : Ah, it's so nice to be out like this! What should we get to eat? \n",\
			"a. I'm in the mood for steak! \n b. Eh, something light like pasta \n",\
			"c. Millions of dicks. \n")
		c5 = input()
		choice5(c5, gf)
	elif x == 'd':
		formatter()
		print("You drown in gallons of semen. \n"
		"This is either a bad end or a good end depending on the person. Play again?")
		play = input("y/n: ")
		if play == 'y': main()
		elif play == 'n': quit()
	else: naughty()
	
def choice5(x, gf):
	if (x == 'a') or (x == 'b'):
		formatter()
		print(gf, ": You're so boring! I'm thinking something spicy! Maybe enchiladas! \n",\
			"*30 minutes pass* \n",\
			"Uggh, what's taking so long? It's been like 30 minutes!\n",\
			"a. Don't worry dear, I'm sure the waiter will come around soon \n",\
			"b. Yeah you're right. Fuck it, let's go to Steak and Shake \n")
		c6 = input()
		choice6(c6, gf)
	elif x == 'c':
		formatter()
		print("You drown in a million dicks. \n",\
		"This is either a bad end or a good end depending on the person. Play again?")
		play = input("y/n: ")
		if play == 'y': main()
		elif play == 'n': quit()
	else: naughty()
	
def choice6(x, gf):
	if x == 'a':
		formatter()
		print(gf, ": ...if you say so. I just don't want to wait around here forever. \n",\
			"A tall, muscular man walks by your table, pauses, turns and looks at \n",\
			"your gf. \n Chad:", gf, "?! I never thought I'd see you here! \n",
			gf, ": Chad! Oh, goodness, um, *blushes*, yeah! I'm uh, I'm here with my \n",\
			"*she clears her throat* my, boyfriend. Sweetie, this is Chad, my... my ex.\n",\
			"Chad looks at you and smirks. \n Chad: This guy? Wow, what a wimp!\n",\
			"a. Say nothing \n b. Tell him he's interrupting your date. \n c. Hey, fuck you guy! \n")
		c7 = input()
		choice7(c7, gf)
	elif x == 'b':
		formatter()
		print(gf, ": FUCK YEAR STEAKNSHAKE \n You and your gf go to Steak and Shake and \n",\
		"have delicious steakburgers and shakes. Then you go home and fuck for hours.",\
		"Best End. Play again?")
		play = input("y/n: ")
		if play == 'y': main()
		elif play == 'n': quit()
	else: naughty()
	
def choice7(x, gf):
	if x == 'a':
		formatter()
		print(gf, ": You're not going to say anything?\n",\
			"You shake your head solemnly.\n",\
			"Chad (laughing): Oh, come on! What a little bitch! Come on,", gf, ",",\
			"let's get out of here! \n Your gf looks down and avoids your eyes, \n",\
			"and leaves the restaurant. You wake up and realize that you can't \n",\
			"even hold onto a girl in your dreams, begin to cry, and finally take \n",\
			"that pistol out of the bedstand and pull the trigger. \n",\
			"Bad end. Play again?")
		play = input("y/n: ")
		if play == 'y': main()
		elif play == 'n': quit()
	elif x == 'b':
		formatter()
		print("Chad: Ah, you're right, dude. Sorry about that - that was rude of me. \n",\
			"I'll let you two do your thing. Can I have a hug before I go, though? \n",\
			"Your gf stands up and embraces Chad, squeezing his shoulder blades and \n",\
			"breathing in his cologne. He winks at her, and turns to leave. Your gf \n",\
			"sits back down.\n ", gf, ": Sorry about that. He can be a jerk sometimes. \n",\
			"You assure your gf that it's nothing to worry about. The waiter finally \n",\
			"comes and you order your food. However, your gf seems distracted. \n",\
			"You eat your food in silence, and then leave the restaurant and begin \n",\
			"to drive home. However, on the way, your car jumps and sputters, and \n",\
			"dies on you in the middle of the road. Your gf sighs loudly and turns \n",\
			"away. After a few moments of toying with the engine (you don't know the \n",\
			"first thing about cars) headlights shine on your back and a red ferrari \n",\
			"pulls up. Chad is in the driver's seat. \n Chad: Hey buddy, what ",\
			"happened? \n a. Ask for help \n b. Tell him you've got in under control. \n")
		c8 = input()
		choice8a(c8, gf)
	elif x == 'c':
		formatter()
		print("Chad: Fuck me? Fuck you! You better be careful buddy, I'll take your ass \n",\
			"out to dry. \n", gf, ": Chad, please, don't. \n Chad: Hey, calm down ",\
			"little lady. So what do you say punk? You wanna take this outside?\n",\
			"a. No, I don't want to fight you \n b. I'll take you on. \n")
		c8 = input()
		choice8b(c8, gf)
	else: naughty()
	
def choice8a(x, gf):
	formatter()
	print("Chad: Nah, I don't mind helping you out. \n He gets out of his car. \n",\
		"Chad: Alright, let's see here... *moments pass* ...ooh, this is bad. \n",\
		"It looks like your alternator belt is shot. You're going to want to \n",\
		"get this thing towed - don't want to drive without an alternator belt. \n",\
		"You guys need a lift in the meantime? My car only seats two, though, haha! \n",\
		"You tell your gf to go ahead and go home and wait for you, while you wait \n",\
		"here for the tow truck. Your gf agrees almost too quickly, and gets in \n",\
		"the car with Chad. \n", gf, ": Bye, sweetie! \n They drive off. When the truck finally comes, \n",\
		"you call a cab and head home. When you get to the door, you notice that the door is unlocked, \n",\
		"and that your gf's nice dress is lying crumpled at the doorstep. As you ascend the stairs, \n",\
		"the familiar noise of the bed's creaking grows louder, in addition to the new noise of your \n",\
		"gf moaning in pleasure like you've never heard her before. You crumple down into a ball \n",\
		"outside of the door. The noises continue for hours until Chad emerges naked, \n",\
		"glistening, and sees you lying on the ground. He laughs, and then returns to \n",\
		"the bedroom for round two. \n Bad end. Play again?")
	play = input("y/n: ")
	if play == 'y': main()
	elif play == 'n': quit()
	
def choice8b(x, gf):
	if x == 'a':
		formatter()
		print("Chad grabs you by the cuff of your shirt and pulls you out of your seat. \n",\
			"He takes you outside and throws you down onto the ground. A couple \n",\
			"of blows to the head and you're out cold. Moments pass and you \n",\
			"come to, and your gf is nowhere to be found. She's not picking up her phone, either. \n",\
			"You call a cab and when it came near the License plate said FRESH and had a dice in the mirror \n",\
			"If anything you could say that this cab was rare\n",\
			"But you thought nah, forget it, yo homes to Bel-air!\n\n",\

			"I pulled up to a house about seven or eight\n",\
			"And I yelled to the cabby \"Yo, homes smell you later!\"\n",\
			"Looked at my kingdom I was finally there\n",\
			"To sit on my throne as the prince of Bel-air\n\n",\
			"Bel air end. Play again?")
		play = input("y/n: ")
		if play == 'y': main()
		elif play == 'n': quit()
	elif x == 'b':
		formatter()
		print(gf, ": No, you don't have to do this. \n You ignore your gf. ",\
			"This guy has been way too cocky, and it's time to put him in his place.\n",\
			"Luckily, you've taken brazilian jujitsu classes for 15 years.\n",\
			"The battle is over in 10 seconds, Chad laying on the ground.\n",\
			"You turn to your girlfriend, and you can tell she's soaked.\n",\
			"You smirk and throw her over your shoulder, drive her home, \n",\
			"and fuck each other's brains out for hours before passing out in \n",\
			"a euphoric frenzy. \n Good End. Play again?")
		play = input("y/n: ")
		if play == 'y': main()
		elif play == 'n': quit()
	else: naughty()
	
	
def naughty():
	formatter()
	print("You have broken the gf simulator. Please try again.")
	main()

def main():
	print("Welcome to the Girlfriend Simulator v1.0!")
	gf = input("Enter your gf's name: ")
	print("Thank you! Your gf's name is ", gf)
	print("Initializing...")
	formatter()
	print(gf, ": Hi Sweetie! How was your day? \n a. Good, and yours, sugar bear? \n b. Not so good ;_; \n (please input a or b in lowercase)")
	c1 = input()
	choice1(c1, gf)
	c2 = input()
	choice2(c2, gf)
	
main()
	
