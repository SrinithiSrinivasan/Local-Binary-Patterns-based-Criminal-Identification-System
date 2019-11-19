#Loginflask.py
from flask import Flask, render_template, redirect, url_for, request
from werkzeug import secure_filename
import os
app = Flask(__name__)
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('upload_file'))
    return render_template('login.html', error=error)    
@app.route('/upload_file')
def upload_file():
   return render_template('upload.html')
@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file1():
   if request.method == 'POST':
      f = request.files['file']
      f.save(secure_filename(f.filename))
      os.system('python integrate.py')
      return 'file uploaded successfully'
if __name__ == '__main__':
   app.run(debug = True)

Login.html
<html>
<head>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
<style>
body{
background-image:url("alvaro-pinot-502465-unsplash.jpg");
 margin: 0;
  font-family: Arial, Helvetica, sans-serif;
  
}

.topnav {
  overflow: hidden;
  background-color: #000000;
}

.topnav a {
  float: left;
  color: lime;
  text-align: center;
  padding: 14px 16px;
  text-decoration: none;
  font-size: 17px;
}


.topnav a:hover {
 color:white;
 transform: scale(1.3);
}
.topnav a.active {
  background-color: #ff0080;
  color:white;
}
 
div.transbox {
  margin-left: 300px;
  margin-top:20px;
  background-color:#ffffff;
  border: 1px solid black;
  opacity: 0.7;
  filter: alpha(opacity=60); /* For IE8 and earlier */
  border-radius: 50px 50px;
    padding: 20px; 
    width: 700px;
    height: 700px; 
}

div.trans{
opacity:0.9;
 background-color:#ffff00;
  height: 50px;
color:#400080;
font-weight:bold;
  
}

input[type=text], input[type=password] {
    width: 60%;
    padding: 12px 20px;
    margin: 8px 0;
    display: inline-block;
    border: 1px solid #ccc;
    box-sizing: border-box;
	background-color:#000000;
	border-radius:15 px;
	color:#ffffff;
	font-size:"7";
	font-family: Arial, Helvetica, sans-serif;
	font-weight:bold;
}
input:hover{
opacity:0.9;
}
button {
    background-color:lime;
    color: white;
    padding: 14px 20px;
    margin: 8px 0;
    border: none;
    cursor: pointer;
	border-radius: 12px;
	width: 50%;
}

button:hover {
    opacity: 0.8;
}

.cancelbtn {
    width: auto;
    padding: 10px 18px;
    background-color: #ff0000;
}

.imgcontainer {
    text-align: center;
    margin: 24px 0 12px 0;
}

img.avatar {
    width: 40%;
    border-radius: 50%;
}

.container {
    padding: 16px;
	width: 50 px;
	height:50 px;
}

span.psw {
    float: right;
    padding-top: 16px;
}
p{color:#000000;
font-family: Arial, Helvetica, sans-serif;
font-size:"7";
}
</style>
</head>
<body>
<div class="topnav">
  </div>
<div class="transbox">
<div class="trans">
<h1 align="center">LOGIN PAGE</h1>
</div>
</hr>
<form id="members" method="post">
  <div class="imgcontainer">
    <!img src="" alt="Avatar" class="avatar">
  </div>
<div class="container">
  <i class="fa fa-address-book-o" style="font-size:36px;color:black"></i>
    <label for="uname"><b>USERNAME</b></label>
	<br>
    <input type="text"  placeholder="Enter username" name="username" value="{{
          request.form.username }}">
     <br> <br>
	 <i class="fa fa-expeditedssl" style="font-size:36px;color:black"></i>
	  <label for="psw"><b>PASSWORD</b></label>
	<br>
<input type="password" placeholder="Enter Password" name="password" value="{{
          request.form.password }}">
        <br><br><br><br>
    <input class="btn btn-default" type="submit" value="Login">
	<br>
 </div>
<div class="container" style="background-color:#f1f1f1">
 </div>
</form>
  {% if error %}
        <p class="error"><strong>Error:</strong> {{ error }}
      {% endif %}
</div>
</body>
</html>

Upload.html
<html>
<style>

.button {
  background-color: #4CAF50;
  border: none;
  color: white;
  padding: 15px 32px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
  margin: 4px 2px;
  cursor: pointer;
}
.modal {
  display: none; /* Hidden by default */
  position: fixed; /* Stay in place */
  z-index: 1; /* Sit on top */
  left: 0;
  top: 0;
  width: 50%; /* Full width */
  height: 100%; /* Full height */
  overflow: auto; /* Enable scroll if needed */
  background-color: #474e5d;
  padding-top: 50px;
  border-radius: 25px;
}

/* Modal Content/Box */
.modal-content {
  background: #f6f1d3;
   //background: linear-gradient(to right, , #648880 85%, #293f50);
  
  margin: 5% auto 15% auto; /* 5% from the top, 15% from the bottom and centered */
  border: 1px solid #888;
  border-radius: 25px;
  width: 30%; /* Could be more or less, depending on screen size */
  height:30%;
}
.container {
  padding: 16px;
}

</style>
   <body background="download.jpg">
   <center><h1 style="color:white" font-family:"Georgia">CRIMINAL INVESTIGATION SYSTEM</H1></center>
   <br><br><br>
      <form class="modal-content" action = "http://localhost:5000/uploader" method = "POST" 
         enctype = "multipart/form-data">
         <div class="container"> <br><br>
         <center><input type = "file" name = "file" />		
         <input class="button" type = "submit"/>
      </form>
   </body>
</html>



