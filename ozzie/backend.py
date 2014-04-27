class OzzieFirebase:
	def __init__(self, config):
		from firebase import firebase
		auth= firebase.FirebaseAuthentication(config.get("Firebase", "Secret"), config.get("Firebase", "Email"))
		fb = firebase.FirebaseApplication(config.get("Firebase", "URL"), auth)
		self.firebase = fb
		self.config = config

	def pollServer(self, status):
		new_user = "test"
		self.firebase.post('/', status)


class OzzieServer:
	def __init__(self, config):
		pass