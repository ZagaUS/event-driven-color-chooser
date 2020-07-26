![CI](https://github.com/ZagaUS/event-driven-color-chooser/workflows/CI/badge.svg)

# event-driven-color-chooser
The Event Driven Color Chooser is a sample application that demonstrates the usage of AWS to support a real-time event-driven use case. Clients may navigate to the home page and "vote" for the color of their preference. Options are Red, Green or Blue. As clients make their respective selections the API will tally votes; perform rudimentary processing on the "voting" events; then respond to inquiries from the client as to vote totals. Votes are given a limited time to live (TTL), so tallied votes only count for a limited duration.

## Deployment
The Event Driven Color Chooser makes use of the [serverless framework](https://www.serverless.com/). The application is intended to deploy on AWS. Cues as to how you might deploy this application may be found in the github [deployment action](.github/workflows/CD.yml).

For more info on how serverless framework deployments work look [here](https://www.serverless.com/framework/docs/providers/aws/guide/quick-start/)

## API
The Event Driven Color Chooser exposes a WebSocket API. Aside from the standard `connect`, `disconnect` and `default`two api endpoints are exposed. Routing is specified for these in the message payload via the `action` attribute.

#### vote
```
{
    "action": "vote",
    "color": "r"
}
```
Valid color values are "r", "g" or "b". The `vote` endpoint will return a success message if a valid value is specified.
```
{
    "event": "success"
}
```
Or an error message should the client specify an invalid value.
```
{
    "event": "error",
    "message": "invalid vote option"
}
```

#### inquire
```
{
    "action": "inquire"
}
```
The `inquire` endpoint will return a payload containing color selection totals as well as a RGB hexadecimal representation of the selection.
```
{
    "event": "success", 
    "body": "{\"r\": 0, \"g\": 0, \"b\": 0, \"hex\": \"#555555\"}"
}
```

## The tech stack
Everything deploys on AWS, but a quick rundown of the internals is as follows:

- The UI (Client) uses [Ionic](https://ionicframework.com/).
- The [Serverless Framework](https://www.serverless.com) handles the heavy lifting with IaC.
- The application deploys on [AWS](https://aws.amazon.com/).
    - State is managed via [ElastiCache](https://aws.amazon.com/elasticache/) / [Redis](https://redis.io/)
    - [Lambda](https://aws.amazon.com/lambda/) facilitates computation.
    - [API Gateway](https://aws.amazon.com/api-gateway/) facilitates API management.
    - [S3](https://aws.amazon.com/s3/) serves static resources
- [Github actions](https://docs.github.com/en/actions) are used for CI / CD