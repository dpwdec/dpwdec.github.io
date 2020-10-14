---
layout: page
exclude: true
title: aws
---

You can **find exam white papers / curriculum** by going to the landing page for the "AWS Certified Cloud Practitioner" page then going to `AWS Certification -> Exam Preparation` then expanding the `+` on "Foundational-level AWS Certification" and expanding the `Read AWS whitepapers and FAQs`.

## Cloud Computing

Cloud computing is **on-demand delivery of compute, database storage and applications via the internet**. Essentially you are **just renting someone else's computer**.

The **advantages of cloud computing**:

1. **Trade capital expense for variable expense**

## Instance Types

### T

Instances that start with a `T` are **small size instances**. The `T` unofficially stands for throttled, when too much traffic comes through then the instance will have its throughput throttled.

## Previewing Applications

AWS's official local host previewing documentation can be found [here][awsPrevDocs]. Y

ou can use a **local host** server in aws by setting the locahost output port to `8080`. When running a server on this port aws will notify you with a link to the local hosted url and port to access the page.

[awsPrevDocs]: https://docs.aws.amazon.com/cloud9/latest/user-guide/app-preview.html

Aws will not always give you correct feedback on local host deployment, launching error messages even when the server is running correctly. You can check by **manually visiting the localhost url**. This url takes the form of `[unique EC2 instance id].vfs.cloud9.[region].amazonaws.com`. You can find your unique EC-2 instance id by going to `services --> EC-2 --> running instances` and copying the long string of numbers and letters displayed after `Environment-` in the "instance:" section. You can find the correct region extension in the `availability zone` section, this takes the format `eu-west-2c`.

Any **url extensions** wil got be appended to this url.

### Rails
When making a rails app you should use amazon's Ubuntu server distribution rather than the Amazon Linux EC-2 version. I don't really understand the reason for this but it has to do with the installation of different dependencies such as SQLite and WebPacker and how they rely on each other. In any case, on Amazon Linux getting a clean install is very difficult but things mostly just work if you use the Ubuntu distribution.

This [post][soWebp] covers how to install `webpacker` and get the basics of a rails server installed.

[soWebp]: https://stackoverflow.com/questions/57891751/webpacker-configuration-file-not-found-rails-6-0-0

To set up a rails server to work on aws' `localhost` go to the `config/environments/development.rb` and add the following code to the bottom of the `development.rb` file just before the `end` keyword.

```ruby
config.hosts << "URL_OF_YOUR_EC2_INSTANCE"
```
 
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTIxMTYyMTY3NSwtMzA1MzM1NTU1LC0xND
ExMzg3ODE3LC0yNTE5NTQ3MTUsLTc3MjIxNjA3OSwtMTcxNTQ2
MzkyNF19
-->