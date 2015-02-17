__author__ = 'teohoch'

import random
import time
from ALMAEventSender import ALMAEventSender

STE = [
	['AOS', 32],
	['AOS', 64],
	['TFENG', 32],
	['TFINT', 32],
	['TFOHG', 32],
	['TFSD', 32],
]
Keys = ['ERROR', 'EVENT','LOG']

Posible_Strings = [
	"Nam finibus mi enim, sed.",
    "Quisque varius mi libero, eget.",
    "Aliquam id est in enim consequat accumsan egestas eu orci.",
	"Fusce vel nisl faucibus ligula gravida dictum nec eget eros.",
	"Integer congue massa vel sollicitudin hendrerit.",
	"Aenean faucibus nulla feugiat lacus viverra, nec cursus dui fringilla.",
	"Etiam ut tellus a odio vehicula feugiat quis porttitor nulla.",
	"Donec scelerisque massa nec feugiat ultricies.",
	"Proin viverra justo vulputate lectus eleifend, quis vulputate nisl efficitur.",
	"Aenean nec risus porta, maximus mauris ac, elementum erat.",
	"Nulla quis libero vulputate, imperdiet nulla nec, vestibulum ligula.",
	"Nulla et erat tempor, tincidunt risus et, rutrum leo.",
	"Vivamus cursus justo eu sem vehicula aliquam.",
	"Nullam sed ligula sed nibh tempus sollicitudin sit amet non orci.",
	"Donec non lacus viverra, tincidunt erat a, viverra nisl.",
	"Aliquam nec leo placerat, lobortis lacus non, congue nunc.",
	"Maecenas vitae metus porttitor, tempus libero ut, tempor nulla.",
	"Curabitur in lacus sed erat aliquet egestas.",
	"Praesent finibus quam eu nunc blandit pellentesque.",
	"Aenean eget diam quis felis pharetra gravida et sit amet velit.",
	"Suspendisse sagittis ligula a venenatis hendrerit."
]

def generate_value():
	decider =  random.randint(1,3)
	if decider == 1:
		value = int(random.random() * 10000)
		label = 'value_int'
	elif decider == 2:
		value = random.random()
		label = 'value_float'
	elif decider == 3:
		value = random.choice(Posible_Strings)
		label = 'value_string'

	return [label, value]


def generate_message():
	message = {}

	ste = random.choice(STE)

	is_release_required = bool(random.getrandbits(1))
	message['environment'] = ste[0]
	message['architecture'] = ste[1]

	if is_release_required:
		message['release'] = 'required'
	else:
		message['release'] = 'ALMA-10_6_0-B'



	# ### Add Key ###

	message['key'] = key = random.choice(Keys)

	# ### Add Values ###
	n_values = random.randint(0,3)

	for i in range(n_values):
		val = generate_value()
		message[val[0]] = val[1]



	return message

if __name__ == "__main__":

	rabbit_config = {'Host'         :   'localhost',
	                 'User'         :   'alma',
	                 'Password'     :   'Carl.Sagan',
	                 'Routing_key'  :   'AlmaEvent',
	                 'Exchange'     :   'alma_events'}

	a = ALMAEventSender(rabbit_config)
	for i in range(0,49):
		print '['+str(i) +']\t ' + str(a.sendEvent(generate_message()))



