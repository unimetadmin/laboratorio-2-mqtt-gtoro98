import sys
import paho.mqtt.client
import json
import psycopg2
from datetime import datetime
from psycopg2 import Error


def on_connect(client, userdata, flags, rc):
	print('connected (%s)' % client._client_id)
	client.subscribe(topic='casa/cocina/#', qos=2)

def on_message(client, userdata, message):
	print('------------------------------')
	print('topic: %s' % message.topic)
	time = datetime.now()
	topic = message.topic
	if topic == 'casa/cocina/nevera':
		if "hielo" in json.loads(message.payload):
			print('payload: %s' % json.loads(message.payload)["hielo"])
			sql_query = """ INSERT INTO "hielonevera" (hielo, fecha) VALUES (%s, %s)"""
			item_tuple = (json.loads(message.payload)["hielo"], time, )
			cursor.execute(sql_query, item_tuple)
			connection.commit()
		else:
			print('payload: %s' % json.loads(message.payload)["temp"])
			sql_query = """ INSERT INTO "tempnevera" (temp, fecha) VALUES (%s, %s)"""
			item_tuple = (json.loads(message.payload)["temp"], time, )
			cursor.execute(sql_query, item_tuple)
			connection.commit()
	else:
		sql_query = """ INSERT INTO "olla" (temp, hirviendo, fecha) VALUES (%s, %s, %s)"""
		item_tuple = (json.loads(message.payload)["temp"], json.loads(message.payload)["hirviendo"], time, )
		cursor.execute(sql_query, item_tuple)
		connection.commit()
	print('qos: %d' % message.qos)

def main():
	client = paho.mqtt.client.Client(client_id='alejandro-subs', clean_session=False)
	client.on_connect = on_connect
	client.on_message = on_message
	client.connect(host='127.0.0.1', port=1883)
	client.loop_forever()


try:
	connection = psycopg2.connect(user="ufwkwpgo",
								password="JC-EWjqXDxpWrUpJ7j3qIcTnmZiFRpKW",
								host="queenie.db.elephantsql.com",
								database="ufwkwpgo")
	cursor = connection.cursor()

	print("PostgreSQL server information")
	print(connection.get_dsn_parameters(), "\n")
	# Executing a SQL query
	cursor.execute("SELECT version();")
	# Fetch result
	record = cursor.fetchone()
	print("You are connected to - ", record, "\n")

	if __name__ == '__main__':
		main()


except (Exception, Error) as error:
	print("Error while connecting to PostgreSQL", error)
finally:
	if connection:
		cursor.close()
		connection.close()
		print("PostgreSQL connection is closed")
		sys.exit(0)