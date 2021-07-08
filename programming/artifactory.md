---
title: Artifactory
layout: page
exclude: true
---

## Rest API

You can **search artifactory repositorities by name** using the `/search/artifact` path with the `name` property.
```
GET https://artifactoryurl/api/search/name=<ARTIFACT_NAME>
```