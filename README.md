# Description of the task

We need to build a basic catalog system to manage _products_. A _product_ should have basic info such as sku, name, price and brand.

In this system, we need to have at least two type of users: (i) _admins_ to create / update / delete _products_ and to create / update / delete other _admins_; and (ii) _anonymous users_ who can only retrieve _products_ information but can't make changes.

As a special requirement, whenever an _admin_ user makes a change in a product (for example, if a price is adjusted), we need to notify all other _admins_ about the change, either via email or other mechanism.

We also need to keep track of the number of times every single product is queried by an _anonymous user_, so we can build some reports in the future.

Your task is to build this system implementing a REST or GraphQL API using the stack of your preference. 


## Requirements
- docker y docker-compose
- make (optional)

## Assumptions:
- We can use django admin for create new users and manage permissions.

## Solution
- The project use django and django rest framework.
- The project use the default User model from django,
is a admin user if "is_staff" or "is_superuser" field is True
- For notifications the project use a broker and worker to send an email in background(dramatiq library).
- The project uses a in memory database to save the product queried data(redis).

## Build the project for local environment
Create a .env file inside server-config/local folder with the values inside env_template file
```
$ make docker-local-build
```
```
$ make docker-local-run
```

## Tools for developing in local environment

The project uses the following tools:
- docker, the project uses a back , postgres, smt, redis, worker containers
- django debug toolbar library
- pytest for testing, you can execute ```$ make docker-local-run-tests``` for run all test cases
- swagger: you can visit http://localhost:8000/swagger for check the documentation



## TO DO
- tests for email notification and product counter
- create the config for a production environment(new docker configuration)
- add rate limit to product detail api (to avoid bots that can generate false counter visit value)
- improve mail message to track product values changed
- Generate data to load on initial setup(django fixtures)