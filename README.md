# Taktaan: Docker Management API

## Introduction

Taktaan is part of the sample code for [Fontoberta's](http://www.fontoberta.com) software development services. It is a simple API for Docker container management. It was written in Python 3, using Flask and Flask-Restful. 

Complete deployment is available via script using Docker in the [Fontoberta Demo](https://github.com/fontoberta/fontoberta-demo) repository.

## Dependencies

Taktaan requires a Docker installation on the host machine. It will recover container information from the default socket, which can be configured on the application/settings.py file.

Token authentication for Taktaan is provided by [Boon API](https://github.com/fontoberta/boon). Boon URLs must be configured in application/settings.py. If only Taktaan installation is desired, Boon URLs should be set to 'standalone'.


## Docker Installation

To deploy Taktaan to a docker container, execute the following from the application directory:

`$ docker-compose up -d`

A container called taktaan-service will be deployed. 

This Taktaan instance will work in combination with the [Boon API](https://github.com/fontoberta/boon) container. If you need to deploy it to a docker container in standalone mode, please change the application/settings.py file in the prod section.

The API is available on port 5000 on your localhost, and will return the container list in JSON format. 

## Local Installation

In order to run the API locally, create a virtualenv with python 3  on your local system and activate it, as follows: 

`$ virtualenv envdir`
 
` $ source envdir/bin/activate`

Install the app dependencies executing the following from the application directory:

`(env)$ pip install -r requirements.pip`

Use the development server to test the API, by executing the following, also in the application directory:

`(env)$ python main.py`

The API is available on port 5000 on your localhost, and will return the container list in JSON format. 

# Usage

Two operations are available in Taktaan: list all containers, and start/stop a particular container. 

List all containers (get):

`http://<host>/`

Start/stop container (post):

`http://<host>/<containerId>`

If we have the security option enabled (application/settings.py Boon Urls != 'standalone'), a token must be provided as a header (token=<oauth_token>). In our scenario, tokens are requested and handled by the client:[Fontoberta Demo](https://github.com/fontoberta/fontoberta-demo).

The body must contain the operation to be executed:

`{`
`	"operation": "start"`
`}`
