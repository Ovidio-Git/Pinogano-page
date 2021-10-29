def do_connect():
	import network
	sta_if = network.WLAN(network.STA_IF)
	if not sta_if.isconnected():
		print('Connecting to network :D ...')
		sta_if.active(True)
		sta_if.connect(':D','2959OhS434')
		while not sta_if.isconnected():
			sta_if.connect(':D','2959OhS434')
			print('Reconnecting to :D ...')
	print('Connectiong success: network config', sta_if.ifconfig())


if __name__ == '__main__':
	do_connect()
