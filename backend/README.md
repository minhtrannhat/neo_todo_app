# Backend Technical Write-up

## Steps

- Initial infrastructure
- Rate Limiting
- JSON error handling
- Req/Res schema validation
- Setup database
- Database schema/models
- Usersessions
- CRUD routes functionalities

## Quart specific terminologies

`blueprint`: a collection of route handlers/API functionalities.

## API route trailing slashes

API paths should end with a slash i.e: `/sessions/` rather than `/session`.
This is because requests sent to `/sessions` will be redirected to `/sessions/` whereas `/sessions/` won't get redirected.

## Difference between database schema and database model

- A schema defines the structure of data within the database.
- A model is a class that can be represented as rows in the database, i.e ID row, age row as class member.

## Managing user's sessions (Authentication)

- Login should results in a cookie being set in the user's browser, which is being sent in every subsequent request.
  The presence and value of this cookie are used to determine whether the member is logged in, and which member made the request.
- Logout results in the cookie being deleted.

## Idempotent routes

Idempotence is a property of a route where the final state is achieved no matter how many times the route is called, that is, calling the route once or 10 times has the same effect. This is a useful property as it means the route can be safely retried if the request fails. For RESTful and HTTP APIs, the routes using GET, PUT, and DELETE verbs are expected to be idempotent.
