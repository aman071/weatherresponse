#NAME: AMAN REHMAN
#SECTION A
#ROLL NO.: 2017278
from urllib.request import urlopen
import datetime

# function to get weather response
def weather_response(location, API_key):
	result=urlopen("http://api.openweathermap.org/data/2.5/forecast?q="+location+"&APPID="+API_key).read().decode('UTF-8')
	return str(result)


# function to check  for valid response
def has_error (location,json):

	if json.find(location)==-1:				#if location is not in json string
		return True
	
	else:									#location matches the location stored in json
		return False


# function to get temperature on nth day
def get_temperature (json, t, n=0):
	date=datetime.date.today() + datetime.timedelta(days=n)	#incrementing date
	date=str(date)		#converting list to str

	if(date+' '+t in json):			#checking for requested date and time
		end=json.find(date+' '+t)
		search_str1="temp"
		temp_start=json.find(search_str1,end-330,end)
		temp_end=json.find(',', temp_start+len(search_str1)+2, end)
		return float(json[temp_start+len(search_str1)+2:temp_end])

	else:
		return 0


# function to get humidity on nth day
def get_humidity(json, t,n=0):
	date=datetime.date.today() + datetime.timedelta(days=n)	#incrementing date
	date=str(date)					#converting list to str

	if date+' '+t in json:		#checking for requested date and time
		end=json.find(date+' '+t)
		search_str2="humidity" 
		humid_start=json.find(search_str2,end-330,end)
		humid_end=json.find(',',humid_start+len(search_str2)+2,end)
		return float(json[humid_start+len(search_str2)+2:humid_end])

	else:
		return 0


# function to get pressure on nth day
def get_pressure(json, t,n=0):
	date=datetime.date.today() + datetime.timedelta(days=n)	#incrementing date
	date=str(date)				#converting list to str

	if date+' '+t in json:			#checking for requested date and time
		end=json.find(date+' '+t)
		search_str3="pressure"
		pressure_start=json.find(search_str3,end-330,end)
		pressure_end=json.find(',', pressure_start+len(search_str3)+2, end)
		return float(json[pressure_start+len(search_str3)+2:pressure_end])

	else:
		return 0


# function to get wind on nth day
def get_wind(json, t,n=0):
	date=datetime.date.today() + datetime.timedelta(days=n)	#incrementing date
	date=str(date)					#converting list to str

	if date+' '+t in json:			#checking for requested date and time
		end=json.find(date+' '+t)
		search_str4="speed"
		wind_start=json.find(search_str4,end-330,end)
		wind_end=json.find(',',wind_start+len(search_str4)+2,end)
		return float(json[wind_start+len(search_str4)+2:wind_end])

	else:
		return 0


# function to get sea level on nth day
def get_sealevel(json, t,n=0):
	date=datetime.date.today() + datetime.timedelta(days=n)	#incrementing date
	date=str(date)					#converting list to str

	if date+' '+t in json:			#checking for requested date and time
		end=json.find(date+' '+t)
		search_str5="sea_level"
		sea_start=json.find(search_str5,end-330,end)
		sea_end=json.find(',',sea_start+len(search_str5)+2,end)
		return float(json[sea_start+len(search_str5)+2:sea_end])

	else:
		return 0