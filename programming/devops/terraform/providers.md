---
title: Providers
layout: page
exclude: true
---

Providers are plugins to the terraform API that **allow you to interact with cloud providers and other APIs or platforms**.

The default terraform install does not come bundled with *all* provider plugins. Instead terraform will download and install the necessary provider plugins on a per project basis according to the file's configuration.

You can **define a provider** by using the `provider` indicator followed by a string with the provider name. The config inside the provider block is a key-value form of configuration information.
```terraform
provider "<PROVIDER_NAME>" {
    # provider config
}
```

## AWS

You can **define the AWS provider** using the `"aws"` provider name. The only required configuration property is the AWS `region`.
```terraform
provider "aws" {
    region = "eu-west-1"
}
```

You can **configure access credentials for an AWS provider**. You can also **add an optional session token** using the `token` key.
```terraform
provider "aws" {
    region = "eu-west-1"
    access_key = "<ACCESS_KEY>"
    secret_key = "<SECRET_KEY>"
    token = "<SESSION_TOKEN>"
}
```