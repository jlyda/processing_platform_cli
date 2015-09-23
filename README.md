# processing_platform_cli

The *client_identify.py* sends a fingerprint to the processing platform. The *client_callback.py* is a dummy flask application that waits for callbacks.

## Authentification token request

```
AUTH_REQUEST_JSON =
{
 username: "test",
 password: "test"
}
```

## Authentification token response

```
AUTH_RESPONSE_JSON =
{
 username: "test",
 id: 1
 token: "eyJhbGciOiJIUzI1NiIsImV4cCI6MTQ0Mjk0OTI3MiwiaWF0IjoxNDQyOD",
 tokenExpireTimeStamp: 1442949272
 tokenExpireIso: "2015-09-22T16:14:32"
}
```

## Identification request

```
IDENTIFICATION_REQUEST_JSON =
{
 callbackUrl: "http://127.0.0.1:5001/callback/de305d54-75b4-431b-adb2-eb6b9e546013/",
 fingerprint: "exm5dfjKd/Ycxe/mp8vP5aRZSvnebtOHyp/5Lc5SEB+Gfb9..."
}
```

## Identification response

```
IDENTIFICATION_RESPONSE_JSON =
{
 status: 202,
 response: {
  identificationId: "21ec2020-3aea-1069-a2dd-08002b30309d"
 }
}
```

## Final results in identification callback

```
IDENTIFICATION_CALLBACK_JSON =
{
 status: 200,
 response: {
  identificationId: "21ec2020-3aea-1069-a2dd-08002b30309d",
  catalogueName: "blocked",
  matches:
    [{ start: 0,
       end: 60,
       metadata: {
         trackName: "Girl Gone Wild",
         artistName: "Madonna"
       }
     },
     { start: 60,
       end: 200,
       metadata: {
         trackName: "The Beatles",
         artistName: "Yellow Submarine"
       }
     }
    ]
 }
}
```

