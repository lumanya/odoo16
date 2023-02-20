## Table of contents
* [Introduction](#Introduction)
* [What is Odoo?](#What-is-Odoo?)
* [Technologies](#Technologies)
* [Architecure Overview](#Architecure-Overview)
* [Development Environment Setup](#Development-Environment-Setup)


# Introduction
Odoo16 is cloned project  to master odoo version 16 Technology of which include odoo default apps and custom module

## What is Odoo?
Odoo is the suite of open source business apps that cover all your company needs:CRM,eCommerce,Accounting,Inventory, Point of sale, Project Management etc
## Technologies
Project is create with
* Python3
* HTML5
* JavaScript
* CSS
* PostgreSQL
## Architecure Overview
Architecture Overview of Odoo odoo is the Multier Application which means it include
* Presentation
* Business logic
* Data 

The Presentation tier is the combination of HTML5, CSS andJavaScript. The Business Logic tier is exclusively written in python where the data tier only support PostgreSQl as RDBMS

## Development Environment Setup
To run this project locally insure you have python3, virtualenvironment and postgresql installed
```
$ sudo apt install python3
$ sudo apt install -y python3-pip
$ sudo apt install -y python3-venv
```
Then, install the Postgres package along with a -contrib package that adds some additional utilities and functionality:
```
$ sudo apt install postgresql postgresql-contrib
$ sudo systemctl start postgresql.service
```
Now,
```
$ cd scr
$ source venv/bin/activate
$ pip install setuptools wheel
$ cd odoo
$ pip install -r requirements.txt
$ python odoo-bin
```

This repository contains all Odoo version 16 apps and custom module that have been developing.
