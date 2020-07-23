import imgkit
import mysql.connector


options = {
	'format': 'png',
	'encoding': 'UTF-8',
	'quiet': '',
	'width': '750',
	'disable-smart-width': '',
	'quality': 10,
	'custom-header': [
		('user-agent', 'Mozilla/5.0 (Linux; Android 7.0; SM-G930V Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36')
	]
}



mydb = mysql.connector.connect(
  host="url",
  user="user",
  passwd="pwd",
  database="database"
)

mycursor = mydb.cursor()
mycursor.execute("select activity_info from pmll_activity;")


for idx, x in enumerate(mycursor):
	if not x[0]:
		continue

	code = x[0]
	print(code)
	code = code.replace('width:auto;', 'max-width: 100%; display: block;')
	code = code.replace('width: auto;', 'max-width: 100%; display: block;')
	frame = """
	<!DOCTYPE html>
	<html>

	<head>
	  <meta charset="utf-8">
	  <meta name="keywords" content="" />
	  <meta name="description" content="" />
	  <meta name="viewport" content="width=device-width,initial-scale=1.0,maximum-scale=1.0,user-scalable=0" />
	  <meta name="format-detection" content="telephone=no" />
	  <meta name="apple-mobile-web-app-capable" content="yes" />
	  <meta name="apple-mobile-web-app-status-bar-style" content="black">
	  <title>web_mobile</title>
	  <style>
    body{font-size:62.5%;font-family:"Microsoft YaHei",Arial; overflow-x:hidden; overflow-y:auto;}
    .viewport{ max-width:640px; min-width:300px; margin:0 auto;}

    html{height: 0px; width: 375px; zoom: 2;}
</style>
	</head>
	<body>""" + code + """</body>"""
	print(frame)
	imgkit.from_string(frame, f'output/{idx}.png', options=options)