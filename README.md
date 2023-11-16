# DragonPark API Documentation

## Note: The front-End Not comleted Because i am a back-end work in this with my own so hope you get this execuse , You can test them by post man.

## Overview

This document provides documentation for the DragonPark API, which manages dragons and their locations within the park.

## Dragon Endpoints

## Before you expose the API you always get endpoint with dragon's ID AND I commented that and you will understand it from the code and i do this to be unified and readable and also some arguments will be not with id but with the name to make request easy for the user also and this is all in the view of the system.

### Add Dragon

- **URL:** `/add/`
- **Method:** `POST`
- **Description:** Add a new dragon to the park.
- **Request Body:**

  jsonCopy code

  `{
  "name": "DragonName",
  "species": "DragonSpecies",
  "gender": "Male/Female",
  "digestion_period_hours": 48,
  "herbivore": false
}`

- **Response:** Returns details of the added dragon.

### List Dragons

- **URL:** `/list/`
- **Method:** `GET`
- **Description:** Get a list of all dragons in the park.
- **Response:** Returns a list of dragons with their details.

  jsonCopy code

  `[
  {
    "id": 1,
    "name": "DragonName",
    "species": "DragonSpecies",
    "gender": "Male/Female",
    "digestion_period": 48,
    "herbivore": false,
    "time": "2023-11-16T10:00:00.000Z"
  },
  ...
]`

### Delete Dragon

- **URL:** `/<int:pk>/delete/`
- **Method:** `DELETE`
- **Description:** Delete a dragon by providing its ID.
- **Response:** Returns a success message upon deletion.

### Update Dragon Location

- **URL:** `/<int:pk>/updatelocation/`
- **Method:** `PUT`
- **Description:** Update the location of a dragon by providing its ID.
- **Request Body:**

  jsonCopy code

  `{
  "location": "NewLocation"
}`

- **Response:** Returns details of the updated dragon.

### Update Dragon Fed Status

- **URL:** `/<int:pk>/fedupdate/`
- **Method:** `PUT`
- **Description:** Update the fed status of a dragon by providing its ID.
- **Request Body:**

  jsonCopy code

  `{
  "fed": true
}`

- **Response:** Returns details of the updated dragon.

### Update Zone Maintenance Status

- **URL:** `/<int:pk>/updatemaintaine/`
- **Method:** `PUT`
- **Description:** Update the maintenance status of a zone by providing its ID.
- **Request Body:**

  jsonCopy code

  `{
  "maintenance": true
}`

- **Response:** Returns details of the updated zone.

## Zone Endpoint

### Check Zone

- **URL:** `/checkzone/`
- **Method:** `GET`
- **Description:** Check the status of park zones.
- **Response:** Returns a JSON object indicating the status of each zone.

  jsonCopy code

  `{
  "A0": false,
  "A1": true,
  "A2": false,
  ...
}`

## Actions App

    Represents an action in the system, capturing events such as dragon additions,
    removals, location updates, feedings, etc.

    Attributes:
    - kind: The type or kind of action (e.g., 'dragon_added', 'dragon_removed', etc.).
    - created: The timestamp when the action was created.
    - target_ct: The ContentType of the target object associated with the action.
    - target_id: The ID of the target object associated with the action.
    - target: A GenericForeignKey field representing the target object associated with the action.

    Meta:
    - indexes: Database indexes to optimize queries on the created timestamp and target object.
    - ordering: The default ordering for the Action model based on the created timestamp.

    - *I Have defined in utils.py the function to create this action*

## This is final result

``## Dragon List and Creation

### Endpoint: `/nudls/add/`

- **Method:** `POST`
- **Description:** Create a new dragon in DragonPark.

#### Request Body

```json
{
  "name": "McGroggity",
  "species": "deadly nadder",
  "gender": "males",
  "digestion_period": 48,
  "herbivore": false,
  "time": "2018-04-20T11:50:53.4601"
}``

#### Response

jsonCopy code

`{
  "kind": "dragon_added",
  "Data Saved": {
    "name": "McGroggity",
    "species": "deadly nadder",
    "gender": "males",
    "digestion_period": 48,
    "herbivore": false,
    "time": "2018-04-20T11:50:53.4601"
  }
}`

### Endpoint: `/nudls/list/`

-   **Method:** `GET`
-   **Description:** Get a list of all dragons in DragonPark.

#### Response

jsonCopy code

`[
  {
    "name": "McGroggity",
    "species": "deadly nadder",
    "gender": "males",
    "digestion_period": 48,
    "herbivore": false,
    "time": "2018-04-20T11:50:53.4601"
  },
  // ... other dragons ...
]`

## Dragon Deletion

### Endpoint: `/nudls/<dragon_id>/delete/`

-   **Method:** `DELETE`
-   **Description:** Remove a dragon from DragonPark.

#### Response

jsonCopy code

`{
  "kind": "dragon_removed",
  "id": 1,
  "time": "2023-11-16T12:00:00.000Z"
}`

## Dragon Location Update

### Endpoint: `/nudls/<dragon_id>/updatelocation/`

-   **Method:** `PUT`
-   **Description:** Update the location of a dragon in DragonPark.

#### Request Body

jsonCopy code

`{
  "dragon": "McGroggity",
  "location": "E10",
  "time": "2023-11-16T12:00:00.000Z"
}`

#### Response

jsonCopy code

`{
  "kind": "dragon_location_updated",
  "Data": {
    "dragon": "McGroggity",
    "location": "E10",
    "time": "2023-11-16T12:00:00.000Z"
  }
}`

## Dragon Feeding Update

### Endpoint: `/nudls/<dragon_id>/fedupdate/`

-   **Method:** `PATCH`
-   **Description:** Update the feeding status of a dragon in DragonPark.

#### Request Body

jsonCopy code

`{
  "time": "2023-11-16T12:00:00.000Z"
}`

#### Response

jsonCopy code

`{
  "kind": "dragon_fed",
  "Data": {
    "dragon": "McGroggity",
    "time": "2023-11-16T12:00:00.000Z"
  }
}`

## Zone Maintenance Check

### Endpoint: `/nudls/checkzone/`

-   **Method:** `GET`
-   **Description:** Check the maintenance status of all zones in DragonPark.

#### Response

jsonCopy code

`{
  "A0": true,
  "A1": false,
  // ... other zones ...
}`
```
