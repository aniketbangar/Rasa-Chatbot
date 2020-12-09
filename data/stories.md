## complete path 1
* greet
    - utter_greet
* restaurant_search{"location": "jaipur"}
    - slot{"location": "jaipur"}
    - action_check_location
    - slot{"location": "jaipur"}
    - slot{"location_found": "found"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - utter_ask_price
* restaurant_search{"price": "between 300 to 700"}
    - slot{"price": "between 300 to 700"}
    - action_restaurant
    - slot{"result_found": true}
    - utter_should_email
* deny
    - utter_final_bye
    - action_restart
    - action_listen

## complete path 2
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - action_check_location
    - slot{"location": "bangalore"}
    - slot{"location_found": "found"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - utter_ask_price
* restaurant_search{"price": "more than 700"}
    - slot{"price": "more than 700"}
    - action_restaurant
    - slot{"result_found": true}
    - utter_should_email
* affirm
    - utter_ask_mail
* ask_email{"email": "bangaraniket@gmail.com"}
    - slot{"email": "bangaraniket@gmail.com"}
    - email_restaurant_details
    - action_restart

* greet
    - utter_greet
* restaurant_search{"location": "Rishikesh"}
    - slot{"location": "Rishikesh"}
    - action_check_location
    - slot{"location": null}
    - slot{"location_found": "tier3"}
    - utter_foodie_not_working
* restaurant_search{"location": "Allahabad"}
    - slot{"location": "Allahabad"}
    - action_check_location
    - slot{"location": "Allahabad"}
    - slot{"location_found": "found"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* restaurant_search{"price": "more than 700"}
    - slot{"price": "more than 700"}
    - action_restaurant
    - slot{"result_found": true}
    - utter_should_email
* ask_email{"email": "bangaraniket@gmail.com"}
    - slot{"email": "bangaraniket@gmail.com"}
    - email_restaurant_details
    - action_restart

* greet
    - utter_greet
* restaurant_search{"location": "kolkata"}
    - slot{"location": "kolkata"}
    - action_check_location
    - slot{"location": "kolkata"}
    - slot{"location_found": "found"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - utter_ask_price
* restaurant_search{"price": "more than 700"}
    - slot{"price": "more than 700"}
    - action_restaurant
    - slot{"result_found": true}
    - utter_should_email
* deny
    - utter_final_bye
    - action_restart
    - action_listen

* restaurant_search{"location": "karnataka"}
    - slot{"location": "karnataka"}

* restaurant_search{"cuisine": "chinese", "location": "mumbai"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "mumbai"}
    - action_check_location
    - slot{"location": "mumbai"}
    - slot{"location_found": "found"}
    - utter_ask_price
* restaurant_search{"price": "more than 700"}
    - slot{"price": "more than 700"}
    - action_restaurant
    - slot{"result_found": true}
    - utter_should_email
* affirm
    - utter_ask_mail
* ask_email{"email": "jddk.2jmd@kdl.co.in"}
    - slot{"email": "jddk.2jmd@kdl.co.in"}
    - email_restaurant_details
    - action_restart

* restaurant_search{"cuisine": "american", "location": "chennai"}
    - slot{"cuisine": "american"}
    - slot{"location": "chennai"}
    - action_check_location
    - slot{"location": "chennai"}
    - slot{"location_found": "found"}
    - utter_ask_price
* restaurant_search{"price": "between 300 to 700"}
    - slot{"price": "between 300 to 700"}
    - action_restaurant
    - slot{"result_found": true}
    - utter_should_email
* ask_email{"email": "bangaraniket@gmail.com"}
    - slot{"email": "bangaraniket@gmail.com"}
    - email_restaurant_details
    - action_restart

* restaurant_search{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - utter_ask_location
* restaurant_search{"location": "kddkdmlakdmmkda"}
    - slot{"location": "kddkdmlakdmmkda"}
    - action_check_location
    - slot{"location": null}
    - slot{"location_found": "notfound"}
    - utter_location_notfound
* restaurant_search{"location": "karnataka"}
    - slot{"location": "karnataka"}
    - action_check_location
    - slot{"location": null}
    - slot{"location_found": "tier3"}
    - action_check_location

* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_location
* restaurant_search
    - action_check_location

* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}

* restaurant_search{"cuisine": "chinese", "location": "mubma"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "mubma"}
    - action_check_location
    - slot{"location": null}
    - slot{"location_found": "tier3"}
    - utter_foodie_not_working
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location": "delhi"}
    - slot{"location_found": "found"}
    - utter_ask_price
* restaurant_search{"price": "lesser than 300"}
    - slot{"price": "lesser than 300"}
    - action_restaurant
    - slot{"result_found": false}
    - action_restart
* restaurant_search{"cuisine": "south indian", "location": "delhi"}
    - slot{"cuisine": "south indian"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location": "delhi"}
    - slot{"location_found": "found"}
    - utter_ask_price
* restaurant_search{"price": "more than 700"}
    - slot{"price": "more than 700"}
    - action_restaurant
    - slot{"result_found": true}
    - utter_should_email
* affirm
    - utter_ask_mail
* ask_email{"email": "bangaraniket@gmail.com"}
    - slot{"email": "bangaraniket@gmail.com"}
    - email_restaurant_details
    - action_restart

* restaurant_search{"cuisine": "north indian", "location": "kolkata"}
    - slot{"cuisine": "north indian"}
    - slot{"location": "kolkata"}
    - action_check_location
    - slot{"location": "kolkata"}
    - slot{"location_found": "found"}
    - utter_ask_price
* restaurant_search{"price": "more than 700"}
    - slot{"price": "more than 700"}
    - action_restaurant
    - slot{"result_found": true}
    - utter_should_email
* deny
    - utter_final_bye
    - action_restart
    - action_listen

* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - action_check_location
    - slot{"location": "mumbai"}
    - slot{"location_found": "found"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* restaurant_search{"price": "more than 700"}
    - slot{"price": "more than 700"}
    - action_restaurant
    - slot{"result_found": true}
    - utter_should_email
* affirm
    - utter_ask_mail
* ask_email{"email": "aiana.goyal@upgrad.com"}
    - slot{"email": "aiana.goyal@upgrad.com"}
    - email_restaurant_details
    - action_restart

* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location": "delhi"}
    - slot{"location_found": "found"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* restaurant_search{"price": "more than 700"}
    - slot{"price": "more than 700"}
    - action_restaurant
    - slot{"result_found": true}
    - utter_should_email
* deny
    - utter_final_bye
    - action_restart
    - action_listen


* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "mubaim"}
    - slot{"location": "mubaim"}
    - action_check_location
    - slot{"location": null}
    - slot{"location_found": "notfound"}
    - utter_location_notfound
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - action_check_location
    - slot{"location": "mumbai"}
    - slot{"location_found": "found"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - utter_ask_price
* restaurant_search{"price": "between 300 to 700"}
    - slot{"price": "between 300 to 700"}
    - action_restaurant
    - slot{"result_found": true}
    - utter_should_email
* affirm
    - utter_ask_mail
* ask_email{"email": "bangaraniket@gmail.com"}
    - slot{"email": "bangaraniket@gmail.com"}
    - email_restaurant_details
    - action_restart

* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "haridwar"}
    - slot{"location": "haridwar"}
    - action_check_location
    - slot{"location": null}
    - slot{"location_found": "tier3"}
    - utter_foodie_not_working
* restaurant_search{"location": "allahabad"}
    - slot{"location": "allahabad"}
    - action_check_location
    - slot{"location": "allahabad"}
    - slot{"location_found": "found"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* restaurant_search{"price": "more than 700"}
    - slot{"price": "more than 700"}
    - action_restaurant
    - slot{"result_found": true}
    - utter_should_email
* deny
    - utter_final_bye
    - action_restart
    - action_listen

* greet
    - utter_greet
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location": "delhi"}
    - slot{"location_found": "found"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* restaurant_search{"price": "lesser than 300"}
    - slot{"price": "lesser than 300"}
    - action_restaurant
    - slot{"result_found": true}
    - utter_should_email
* affirm
    - utter_ask_mail
* ask_email{"email": "bangaraniket@gmail.com"}
    - slot{"email": "bangaraniket@gmail.com"}
    - email_restaurant_details
    - action_restart
	
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "pune"}
    - slot{"location": "pune"}
    - action_check_location
    - slot{"location": "pune"}
    - slot{"location_found": "found"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - utter_ask_price
* restaurant_search{"price": "more than 700"}
    - slot{"price": "more than 700"}
    - action_restaurant
    - slot{"result_found": true}
    - utter_should_email
* deny
    - utter_final_bye
    - action_restart
    - action_listen
	
* greet
    - utter_greet
* restaurant_search{"location": "manali"}
    - slot{"location": "manali"}
    - action_check_location
    - slot{"location": null}
    - slot{"location_found": "tier3"}
    - utter_foodie_not_working
* restaurant_search{"location": "srinagar"}
    - slot{"location": "srinagar"}
    - action_check_location
    - slot{"location": "srinagar"}
    - slot{"location_found": "found"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - utter_ask_price
* restaurant_search{"price": "lesser than 300"}
    - slot{"price": "lesser than 300"}
    - action_restaurant
    - slot{"result_found": true}
    - utter_should_email
* ask_email{"email": "aiana.goyal@upgrad.com"}
    - slot{"email": "aiana.goyal@upgrad.com"}
    - email_restaurant_details
    - action_restart

* goodbye
    - utter_goodbye
    - action_restart

* greet
    - utter_greet
* restaurant_search{"location": "manali"}
    - slot{"location": "manali"}
    - action_check_location
    - slot{"location": null}
    - slot{"location_found": "tier3"}
    - utter_foodie_not_working
* restaurant_search{"location": "srinagar"}
    - slot{"location": "srinagar"}
    - action_check_location
    - slot{"location": "srinagar"}
    - slot{"location_found": "found"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - utter_ask_price
* restaurant_search{"price": "lesser than 300"}
    - slot{"price": "lesser than 300"}
    - action_restaurant
    - slot{"result_found": false}
    - action_restart

* greet
    - utter_greet
* restaurant_search{"location": "pune"}
    - slot{"location": "pune"}
    - action_check_location
    - slot{"location": "pune"}
    - slot{"location_found": "found"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - utter_ask_price
* restaurant_search{"price": "more than 700"}
    - slot{"price": "more than 700"}
    - action_restaurant
    - slot{"result_found": true}
    - utter_should_email
* deny
    - utter_final_bye
    - action_restart
	
* greet
    - utter_greet
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - utter_ask_location
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - action_check_location
    - slot{"location": "mumbai"}
    - slot{"location_found": "found"}
    - utter_ask_price
* restaurant_search{"price": "more than 700"}
    - slot{"price": "more than 700"}
    - action_restaurant
    - slot{"result_found": true}
    - utter_should_email
* affirm
    - utter_ask_mail
* ask_email{"email": "bangaraniket@gmail.com"}
    - slot{"email": "bangaraniket@gmail.com"}
    - email_restaurant_details
    - action_restart

* greet
    - utter_greet
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - utter_ask_location
* restaurant_search{"location": "Pune"}
    - slot{"location": "pune"}
    - action_check_location
    - slot{"location": "pune"}
    - slot{"location_found": "found"}
    - utter_ask_price
* restaurant_search{"price": "more than 700"}
    - slot{"price": "more than 700"}
    - action_restaurant
    - slot{"result_found": true}
    - utter_should_email
* affirm
    - utter_ask_mail
* ask_email{"email": "bangaraniket@gmail.com"}
    - slot{"email": "bangaraniket@gmail.com"}
    - email_restaurant_details
    - action_restart

* greet
    - utter_greet
* restaurant_search{"cuisine": "italian", "location": "ptnsneha"}
    - slot{"cuisine": "italian"}
    - slot{"location": "ptnsneha"}
    - action_check_location
    - slot{"location": null}
    - slot{"location_found": "notfound"}
    - utter_location_notfound
* restaurant_search{"location": "patna"}
    - slot{"location": "patna"}
    - action_check_location
    - slot{"location": "patna"}
    - slot{"location_found": "found"}
    - utter_ask_price
* restaurant_search{"price": "between 300 to 700"}
    - slot{"price": "between 300 to 700"}
    - action_restaurant
    - slot{"result_found": true}
    - utter_should_email
* deny
    - utter_final_bye
    - action_restart

* greet
    - utter_greet
* restaurant_search{"cuisine": "italian", "location": "ptnsneha"}
    - slot{"cuisine": "italian"}
    - slot{"location": "ptnsneha"}
    - action_check_location
    - slot{"location": null}
    - slot{"location_found": "notfound"}
    - utter_location_notfound
* restaurant_search{"location": "patna"}
    - slot{"location": "patna"}
    - action_check_location
    - slot{"location": "patna"}
    - slot{"location_found": "found"}
    - utter_ask_price
* restaurant_search{"price": "between 300 to 700"}
    - slot{"price": "between 300 to 700"}
    - action_restaurant
    - slot{"result_found": false}
    - action_restart

* restaurant_search{"cuisine": "italian", "location": "solapur"}
    - slot{"cuisine": "italian"}
    - slot{"location": "solapur"}
    - action_check_location
    - slot{"location": "solapur"}
    - slot{"location_found": "found"}
    - utter_ask_price
* restaurant_search{"price": "more than 700"}
    - slot{"price": "more than 700"}
    - action_restaurant
    - slot{"result_found": true}
    - utter_should_email
* deny
    - utter_final_bye
    - action_restart
    - action_listen

* greet
    - utter_greet
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - utter_ask_location
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - action_check_location
    - slot{"location": "bangalore"}
    - slot{"location_found": "found"}
    - utter_ask_price
* restaurant_search{"price": "more than 700"}
    - slot{"price": "more than 700"}
    - action_restaurant
    - slot{"result_found": true}
    - utter_should_email
* affirm
    - utter_ask_mail
* ask_email{"email": "goyal.aiana@gmail.com"}
    - slot{"email": "goyal.aiana@gmail.com"}
    - email_restaurant_details
    - action_restart

* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - action_check_location
    - slot{"location": "bangalore"}
    - slot{"location_found": "found"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - utter_ask_price
* restaurant_search{"price": "between 300 to 700"}
    - slot{"price": "between 300 to 700"}
    - action_restaurant
    - slot{"result_found": false}
    - action_restart
    - action_listen

* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - action_check_location
    - slot{"location": "bangalore"}
    - slot{"location_found": "found"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - utter_ask_price
* restaurant_search{"price": "between 300 to 700"}
    - slot{"price": "between 300 to 700"}
    - action_restaurant
    - slot{"result_found": false}
    - action_restart
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location": "delhi"}
    - slot{"location_found": "found"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - utter_ask_price
* restaurant_search{"price": "more than 700"}
    - slot{"price": "more than 700"}
    - action_restaurant
    - slot{"result_found": true}
    - utter_should_email
* affirm{"email": "ahbcdj@dkj.com"}
    - slot{"email": "ahbcdj@dkj.com"}
    - email_restaurant_details
    - action_restart

* goodbye
    - utter_goodbye
    - action_restart
    - action_listen

* greet
    - utter_greet
* restaurant_search{"location": "Rishikesh"}
    - slot{"location": "Rishikesh"}
    - action_check_location
    - slot{"location": null}
    - slot{"location_found": "tier3"}
    - utter_foodie_not_working
* restaurant_search{"location": "Allahabad"}
    - slot{"location": "Allahabad"}
    - action_check_location
    - slot{"location": "Allahabad"}
    - slot{"location_found": "found"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* restaurant_search{"price": "more than 700"}
    - slot{"price": "more than 700"}
    - action_restaurant
    - slot{"result_found": true}
    - utter_should_email
* affirm{"email": "xyz@sth.edu"}
    - slot{"email": "xyz@sth.edu"}
    - email_restaurant_details
    - action_restart
* goodbye
    - utter_goodbye

* restaurant_search{"cuisine": "italian", "location": "mumbai"}
    - slot{"cuisine": "italian"}
    - slot{"location": "mumbai"}
    - action_check_location
    - slot{"location": "mumbai"}
    - slot{"location_found": "found"}
    - utter_ask_price
* restaurant_search{"price": "more than 700"}
    - slot{"price": "more than 700"}
    - action_restaurant
    - slot{"result_found": true}
    - utter_should_email
* affirm
    - utter_ask_mail
* ask_email{"email": "djdkjaskj@gddda.com"}
    - slot{"email": "djdkjaskj@gddda.com"}
    - email_restaurant_details
* goodbye
    - utter_goodbye
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - action_check_location
    - slot{"location": "mumbai"}
    - slot{"location_found": "found"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - utter_ask_price
* restaurant_search{"price": "between 300 to 700"}
    - slot{"price": "between 300 to 700"}
    - action_restaurant
    - slot{"result_found": false}
    - action_restart
    - action_listen

* restaurant_search{"location": "400601"}
    - slot{"location": "400601"}
    - action_check_location
    - slot{"location": null}
    - slot{"location_found": "notfound"}
    - utter_location_notfound
* restaurant_search{"location": "thane"}
    - slot{"location": "thane"}
    - action_check_location
    - slot{"location": null}
    - slot{"location_found": "notfound"}
    - utter_location_notfound
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - action_check_location
    - slot{"location": "mumbai"}
    - slot{"location_found": "found"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - utter_ask_price
* restaurant_search{"price": "more than 700"}
    - slot{"price": "more than 700"}
    - action_restaurant
    - slot{"result_found": true}
    - utter_should_email
* affirm{"email": "bangaraniket@gmail.com"}
    - slot{"email": "bangaraniket@gmail.com"}
    - email_restaurant_details
    - action_restart
    - action_listen

* greet
    - utter_greet
* restaurant_search{"location": "627364"}
    - slot{"location": "627364"}
    - action_check_location
    - slot{"location": null}
    - slot{"location_found": "notfound"}
    - utter_location_notfound
* restaurant_search{"location": "Agra"}
    - slot{"location": "agra"}
    - action_check_location
    - slot{"location": "agra"}
    - slot{"location_found": "found"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - utter_ask_price
* restaurant_search{"price": "more than 700"}
    - slot{"price": "more than 700"}
    - action_restaurant
    - slot{"result_found": true}
    - utter_should_email
* affirm{"email": "bangaraniket@gmail.com"}
    - slot{"email": "bangaraniket@gmail.com"}
    - email_restaurant_details
    - action_restart
    - action_listen

* restaurant_search{"location": "mumbai", "cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - slot{"location": "mumbai"}
    - action_check_location
    - slot{"location": "mumbai"}
    - slot{"location_found": "found"}
    - utter_ask_price
* restaurant_search{"price": "between 300 to 700"}
    - slot{"price": "between 300 to 700"}
    - action_restaurant
    - slot{"result_found": false}
    - action_restart
    - action_listen

* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - action_check_location
    - slot{"location": "mumbai"}
    - slot{"location_found": "found"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - utter_ask_price
* restaurant_search{"price": "betwen 300 to 700"}
    - slot{"price": "betwen 300 to 700"}
    - action_restaurant
    - slot{"result_found": false}
    - action_restart
    - action_listen

* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - action_check_location
    - slot{"location": "mumbai"}
    - slot{"location_found": "found"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}

* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - action_check_location
    - slot{"location": "mumbai"}
    - slot{"location_found": "found"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - utter_ask_price
* restaurant_search{"price": "lesser than 300"}
    - slot{"price": "lesser than 300"}
    - action_restaurant
    - slot{"result_found": false}
    - action_restart
    - action_listen

* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - action_check_location
    - slot{"location": "bangalore"}
    - slot{"location_found": "found"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - utter_ask_price
* restaurant_search{"price": "between 300 to 700"}
    - slot{"price": "between 300 to 700"}
    - action_restaurant
    - slot{"result_found": false}
    - action_restart
    - action_listen

* greet
    - utter_greet
* restaurant_search{"location": "Rishikesh"}
    - slot{"location": "Rishikesh"}
    - action_check_location
    - slot{"location": null}
    - slot{"location_found": "tier3"}
    - utter_foodie_not_working
* restaurant_search{"location": "Allahabad"}
    - slot{"location": "Allahabad"}
    - action_check_location
    - slot{"location": "Allahabad"}
    - slot{"location_found": "found"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* restaurant_search{"price": "more than 700"}
    - slot{"price": "more than 700"}
    - action_restaurant
    - slot{"result_found": true}
    - utter_should_email
* affirm{"email": "xyz@sth.edu"}
    - slot{"email": "xyz@sth.edu"}
    - email_restaurant_details
    - action_restart
    - action_listen

* greet
    - utter_greet
* restaurant_search{"location": "kolkata"}
    - slot{"location": "kolkata"}
    - action_check_location
    - slot{"location": "kolkata"}
    - slot{"location_found": "found"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - utter_ask_price
* restaurant_search{"price": "lesser than 300"}
    - slot{"price": "lesser than 300"}
    - action_restaurant
    - slot{"result_found": true}
    - utter_should_email
* affirm
    - utter_ask_mail
* affirm{"email": "jddk.2jmd@kdl.co.in"}
    - slot{"email": "jddk.2jmd@kdl.co.in"}
    - email_restaurant_details
    - action_restart
    - action_listen

* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "mubaim"}
    - slot{"location": "mubaim"}
    - action_check_location
    - slot{"location": null}
    - slot{"location_found": "notfound"}
    - utter_location_notfound
* restaurant_search{"location": "Mumbai"}
    - slot{"location": "Mumbai"}
    - action_check_location
    - slot{"location": "Mumbai"}
    - slot{"location_found": "found"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - utter_ask_price
* restaurant_search{"price": "lesser than 300"}
    - slot{"price": "lesser than 300"}
    - action_restaurant
    - slot{"result_found": false}
    - action_restart
    - action_listen

* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "chandigarh"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "chandigarh"}
    - action_check_location
    - slot{"location": "chandigarh"}
    - slot{"location_found": "found"}
    - utter_ask_price
* restaurant_search{"price": "lesser than 300"}
    - slot{"price": "lesser than 300"}
    - action_restaurant
    - slot{"result_found": false}
    - action_restart
    - action_listen

* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location": "delhi"}
    - slot{"location_found": "found"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - utter_ask_price
* restaurant_search{"price": "more than 700"}
    - slot{"price": "more than 700"}
    - action_restaurant
    - slot{"result_found": true}
    - utter_should_email
* deny
    - utter_final_bye
    - action_restart
    - action_listen
