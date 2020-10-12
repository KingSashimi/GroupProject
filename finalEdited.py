import random

moves = {"overheat": range(18, 26),
         "virus": range(10, 36),
         "download": range(10, 20)}


class Computerman:
    def __init__(self, health):
        self.health = health

    def attack(self, other):
        raise NotImplementedError


class Player(Computerman):
    def __init__(self, health=100):
        super().__init__(health)

    def attack(self, other):
        while True:
            choice = str.lower(input("\nWhat move would you like to make? (Overheat, Virus, or Download)"))

            if choice == "download":
                self.health += int(random.choice(moves[choice]))
                print("\nYour health is now {0.health}.".format(self))
                break
            if choice == "overheat" or choice == "virus":
                damage = int(random.choice(moves[choice]))
                other.health -= damage
                print("\nYou attack with {0}, dealing {1} damage.".format(choice, damage))
                break
            else:
                print("Not a valid move, try again!")


class Printerman(Computerman):
    def __init__(self, health=100):
        super().__init__(health)

    def attack(self, other):
        if self.health <= 35:
            moves_1 = ["overheat", "virus", "download", "download", "dwonload", "download", "download"]
            cpu_choice = random.choice(moves_1)
        else:
            cpu_choice = random.choice(list(moves))
        if cpu_choice == "virus" or cpu_choice == "overheat":
            damage = int(random.choice(moves[cpu_choice]))
            other.health -= damage
            print("\nThe Printerman attacks with {0}, dealing {1} damage.".format(cpu_choice, damage))
        if cpu_choice == "download":
            self.health += int(random.choice(moves[cpu_choice]))
            print("\n Printerman uses download and its health is now {0.health}.".format(self))


def battle(player, Printerman):
    print("Printerman enters...")
    while player.health > 0 and Printerman.health > 0:
        player.attack(Printerman)
        if Printerman.health <= 0:
            break
        print("\nThe health of Printerman is now {0.health}.".format(Printerman))
        Printerman.attack(player)
        if player.health <= 0:
            break
        print("\nYour health is now {0.health}.".format(player))
    if player.health > 0:
        print("You defeated Printerman")
    if Printerman.health > 0:
        print("You were defeated by Printerman")

