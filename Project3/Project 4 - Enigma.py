import math


class Rotor:

    def __init__(self):

        self.rotor_starting_position = 0

    def shift_start_position(self, seq, n):
        return seq[n:] + seq[:n]

    def shift_rotor(self, seq, n, rn, numb):
        if rn == 1:
            n = -n % len(seq)

        elif rn == 2:
            n = - math.trunc(n / 25) % len(seq)

        elif rn == 3:
            n = - math.trunc(n / 675) % len(seq)

        return seq[n:] + seq[:n]

    def rotor_revolution(self, seq):
        rotor_revolution = [''] * 26
        for i in range(26):
            rotor_revolution[seq[i]] = i

        return rotor_revolution

    def initiate_revolution(self, seq, rev, numb, rn):
        number = []
        if rev == 0:
            for i in range(len(numb)):
                rotation = Rotor.shift_rotor(self, seq, i, rn, numb)
                number.append(rotation[numb[i]])

        elif rev == 1:
            for i in range(len(numb)):
                rotation = Rotor.shift_rotor(self, seq, i, rn, numb)
                sequence_of_revolution = Rotor.rotor_revolution(self, rotation)
                number.append(sequence_of_revolution[numb[i]])

        return number


class Reflector:

    def __init__(self):
        self.reflector = [24, 17, 20, 7, 16, 18, 11, 3, 15, 23, 13, 6, 14, 10, 12, 8, 4, 1, 5, 25, 2, 22, 21, 9, 0, 19]

    def reflector_and_plugboard(self, list, step):
        ref = []
        for n in step:
            ref.append(list[n])

        return ref


class Plugboard:

    def __init__(self):
        self.plugboard_dude = [0, 24, 2, 3, 4, 5, 22, 7, 8, 9, 10, 12, 11, 16, 14, 15, 13, 17, 18, 19, 20, 21, 6, 23, 1, 25]

    def change_plugboard_settings(self):
        answer = input("Although it is not encouraged, would you like to change the existing plugboard settings?\n")

        if answer == "yes" or answer == 'YES':

            user_input_plugboard = input("Enter pair like [AB CD EF GH IJ KL MN OP QR ST] without any spaces:\n")
            user_input_plugboard = user_input_plugboard.upper()
            user_changed_plugboard = []
            for sign in user_input_plugboard:
                letter = ord(sign) - 65
                user_changed_plugboard.append(letter)
            self.plugboard_dude = user_changed_plugboard

    def reflector_and_plugboard(self, list, step):
        ref = []
        for n in step:
            ref.append(list[n])

        return ref


instance_plugboard = Plugboard()
instance_plugboard.change_plugboard_settings()

message = input("Enter a message to encrypt/decrypt:\n")
message = message.upper()

numb = []

for sign in message:
    number = ord(sign) - 65
    numb.append(number)

rotor1 = Rotor()
rotor1.rotor_dude = [4, 10, 12, 5, 11, 6, 3, 16, 21, 25, 13, 19, 14, 22, 24, 7, 23, 20, 18, 15, 0, 8, 1, 17, 2, 9]
rotor1_start_position = rotor1.rotor_starting_position = 1
rotor1_movement = rotor1.shift_start_position(rotor1.rotor_dude, rotor1_start_position)

rotor2 = Rotor()
rotor2.rotor_dude = [0, 9, 3, 10, 18, 8, 17, 20, 23, 1, 11, 7, 22, 19, 12, 2, 16, 6, 25, 13, 15, 24, 5, 21, 14, 4]
rotor2_start_position = rotor2.rotor_starting_position = 2
rotor2_movement = rotor2.shift_start_position(rotor2.rotor_dude, rotor2_start_position)

rotor3 = Rotor()
rotor3.rotor_dude = [1, 3, 5, 7, 9, 11, 2, 15, 17, 19, 23, 21, 25, 13, 24, 4, 8, 22, 6, 0, 10, 12, 20, 18, 16, 14]
rotor3_start_position = rotor3.rotor_starting_position = 3
rotor3_movement = rotor3.shift_start_position(rotor3.rotor_dude, rotor3_start_position)

instance_reflector = Reflector()
instance_reflector.reflector = [24, 17, 20, 7, 16, 18, 11, 3, 15, 23, 13, 6, 14, 10, 12, 8, 4, 1, 5, 25, 2, 22, 21, 9, 0, 19]


class Enigma:

    step1 = instance_plugboard.reflector_and_plugboard(instance_plugboard.plugboard_dude, numb)
    step2 = rotor1.initiate_revolution(rotor1_movement, 0, step1, 1)
    step3 = rotor2.initiate_revolution(rotor2_movement, 0, step2, 2)
    step4 = rotor3.initiate_revolution(rotor3_movement, 0, step3, 3)
    step5 = instance_reflector.reflector_and_plugboard(instance_reflector.reflector, step4)
    step6 = rotor3.initiate_revolution(rotor3_movement, 1, step5, 3)
    step7 = rotor2.initiate_revolution(rotor2_movement, 1, step6, 2)
    step8 = rotor1.initiate_revolution(rotor1_movement, 1, step7, 1)
    step9 = instance_plugboard.reflector_and_plugboard(instance_plugboard.plugboard_dude, step8)


enigma = Enigma()

new_message = []
for i in range(len(enigma.step9)):
    word = chr(enigma.step9[i]+65)
    new_message.append(word)

print(''.join(new_message))