# innovaccer-summergeeks-assignment

[![Build Status](https://travis-ci.org/adwait-thattey/innovacer_summergeeks_assignment.svg?branch=master)](https://travis-ci.org/adwait-thattey/innovacer_summergeeks_assignment)

---
The Entry management software for Innovaccer Summer Geeks Challenge

Stack: Backend in django-2.2.7, Frontend in MaterializeCSS

There are 2 types of Users: Host and Visitor

Hosts need to have an account. Right now anyone can register and create a host account.   
Visitors can choose which host they want to visit. 

Once a visitor checks-in, an email is sent to the corresponding host.  
After the visitor checks out, email is sent to visitor with details about the visit

> Only emails are being sent. Not text messages as I have exhausted my Twilio free account limit


The models are designed in this way:

**User**: Contains common information about any person [registration/models](https://github.com/adwait-thattey/innovacer_summergeeks_assignment/blob/master/registration/models.py)  
**Host**: One-To-One related with User. Contains details specific to a Host  
**Visitor**: One-To-One related with User. Contains details specific to a Visitor  
**VisitorLog**: Contains logs of visitors

Once a visitor checks-in, a 5 digit token is generated for the user. The token is used by the visitor during checkout. 
This is done so that a visitor does not need to create an account just to visit. And no one can check-out on someone else's behalf by just using email.


Emails are being sent using [SendGrid](https://sendgrid.com/)
