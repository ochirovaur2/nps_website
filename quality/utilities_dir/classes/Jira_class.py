import psycopg2






class Jira:
	"""docstring for Jira"""
	def __init__(self, passwords):
		self.passwords = passwords

	def connect_to_db(self):

		self.con = psycopg2.connect(database=self.passwords['database'], 
								user=self.passwords['user'], 
								password=self.passwords['password'], 
								host=self.passwords['host'], 
								port=self.passwords['port'])
		self.cursor =  self.con.cursor()
		
	def save_comment(self, rating, comment, ticket_id, user_id, resolution_time):
		
		
		self.connect_to_db()
		

		
		# cursor.execute(f'''
		# 	INSERT INTO custom_quality_rating (
		# 	"ticket_id", "rating" , "comment", "user" ) VALUES ('{ticket_id}', '{rating}' ,'{comment}', '{user_id}')
		# 	''')
		self.cursor.execute('''INSERT INTO custom_quality_rating (ticket_id, rating , comment, "user", "resolution_time") VALUES (%(ticket_id)s, %(rating)s,%(comment)s, %(user)s, %(resolution_time)s)''', {'ticket_id': ticket_id, 'rating': rating, 'comment' : comment, 'user': user_id, 'resolution_time': resolution_time})

		self.con.commit()	



		self.cursor.close()
		print(self.cursor.statusmessage)
		self.con.close()


	def check_resolution_uniqueness(self, ticket_id, user_id, resolution_time):
		
		
		self.connect_to_db()
		

		print(user_id)
		print(ticket_id)
		print(resolution_time)

		self.cursor.execute('''SELECT * FROM custom_quality_rating WHERE "ticket_id" = %(ticket_id)s AND "user" = %(user)s AND "resolution_time" = %(resolution_time)s ''', {'ticket_id': ticket_id,  'user': user_id, 'resolution_time': resolution_time})

		print(self.cursor.statusmessage)


		data = self.cursor.fetchall()


		self.cursor.close()
		
		self.con.close()

		
		if len(data)> 0:
			return 302
		else:
			return 201

	def get_sd_number(self, ticket_id):

		self.connect_to_db()


		self.cursor.execute('''
			SELECT issuenum FROM jiraissue WHERE id = %(ticket_id)s LIMIT 1
			''', {'ticket_id': ticket_id})


		data = self.cursor.fetchall()

		if len(data) > 0:

			

			return f'SD-{int(data[0][0])}'


		else:
			return None



		self.cursor.close()
		print(self.cursor.statusmessage)
		self.con.close()


	





    