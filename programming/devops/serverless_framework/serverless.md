---
title: Serverless
layout: page
exclude: true
---

## Deployments

You can **limit deployment to a specific serverless function** by using the `-f` flag and the function name when deploying. This can be useful if you only make change to one part of a serverless application composed of a host of lambdas and only want to redeploy an individual function as opposed to the entire application.
```bash
serverless deploy -f myFunction
```