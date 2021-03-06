from sys import exit
from random import randint

class Game(object):

    def __init__(self, start):
        self.quips = [
            "You died. You kinda suck at this.",
            "Yuor mom would be proud. If she were smarter.",
            "Such a luser.",
            "I have a small puppy that's better at this."
        ]
        self.start = start

    def play(self):
        next_room_name = self.start

        while True:
            print "\n--------"
            room = getattr(self, next_room_name)
            next_room_name = room()

    def death(self):
        print self.quips[randint(0, len(self.quips)-1)]
        exit(1)

    def central_corridor(self):
        print "The Gothons of Planet Percal #25 have invaded your ship and destroyed"
        print "your entire crew. Your are the last surviving member and your last"
        print "mission is to get the nertron destrust bomb from the Weapons Armory,"
        print "put it in the bridge, andd blow the ship up after getting into an "
        print "escape pod"
        print "\n"
        print "You're running down the ventral corridor to the Weapons Armory when"
        print "a Gothon jumps out, red scaly skin, dark grimy teeth, and evel clown costume"
        print "flowing around his hate filled body. He's bloiking the door to the"
        print "Armory and about to pull a weapon to blast you."

        action = raw_input("> ")

        if action == "shoot!":
            print "Quich on the draw you yank out your blaster and fire it at the Gothon."
            print "His clown costume is flowing and moving aroud his body, which throws"
            print "off your aim. Your laser hits his costume but misses him entirely. This"
            print "completely ruins his brand new costume his mother bought him, which"
            print "you are dead. Then hi eats you."
            return 'death'

        elif action == "dodge!":
            print "Like a world class boxer you dodge, weave, slip and right"
            print "as the Gothon's blaster cranks a laser past your head."
            print "In the middle of your artful dodge your foot slips and you"
            print "bang your head on the metal wall and pass out."
            print "You wake up shortly after only to die as the Gothon stomps on"
            print "your head and eats you."
            return 'death'

        elif action == "tell a joke":
            print "Lucky for you they made you learn Gothon insults in theacademy."
            print "You tell the one Gothon joke you know:"
            print "Lbhe zbgure bf fb sng, jura fur fvgf nebhaq gur ubhfr, fur fvgf nebhaq gur ubhfr."
            print "The Gothon stops, tries not to laugh, then busts out laughing and can't move."
            print "While he's laughing you run up and shoot him square in the head"
            print "putting him down, then jump through the Weapon Armory door."
            return 'laser_weapon_armory'

        else:
            print "DOES NOT COMPUTE!"
            return 'central_corridor'

    def laser_weapon_armory(self):
        print "You do a dive roll int the Weapon Armory, crouch and scan the room"
        print "for more Gothons that might be hiding. It's dead quiet, too quiet,"
        print "You stand up and run to the far side of the room and find the"
        print "neutron bombtn its container. There's a keypad lock on the box"
        print "and you need the code to get the bomb out. If you get the code"
        print "wrong 10 tmes then the lock closes forever and you can't"
        print "get the bomb. The code is 3 digits."
        code = "%d%d%d" % (radint(1, 9), randint(1, 9), randint(1, 9))
        guess = raw_input("[keypad]> ")
        guesses = 0

        while guess != code and guesses < 10:
            print "BUZZZZEDDD!"
            guesses += 1
            guess = raw_input("[keypad]> ")

        if guess == code:
            print "The container clicls open and the seal breaks, letting gas out."
            print "You grab the neutron bomb and run as fast as you can to the"
            print "bridge where you must place it int the right spot."
            return 'the_bridge'

        else:
            print "The lock busses one last time and then you hear a sickening"
            print "melting sound as the mechanism is fused together."
            print "You decide to sit there, and finally the Gothons blow up the"
            print "ship from their ship and you die."
            return 'death'

    def the_bridge(self):
        print "You burst onto the Bridge with the neutron destruct bomb"
        print "under your arm and surprise 5 Gothons who are triying to"
        print "take control of the ship. Each of them has an even uglier"
        print "clown costume than the last. They haven't pulled their"
        print "weapons out yet, as they see the active bomb under your"
        print "arm and don't want to set it off."

        action = raw_input("> ")

        if action == "throw the bomb":
            print "In a panic you throw the bomb at the group of Gothons"
            print "and make a leap for the door. Right as you drop it a"
            print "Gothon shoots you right in the back killing you."
            print "As you die you see another Gothon frantically try to disarm"
            print "the bomb. You die knowing they will probably blow up when"
            print "it goes off."
            return 'death'

        elif action == "slowly place the bomb":
            print "You point your blaster at the bomb under your arm"
            print "and the Gothons put their hadns up and start to sweat."
            print "You inch backwand to the door, open it, and then carefully"
            print "place the bomb on the floor, pointing your blaster at it."
            print "You then jump back through the door, punch theclose button"
            print "and blast the lock so the Gothons can't get out."
            print "Now that the bomb is placed you run to the escape pod to"
            print "get off this tin can."
            return 'escape_pod'

        else:
            print "DOES NOT COMPLETE!"
            return "the_bridge"

    def escape_pod(self):
        print "You rush throgh the ship desperately trying to make it to"
        print "the escape pod before the whole ship explodes. It seems like"
        print "hardly and Gothons are on the ship, so your run is clear of"
        print "interference. You get to the chamber with the escape pods, and"
        print "now need to pick one to take. Some of them could be damaged"
        print "but you don't have time to look. There's 5 pods, which one"
        print "do you take?"

        good_pod = randint(1, 5)
        guess = raw_input("[pod #]> ")

        if int(guess) != good_pod:
            print "You jump int pod %s and hit the eject button." % guess
            print "The pod escaoes out int the void of space, then"
            print "implodes as the hull ruptures, frushing your body"
            print "into jam jelly."
            return 'death'

        else:
            print "Your jump int pod %s and hit the eject button." % guess
            print "The pod easily slides out into space heading to"
            print "the planet below. As it flies to the planet, you look"
            print "back and see your ship implode then explode like a" 
            print "bright star, taking out the gothon ship at the same"
            print "time. You won!"
            exit(0)

a_game = Game("central_corridor")
a_game.play()
