
[Scroll down for english](#moses-smt-online-api)

# API Cyfieithu Peirianyddol Moses-SMT

Mae swyddogaethau peiriannau cyfieithu y storfa hon ar gael dros y we o'r Canolfan APIs [gweler https://api.techiaith.org](https://api.techiaith.org). Mae'r API yn gweithio dros HTTPS GET, felly gellir defnyddio unrhyw iaith/meddalwedd HTTP er mwyn cysylltu at yr API. 

## Tiwtorialau

Mae [Twitorial 1](demo1.md) yn enghraifft o sut i ddefnyddio API cyfieithu peirianyddol i gyfieithu testun


## Fersiwn Cyfredol

Mae un fersiwn o API Cyfieithu Peiraianyddol ar gael. v1 neu 'fersiwn 1'.
Dychwelir enw'r fersiwn sy'n cael ei ddefnyddio yn y canlyniadau JSON.

Mi fydd yr URL yn newid ar gyfer pob fersiwn newydd o'r API. Ar hyn o bryd, dylid defnyddio `/v1` ar gyfer fersiwn 1.

## Sgema

Mae cysylltu â'r API yn gweithio dros HTTPS yn unig, gan ddefnyddio'r parth `api.techiaith.org/translate`. Mae'r holl ddata sy'n cael ei dderbyn/anfon yn cael ei drosglwyddo ar ffurf JSON ([unicode-escaped ASCII](http://tools.ietf.org/html/rfc5137)).

## Paramedrau

| Paramedr     | Disgrifiad | Sylwadau |
|--------------|------------|----------|
| `api_key`    | Eich allwedd API, ar gael o'r Canolfan APIs (https://api.techiaith.org) | angenrheidiol |
| `q`       | Y testun i'w gyfieithu. Wedi ei fformatio yn ôl RFC 3986 (percent-encoded) | angenrheidiol |
| `engine` | Enw'r peiriant rydych am defnyddio i gyfieithu'n peirianyddol. Y dewis yw : CofnodYCynulliad  neu Deddfwriaeth | angenrheidiol |
| `source` | Iaith y testun ffynhonnell. Dewis o `en` neu `cy`. | angenrheidiol |
| `target` | Iaith ar gyfer y cyfieithiad sy'n cael ei ddychwelyd yn ôl.  Dewis o `en` neu `cy`. | angenrheidiol |
| `callback`   | Enw 'function' ar gyfer unrhyw callback JSON-P (gweler isod) | dewisiol |

### Enghriafft

```
$ curl https://api.techiaith.org/translate/v1/translate?api_key=123&q=Will+the+Minister+make+a+statement&engine=CofnodYCynulliad&source=en&target=cy

{
    "success": true,
    "translations": [
        {"translatedText": "A wnaiff y Gweinidog wneud datganiad"},
    ],
    "version": 1
}
```

## JSON-P Callbacks

Gellir defnyddio'r API gyda JSON-P callbacks trwy ychwanegu'r paramedr `callback` i'ch galwad:

```
$ curl https://api.techiaith.org/translate/v1/translate?api_key=123&q=Will+the+Minister+make+a+statement&engine=CofnodYCynulliad&source=en&target=cy&callback=foo
foo({
	"success": true,
	"translations": [
		{"translatedText": "A wnaiff y Gweinidog wneud datganiad"},
	],
    	"version": 1
});
```


## Cyfyngu nifer yr alwadau yr awr

Mae gan yr API gyfyngiad ar nifer yr alwadau y gellir eu gwneud mewn awr.

Os ydych eisiau cynyddu nifer y galwadau at yr API sydd gennych, cysylltwch â ni.

Gellir gweld cyfanswm nifer eich galwadau ar unrhyw adeg drwy edrych ar y 'HTTP headers' yn eich galwad API:

```
$ curl -i https://api.techiaith.org/translate/v1/translate?api_key=123&q=Will+the+Minister+make+a+statement&engine=CofnodYCynulliad&source=en&target=cy                                                            

HTTP/1.1 200 OK
Date: Mon, 17 Nov 2014 14:41:21 GMT
Content-Type: application/json
Content-Language: cy
X-Ratelimit-Remaining: 276
X-Ratelimit-Limit: 24
X-Ratelimit-Reset: 1416237399
```

Mae'r headers yn cynnwys yr holl wybodaeth sydd ei angen:

| Enw'r Header | Disgrifiad |
|--------------|------------|
| X-RateLimit-Limit | Y nifer mwyaf o alwadau allwch chi eu gwneud mewn awr |
| X-RateLimit-Remaining | Y nifer o alwadau sydd gennych ar ôl yn y 'blwch' cyfyngu presennol |
| X-RateLimit-Reset | Yr amser y bydd y 'blwch' cyfyngu presennol yn cael ei ail-osod, mewn [eiliadau epoch UTC](http://en.wikipedia.org/wiki/Unix_time) |

Os ydych chi angen yr amser mewn fformat gwahanol, gellir gwneud hyn gydag unrhyw iaith raglennu modern. Er engraifft, gellir gwneud hyn trwy gonsol eich porwr (gyda Javascript) a dychwelych gwrthrych 'Javascript Date'.


```javascript
new Date(1416237399 * 1000)
Date 2014-11-17T15:16:39.000Z
```

Ar ôl i chi fynd dros eich nifer mwyaf o alwadau yr awr, byddwch yn derbyn gwall gan y gweinydd (403 Forbidden):


```
curl -i https://api.techiaith.org/translate/v1/translate?api_key=123&q=Will+the+Minister+make+a+statement&engine=CofnodYCynulliad&source=en&target=cy

HTTP/1.1 200 OK
Date: Tue, 18 Nov 2014 10:45:10 GMT
Content-Type: application/json
X-Ratelimit-Limit: 300
X-Ratelimit-Remaining: 0
Content-Language: cy
X-Ratelimit-Reset: 1416310586

{
    "success": false,
    "errors": ["403 Forbidden: Rydych chi wedi mynd dros eich cyfyngiad nifer yr alwadau yr awr"]
}
```

------

# Moses SMT Machine Translation Online API
This repository's machine translation capabilities are available also online from our API Centre [please see: https://api.techiaith.org/](https://api.techiaith.org). 
The API works using HTTPS GET, meaning you can use it with any programming language/software package of your choice which works over HTTP.

## Tutorials

[Tutorial 1](demo1.md) is an example of how to use the Moses SMT Machine Translation Online API to translate text.



## Current Version

Currently, there is only one version of the Moses SMT Machine Translation Online API available: v1 or 'version 1'.
The version used for the request is returned in the JSON result.

## Schema

The connection to the API is over HTTPS only, from the domain `api.techiaith.org/translate`. All data sent to and received from the API is in JSON ([unicode-escaped ASCII](http://tools.ietf.org/html/rfc5137))

## API Parameters

| Parameter     | Description | Notes |
|--------------|------------|----------|
| `api_key`    |  Your API key, from the API Centre (https://api.techiaith.org) | required |
| `q`       | The text to be translated. Formatted according to RFC 3986 (percent-encoded)  | required |
| `engine` | The name of the engine to be used for translation.  Choices are :  `CofnodYCynulliad` or `Deddfwriaeth` | required |
| `source` | The source text's language. Choices are `en` or `cy`. | required |
| `target` | The target language for any translations returned by the API.  Choices are `en` or `cy`. | required |
| `callback`   | Name of the function to wrap the response in for a JSON-P callback (see below)  | optional |


### Example

```
$ curl https://api.techiaith.org/translate/v1/translate?api_key=123&q=Will+the+Minister+make+a+statement&engine=CofnodYCynulliad&source=en&target=cy

{
    "success": true,
    "translations": [
        {"translatedText": "A wnaiff y Gweinidog wneud datganiad"},
    ],
    "version": 1
}
```

## JSON-P Callbacks

You can use the API with JSON-P callbacks by adding the parameter `callback` to your request:

```
$ curl https://api.techiaith.org/translate/v1/translate?api_key=123&q=Will+the+Minister+make+a+statement&engine=CofnodYCynulliad&source=en&target=cy&callback=foo
foo({
	"success": true,
	"translations": [
		{"translatedText": "A wnaiff y Gweinidog wneud datganiad"},
	],
    	"version": 1
});
```


## Rate Limiting

The API has a limit on the number of requests you can make per hour, linked to your API key. If you would like to increase the number of requests you can make to the API per hour, use the form within the 'API Centre'.

You can view the number of requests you have made/have remaining at any time by looking at the 'HTTP headers' of any response to the API:

```
$ curl -i https://api.techiaith.org/translate/v1/translate?api_key=123&q=Will+the+Minister+make+a+statement&engine=CofnodYCynulliad&source=en&target=cy                                                           

HTTP/1.1 200 OK
Date: Mon, 17 Nov 2014 14:41:21 GMT
Content-Type: application/json
Content-Language: cy
X-Ratelimit-Remaining: 276
X-Ratelimit-Limit: 300
X-Ratelimit-Reset: 1416237399
```

The headers contain all information you may require:

| Header Name | Description |
|--------------|------------|
| X-RateLimit-Limit | Maximum number of requests you can make per hour (rate limit) |
| X-RateLimit-Remaining | The number of requests remaining in the current rate limit window |
| X-RateLimit-Reset | The time at which the current rate limit window resets in [UTC epoch seconds](http://en.wikipedia.org/wiki/Unix_time) |


If you need the time in a different format, any modern programming language can get the job done. For example, if you open up the console on your web browser, you can easily get the reset time as a JavaScript Date object.

```javascript
new Date(1416237399 * 1000)
Date 2014-11-17T15:16:39.000Z
```

Once you go over the rate limit you will receive an error response:

```
$ curl -i curl https://api.techiaith.org/translate/v1/translate?api_key=123&q=Will+the+Minister+make+a+statement&engine=CofnodYCynulliad&source=en&target=cy

HTTP/1.1 200 OK
Date: Tue, 18 Nov 2014 10:44:37 GMT
Content-Type: application/json
X-Ratelimit-Limit: 300
X-Ratelimit-Remaining: 0
Content-Language: en
X-Ratelimit-Reset: 1416310586

{
    "success": false,
    "errors": ["403 Forbidden: You have exceeded your request limit"]
}
```
