from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_sdk import Action
from rasa_sdk.events import SlotSet

import json
from flask_mail_send import send_email
import zomatopy
import pandas as pd

# Zomato Config start

config={"user_key":""} #Enter Zomato token
zomato = zomatopy.initialize_app(config)
# Zomato Config end

# Email Config start
def Config():
	gmail_user = '' # Gmail Username
	gmail_pwd = '' #APP Password
	gmail_config = (gmail_user, gmail_pwd)
	return gmail_config
# Email Config end


city_dict = ['Ahmedabad','Bangalore','Chennai','Delhi','Hyderabad','Kolkata','Mumbai','Pune','Agra','Ajmer',
'Aligarh','Allahabad','Amravati','Amritsar','Asansol','Aurangabad','Bareilly','Belgaum','Bhavnagar','Bhiwandi',
'Bhopal','Bhubaneswar','Bikaner','Bokaro Steel City','Chandigarh','Coimbatore','Cuttack','Dehradun','Dhanbad',
'Durg-Bhilai Nagar','Durgapur','Erode','Faridabad','Firozabad','Ghaziabad','Gorakhpur','Gulbarga','Guntur',
'Gurgaon','Guwahati‚ Gwalior','Hubli-Dharwad','Indore','Jabalpur','Jaipur','Jalandhar','Jammu','Jamnagar','Jamshedpur',
'Jhansi','Jodhpur','Kannur','Kanpur','Kakinada','Kochi','Kottayam','Kolhapur','Kollam','Kota','Kozhikode','Kurnool',
'Lucknow','Ludhiana','Madurai','Malappuram','Mathura','Goa','Mangalore','Meerut','Moradabad','Mysore','Nagpur','Nanded','Nashik',
'Nellore','Noida','Palakkad','Patna','Pondicherry','Raipur','Rajkot','Rajahmundry','Ranchi','Rourkela','Salem','Sangli','Siliguri',
'Solapur','Srinagar','Sultanpur','Surat','Thiruvananthapuram','Thrissur','Tiruchirappalli','Tirunelveli','Tiruppur','Ujjain','Vijayapura',
'Vadodara','Varanasi','Vasai-Virar City','Vijayawada','Visakhapatnam','Warangal']

city_dict = [x.lower() for x in city_dict]
cuisines_dict={'american': 1,'chinese': 25, 'north indian': 50, 'italian': 55, 'mexican': 73, 'south indian': 85, 'thai': 95}

class ActionSearchRestaurants(Action):
	def name(self):
		return 'action_restaurant'

	def run(self, dispatcher, tracker, domain):
		loc = tracker.get_slot('location')
		cuisine = tracker.get_slot('cuisine')
		price = tracker.get_slot('price')

		global restaurants
		print(loc, cuisine, price)
		restaurants = zomatorRestoSearch(loc, cuisine, price)
		top5 = restaurants.head(5)

		# top 5 results to display
		if len(top5)>0:
			response = 'Showing you top results:' + "\n"
			for index, row in top5.iterrows():
				response = response + str(row["restaurant_name"]) + ' in ' + row['restaurant_address'] + ' has been rated ' + row['restaurant_rating'] +"\n"
				# response = response + "\nShould i mail you the details"
			dispatcher.utter_message(str(response))
			return [SlotSet('result_found',True)]
		else:
			response = 'No restaurants found'
			dispatcher.utter_message(str(response))
			return [SlotSet('result_found',False)]


class SendMail(Action):
	def name(self):
		return 'email_restaurant_details'

	def run(self, dispatcher, tracker, domain):
		recipient = tracker.get_slot('email')

		top10 = restaurants.head(10)
		print("Sending email to {}".format(recipient))
		send_email(recipient, top10)

		dispatcher.utter_message("Sent. Bon Appetit!")


class Check_location(Action):
	def name(self):
		return 'action_check_location'

	def run(self, dispatcher, tracker, domain):
		loc = tracker.get_slot('location')
		print("Check location",loc)
		check= {'location_f' : 'notfound', 'location_new' : None}
		config={"user_key":"f4924dc9ad672ee8c4f8c84743301af5"}
		zomato = zomatopy.initialize_app(config)
		location_detail=zomato.get_location(loc, 1)
		location_json = json.loads(location_detail)
		print(location_json)
		if 'location_suggestions' in location_json:		
			location_results = len(location_json['location_suggestions'])

			if location_results ==0:
				check= {'location_f' : 'notfound', 'location_new' : None}
			elif loc.lower() not in city_dict:
				check= {'location_f' : 'tier3', 'location_new' : None}
			else:
				check= {'location_f' : 'found', 'location_new' : loc}
		else:
			check= {'location_f' : 'notfound', 'location_new' : None}


		return [SlotSet('location',check['location_new']), SlotSet('location_found',check['location_f'])]

class Check_cuisine(Action):
	def name(self):
		return 'action_check_cuisine'

	def run(self, dispatcher, tracker, domain):
		cuisine = tracker.get_slot('cuisine')
		print("Check Cusine",cuisine)
		if key not in cuisines_dict:
			return [SlotSet('cuisine_not_found',True)]



def zomatorRestoSearch(loc,cuisine,price):
	location_detail=zomato.get_location(loc, 1)
	location_json = json.loads(location_detail)
	location_results = len(location_json['location_suggestions'])
	lat=location_json["location_suggestions"][0]["latitude"]
	lon=location_json["location_suggestions"][0]["longitude"]
	city_id=location_json["location_suggestions"][0]["city_id"]


	list1 = [0,20,40,60,80]
	d = []
	df = pd.DataFrame()
	results = zomato.restaurant_search("", lat, lon, str(cuisines_dict.get(cuisine)))
	d1 = json.loads(results)
	# print("d1",d1)
	d = d1['restaurants']
	df1 = pd.DataFrame([{'restaurant_name': x['restaurant']['name'], 'restaurant_rating': x['restaurant']['user_rating']['aggregate_rating'],
			'restaurant_address': x['restaurant']['location']['address'],'budget_for2people': x['restaurant']['average_cost_for_two'],
			'restaurant_photo': x['restaurant']['featured_image'], 'restaurant_url': x['restaurant']['url'] } for x in d])
	df = df.append(df1)

	def budget_group(row):
		if row['budget_for2people'] <300 :
			return 'lesser than 300'
		elif 300 <= row['budget_for2people'] <700 :
			return 'between 300 to 700'
		else:
			return 'more than 700'

	df['budget'] = df.apply(lambda row: budget_group (row),axis=1)
		#sorting by review & filter by budget
	restaurant_df = df[(df.budget == price)]
	restaurant_df = restaurant_df.sort_values(['restaurant_rating'], ascending=0)

	return restaurant_df