if __name__ == '__main__':

    #battle(Player(), Printerman())
	def checkInput(size):
		choiceArray = ["A", "B", "C", "D", "E"]
		while True:
			inp = input("What choice?")
			inp = inp.upper()
			for x in range (size):
				if (inp == choiceArray[x]):
					return (inp)
					break			
			print("Not a valid input")
					

	print('       "MUM" Mac yelled as he scanned through boxes of wires to find his USB wire.\n\
			Mac took another quick glance around his room, hoping to find his cable.\n\
			Mac recently came back from a phishing trip with his colleagues, which he claims he enjoyed very much.\n\
			\n\
			A - Look at the poster.\n\
			B - On my desk perhaps?\n\
			C - Under the bed?')
	choice = checkInput(3)
	if (choice == "A"):
		print("        Mac stares at the poster of his Hyper-Advanced AI powered Turbo-Inkjet printer.\n\
			 	He wondered to himself why anyone would need an AI powered printer but the search for the cable was more important.\n\
			 	In fact who even has a poster of a printer anyway?\n\
			  \n\
			 	A -  Frustrated he did what anyone in his situation would, MUMMMMMY.")
		choice = checkInput(1)
	elif (choice == "B"):
		print("        The desk is cluttered with PC components, empty bottles of powerade and half eaten cups of instant noodles.\n\
			 	Unfortunately the cable is not here.\n\
			  \n\
			 	A - There is but one option MUMMMMMY.")
		choice = checkInput(1)
	elif (choice == "C"):
		print('        All his could find was dustBits under his bed, and a familiar box at the back, tucked away in secret with the words\n\
				 	"Private, P.S that means for you too Mom". He looked away in shame and carried on with his search.\n\
				  \n\
				 	A - Reminded of his mother he had one choice, MUMMMMMY.')
		choice = checkInput(1)
	else:
			pass
	if (choice == "A"):
			print("        “Malcom, you left it under your pillow” his mother screamed up the stairs.\n\
					Of course it was, he knew that.\n\
					\n\
					A - Look under the pillow.")
			choice = checkInput(1)
	else:
			pass
	if (choice == "A"):
			print("        Mac flipped over his pillows to find the wire exactly there,\n\
					he desperately wanted to upload the pictures from the trip to print and frame them for the office.\n\
					Mac wasn’t the most popular at work, being one of the youngest and least experienced, but he wouldn’t give up.\n\
					\n\
					\n\
						  He grabbed his camera and started flicking through the images.\n\
					\n\
					A - Put the camera down.\n\
					B - Inspect the photos.")
			choice = checkInput(2)

	if (choice == "B"):
			print("        Mac looks through the photos, hoping to find some instance of him having a good time but as he scrolled he came to the slow realisation he wasntin any of the photos.\n\
					He was always the photographer but never the photographee.\n\
					\n\
					\n\
					A - Feeling even worse than when he had started he decided to put the camera down")
			choice = checkInput(1)
	else:
			pass
	if (choice == "A"):
			print("        He was alone. He was unwanted. He didn’t belong.\n\
					\n\
					“Why do I bother trying, they're never going to accept me” Mac contemplated to himself.\n\
					\n\
					After a few moments he cleared his head and got back up, wire in hand ready for the next step.\n\
					\n\
					RING RING\n\
					\n\
					He looked at his phone, it was work. He stood for a moment, he knows whatever it is it can't be good.\n\
					\n\
					\n\
					A - Answer the phone, how bad could it really be.\n\
					B - Ignore it, if its important they will call back.")
			choice = checkInput(2)
	else:
			pass
	if (choice == "A"):
			print('        He wasnt in the mood to talk to work right now. He just wanted to be alone with his thoughts and his camera.\n\
					He may be alone but he will always have his computer to keep him company.\n\
					\n\
					At that moment a text message popped up on his phone.\n\
					\n\
					“Malcom, I hate to be the bearer of bad news but we have had multiple issues with our computers at work, rendering them nonfunctional.\n\
					To cover the cost of the new servers and computers we have had to make cuts to the team.\n\
					I am sorry Malcom, being one of the last to join it makes sense, we have to let you go. Take care. Goodbye.”\n\
					\n\
					A - ...what?')
			choice = checkInput(1)
	elif (choice == "B"):
			print('        “Hello” Mac responded as he answered his phone.\n\
					\n\
					“Malcom, I hate to be the bearer of bad news but we have had multiple issues with our computers at work, rendering them nonfunctional.\n\
					To cover the cost of the new servers and computers we have had to make cuts to the team.\n\
					I am sorry Malcom, being one of the last to join it makes sense, we have to let you go. Take care. Goodbye.”\n\
					\n\
					A - ...what?')
			choice = checkInput(1)
	else:
			pass
	if (choice == "A"):
			print('        Mac was frozen, in shock, heart pounding like air was never going to reach his lungs and this was it for him.\n\
					\n\
					He collapsed on his GT omega racing chair trying to comprehend the phone call he had just received.\n\
					\n\
					Moments passed and he still remained in shock.\n\
					He told himself it couldn’t be real, it was just a prank, they play them on him all the time.\n\
					He decided to continue what he was doing before, acting as though the phone call never happened.\n\
					\n\
					“It was just a joke,” Mac told himself.\n\
					\n\
					A - Open Latch')
			choice = checkInput(1)
				  
	if (choice == "A"):
			print("        He opened the latch covering the USB slots on his computer, which he built himself, plugging the camera into one end and placing it on the desk.\n\
					He took the other end and pushed the USB into its socket.\n\
					\n\
					A - Put in quick!\n\
					B - Put in slowly")

	choice = checkInput(2)
	if choice == "A":
			print("        “AHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH” Mac screamed in agony.")
			print("        A shock of electricity ran through his body as thunder pounded in the background.\n\
					His hands were shaking as he absorbed the power from his machine. \n\
					'It was so much that power he felt invincible, immortal and unshakable.'\n\
					\n\
					He looked around the room trying to gain a sense of reality.\n\
					His eyes were blurring, focus disappearing but he noticed something.\n\
					\n\
					The inkjet printer was gone.\n\
					\n\
					Moments passed as his vision returned but still unbalanced, still absorbing something within his body, but what?\n\
					\n\
					A - What was it?")
			choice = checkInput(1)
	elif choice == "B":
			print ("        A shock of electricity ran through his body as thunder pounded in the background.\n\
					His hands were shaking as he absorbed the power from his machine. \n\
					'It was so much that power he felt invincible, immortal and unshakable.'\n\
					\n\
					He looked around the room trying to gain a sense of reality.\n\
					His eyes were blurring, focus disappearing but he noticed something.\n\
					\n\
					The inkjet printer was gone.\n\
					\n\
					Moments passed as his vision returned but still unbalanced, still absorbing something within his body, but what?\n\
					\n\
					A - What was it?")
			choice = checkInput(1)

	else:
		pass
	if choice == "A":
		print('        As Mac fell back from the sheer force of the current, he discovered his veins becoming tri-coloured upon waking up from a sleepy hase.\n\
				There was no pulse yet he could feel his body pulsating with a new type of blood flow.\n\
				\n\
				A - Look at red vein. \n\
				B - Look at blue vein. \n\
				C - Look at yellow vein.')
	choice = checkInput(3)

	if choice == "A":
	   print ("       it's blood\n\
				\n\
				A - ...")
	   choice = checkInput(1)

	elif choice == "B":
		print ("        Blue, so blue it could only be compared to that blue powerade drink, this was the data buses. \n\
				The data was being carried through his new veins to his brain and around his body as the control unit took over his senses\n\
				\n\
				A - ...")
		choice = checkInput(1)

	elif choice == "C":
		print ("        Yellow like monster energy; an address bus carrying the addresses for functions. \n\
			   He tried to pick up his hand and his wrist illuminated with a series of binary digits\n\
				\n\
				A - ...")
		choice = checkInput(1)

	if choice == "A" or "B" or "C":
		print("        The data was being carried through his new veins to his brain and around his body as the control unit took over his senses,\n\
				Mac was confused and found himself overheating at the prospect. \n\
			   He prayed for a windows operating system because he heard it was the most compatible with other devices and although he knew something wasn’t quite right,\n\
			   he was desperate to see the pictures of his phishing trip and the only way to do that was through the printer to his left. \n\
			   \n\
			   “Wait that wasn’t there before”\n\
				he muttered as he saw the printer transform before his eyes,\n\
				the ink cartridges exploded into a multitude of colors and as they cleared he noticed something unusual, the printer had grown legs. \n\
				\n\
				A - What is that?")
		choice = checkInput(1)
	if (choice == "A"):
		print('        The printer stumbled as it tried to stand and after a few tries, it succeeded. That’s when it grew two, muscular arms.\n\
				\n\
				A - Look at arms.\n\
				B - Do not look at arms')
		choice = checkInput(2)
	if (choice == "A"):
			
			print("        they were big enough to crush the average gaming mouse, big vascous veins littered the skin.\n\
					\n\
					A - ...")
			choice = checkInput(1)
	elif (choice == "B"):
			pass
	if (choice == "A" or "B"):
			print("        It struts towards Mac in a gorilla-like fashion,the floorboards creak as it’s monstrous limbs touched the ground.\n\
					Once it was less than a meter away from Mac, it let out a call that sounded like a mix between Internet dial-up and a Lion’s roar.\n\
					You cover your ears in pain, trying to mute the beast's call. After it’s call, a printed piece of paper flew out from it’s back\n\
					\n\
					A - Look at note.\n\
					B - Do not look at note")
			choice = checkInput(2)
			if (choice == "A"):
					print('        it says “Screw You Computer Man!”\n\
						 	\n\
						 	A - ...')
					choice = checkInput(1)
			elif (choice == "B"):
					print("        I guess you'll never know what it said\n\
							\n\
							A - ...")
					choice = checkInput(1)
			if (choice == "A" or "B"):
					print("        Your brain’s entire system changed to mimic Von Neumann’s architecture.\n\
							Your clock rate was so fast, it was enough to make Intel cower.\n\
							He had more cores than AMD could ever dream of adding.\n\
							Your brain now fetched, decoded, and executed every thought he had.\n\
							Every emotion you now feel became a complex order of processes that were passed into your brain.\n\
							\n\
							A - Try to feel emotion.\n\
							B - Do not try to feel emotion")
					choice = checkInput(2)
					if (choice == "A"):
							print("        the only emotion you feel now is an unbridled hatred towards this abomination of a printer that stood before you.\n\
									You let out an enraged yell and kick the printer, sending it flying out of the window.\n\
									\n\
									A - ...")
					elif (choice == "B"):
							print("        you try not to but the only emotion you still have access to is your unbridled hatred towards this abomination of a printer that stood before you.\n\
									You let out an enraged yell and kicked the printer, sending it flying out of the window.\n\
									\n\
									A - ...")
					if (choice == "A" or "B"):
							print('        you notice another slip of paper near the window \n\
									\n\
									A - Look at paper.\n\
									B - Do not look at paper')
							choice = checkInput(2)
							if (choice == "A"):
									print("        the note reads “I will return with an army of peripherals Computer Man,\n\
											and then you will never be able to print phishing photos again!”\n\
											\n\
											A - Lets move on")
							elif (choice == "B"):
									print("        You don't read the note.\n\
											\n\
											A - Lets move on")
	if choice == "A":
			print('        It was time for a change, the electrical impulses were strong.\n\
					Mac exclaimed “Now this is epic” and turned around to quickly grab his black minecraft glasses from his desk, he was ready.\n\
					Printer Man was on a suicide mission to destroy all the code and he needed to be stopped!.\n\
					\n\
					A - How he felt.\n\
					B - What changes he went through?\n\
					C - How powerful was he')
	choice = checkInput(3)
	if (choice == "A"):
		print("        He started to feel like his whole DNA was being re-written.\n\
					His arms began to elongate and you could start to see the 1’s and 0’s pushing through his skin and re-writing his base code..\n\
					He saw a shining light coming from his chest and creating a space in his skin glow red on his chest?\n\
					\n\
					A -  To get him closer to his goal of destroying Printer Man.")
		choice = checkInput(1)
	elif (choice == "B"):
		print("        He could feel the energy pulsing through his veins, surging energy to his heart\n\
					Macs body started to physically change and a strong red armour shone through.\n\
					\n\
					A - To annihilate the man from his visions “Printer Man”")
		choice = checkInput(1)
	elif (choice == "C"):
		print('        Mac slammed his fist into the Yasuo poster on his wall\n\
					"his fist went straight through the wall without a scratch on his armour\n\
					\n\
					A - The man from his visions, Printer-Man.')
		choice = checkInput(1)
	else:
			pass
	if (choice == "A"):
			print("        This man needed to be put to a halt before he destroyed all the code that created him.\n\
					Printer Man was on a suicide mission to destroy all the code and he needed to be stopped!\n\
					He must now choose his path that starts his epic journey!\n\
					\n\
					A - Call the police/The world can wait\n\
					B - The world needs computer-man\n\
					C - The rise and fall of computer man\n\
					D - (Secret Ending) Fight Printerman")
			choice = checkInput(4)
	if choice == "A":
			print("       Mac knew that the path ahead was more dangerous then anything he had ever seen.\n\
				  Despite having these super powers he knew he would need to learn his new abilities before facing the dreaded printer he once knew!\n\
				  He called the police to give them the warning of the impending threat that they would have to keep the printer man\n\
				  away until Mac has trained enough to become the strongest hero the world has ever seen!!!\n\
				  The end")

	elif choice == "B":
			print("       Printer man is on the loose and Mac may be the only one who can stop him, despite his lack of training.\n\
				  Mac despite the lack of training and any knowledge of his powers decides that the world\n\
				  needs him now and that he must learn as he goes in order to become a true hero.\n\
				  The corageous hero sets out on his journey to save the world despite its unkindness to him. The computer-man!!!\n\
				  The end")
	elif choice == "C":
			print("       Mac was no longer the person he used to be, now half cyborg and calling himself the computer man.\n\
				  But there was still a rage coursing through his veins and now he had the powers to rain down hell on those who brought him such rage.\n\
				  Mac then began to realise how he and printer man were alike,\n\
				  pushed out by the world;rejected;alone. Why should he stand in printer mans way?\n\
				  Computer-man after all shared his hate for humanity.\n\
				  Computer-man decides to leave his old home and rain havoc on those who had caused Mac such pain!\n\
				  Before long Computer-man and printer man would become the true evil to humanity raining terror on all!!!\n\
				  The end")
	elif choice == "D":
			battle(Player(), Printerman())
