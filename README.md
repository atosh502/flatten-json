Install python and run with: `python main.py`

Tries to flatten a nested json object.

Example file: sample.json

Original JSON object
```
{
  "product": "Live JSON generator",
  "version": 3.1,
  "releaseDate": "2014-06-25T00:00:00.000Z",
  "demo": true,
  "person": {
    "id": 12345,
    "name": "John Doe",
    "phones": {
      "home": "800-123-4567",
      "mobile": "877-123-1234"
    },
    "email": [
      "jd@example.com",
      "jd@example.org"
    ],
    "dateOfBirth": "1980-01-02T00:00:00.000Z",
    "registered": true,
    "emergencyContacts": [
      {
        "name": "Jane Doe",
        "phone": "888-555-1212",
        "relationship": "spouse"
      },
      {
        "name": "Justin Doe",
        "phone": "877-123-1212",
        "relationship": "parent"
      }
    ]
  }
}
```

After running through the function
```
{
    "product": "Live JSON generator",
    "version": 3.1,
    "releaseDate": "2014-06-25T00:00:00.000Z",
    "demo": true,
    "person.id": 12345,
    "person.name": "John Doe",
    "person.dateOfBirth": "1980-01-02T00:00:00.000Z",
    "person.registered": true,
    "person.phones.home": "800-123-4567",
    "person.phones.mobile": "877-123-1234",
    "person.email.0": "jd@example.com",
    "person.email.1": "jd@example.org",
    "person.emergencyContacts.0.name": "Jane Doe",
    "person.emergencyContacts.0.phone": "888-555-1212",
    "person.emergencyContacts.0.relationship": "spouse",
    "person.emergencyContacts.1.name": "Justin Doe",
    "person.emergencyContacts.1.phone": "877-123-1212",
    "person.emergencyContacts.1.relationship": "parent"
}
```

Suggestions, improvements and bugs are always appreciated.