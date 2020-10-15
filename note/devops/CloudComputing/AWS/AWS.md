---
layout: page
exclude: true
title: aws
---

You can **find exam white papers / curriculum** by going to the landing page for the "AWS Certified Cloud Practitioner" page then going to `AWS Certification -> Exam Preparation` then expanding the `+` on "Foundational-level AWS Certification" and expanding the `Read AWS whitepapers and FAQs`.

## Services

For the **purposes of the Cloud Practitioner Exam** you need to know about the following services offered by AWS:

- AWS Cost Management
- Security, Identity & Compliance
- Databases
- ~~Network & Content Delivery~~
- Storage
- ~~Migration & Transfer~~
- Compute

*Crossed out services are still technically required but less important*.

## AWS Global Infrastructure

AWS Infrastructure is structured using **regions**, **availability zones** and **edge locations**.

### Availability Zones

An **availability zone** is the equivalent of a data center. It can also be a group of data centers that are geographically co-located, but these are still counted as 1 availability zone.

### Region

A **region** is a **geographical area that contains two or more availability zones**.

There are `GovCloud` regions in North America that are used by the US federal government and private entities. However private entities that use these regions must:

1. Be based on the in US
2. Pass a screening process
3. Only use US citizens or green card holders to hold root access to accounts

**Europe, Middle East and Africa** are all grouped into a **single region**.

### Edge Locations

An **edge location** is a physical AWS endpoint used for caching content from `CloudFront` (Amazon's content delivery network). For example, if I live somewhere far away from an Amazon data center and then download a file from the other side of the world, it can take a long time, however, for future access Amazon will cache this file at an **edge location** for easy access in the future.

There are **always more edge locations than regions**.

### Choosing AWS Region

There are three main factors to consider where choosing an AWS region for your service:

- **Data Sovereignty laws**: where does the data needs to reside legally?
- **Latency to end users**: where are the majority of your customers located?
- **Availability of AWS Services**: US-East-1 is the primary AWS region and is always the first to get new features, which are then released in other regions. The newest services are always available in Northern Virginia.


## AWS Support Packages

There are **four tiers of support package**:

- **Basic** - Free
- **Developer** - $29 a month (12-24 support turn around)
- **Business** - $100/month 
- **Enterprise** - $15,000/month (Gives access to a TAM - Technical Amount Manager)

## CloudWatch

You can **access CloudWatch** in `Services -> Management and Governance -> CloudWatch`.

You can **create a billing alarm** by:

1. Going to `Alarm (Left Menu) -> Billing` on the CloudWatch landing page
2. Click o *LOWER* `Create Alarm` button.





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
eyJoaXN0b3J5IjpbLTIwMTczMTcyODQsLTg3MDQ2NjQwLC00Mj
Y2NzEzNTcsLTE2NDY5ODIzNjgsLTQ5Mjc1ODEzNCwtMjIyNDI2
NDc5LDYyNDU5NDUwOV19
-->