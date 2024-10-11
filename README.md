# Immfly Technical Interview Test

## Technologies used

- Python 3.10 and Django
- PostgreSQL

## Execution instructions

This project needs docker to deploy the whole environment, which is composed of 2 containers : 
 - Python / Django container
 - PostgreSQL container

The project should be correctly setup after running `docker-compose build` and `docker-compose up`

## SQL Script

The script used to recreate the DB is located in sql/data.sql

## API URLs

- contents/<content_id> : To get all the information of a content <content_id>.
- channels/contents/<channel_id> : To get the contents of a channel. Replace <channel_id>
- channels/ : To get all the channels that have subchannels.
- channels/<channel_id> : To get the information of a channel. Replace <channel_id>