## Person API

This project is a simple REST API capable of performing CRUD operations on person resource
It can dynamically handle parameters such as adding a person by name, retriving person by name etc.

## UML
![UML Diagram](./assets/uml.png)

## Structure of the API
```
- POST /api
    - Creating a  new person
- GET /api/:id
    - Fetch details of a person based on the ID
- PUT /api/:id 
    - Edit person's details based on the ID
- DELETE api/:id
    - DELETE a person based on the ID
```

## Assumptions
we have assumed that all users will have unique names, so using the name in place of id should work just fine. What this means is that 

```
GET /api/:id
```

And

```
GET /api/:name
```

Should have the same idempotent effect.
## Setup and Usage
There's two options to running this api, directly from the source code, or as a docker container

### Directly from source code



### As a docker container
Coming sooon!


More details can be found in the [Documentation](./DOCUMENTATION.md)