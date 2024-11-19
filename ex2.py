#! /usr/bin/env python3
#Author: Brad
#version: 1.0
#Description: Ex2 python script

firstname = input ("Enter your First Name: ")
lastname = input ("Enter your Last Name: ")

print("Your name is:" ,firstname, lastname)

names = [firstname, lastname]
print(names)

namesdict = {'firstname': firstname, 'lastname': lastname}
print(namesdict['firstname'], namesdict['lastname'])

