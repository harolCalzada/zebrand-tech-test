# Description of the task

We need to build a basic catalog system to manage _products_. A _product_ should have basic info such as sku, name, price and brand.

In this system, we need to have at least two type of users: (i) _admins_ to create / update / delete _products_ and to create / update / delete other _admins_; and (ii) _anonymous users_ who can only retrieve _products_ information but can't make changes.

As a special requirement, whenever an _admin_ user makes a change in a product (for example, if a price is adjusted), we need to notify all other _admins_ about the change, either via email or other mechanism.

We also need to keep track of the number of times every single product is queried by an _anonymous user_, so we can build some reports in the future.

Your task is to build this system implementing a REST or GraphQL API using the stack of your preference. 