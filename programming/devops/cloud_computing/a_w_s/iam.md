---
layout: page
exclude: true
title: IAM
---

**Identity Access Management (IAM)** allows you create accounts with access to your AWS instances. IAM is **configured globally for your account**, the region you use does not matter.

You can **access IAM** from the `Services -> Security, Identity & Compliance -> IAM`.

There is a **IAM users sign-in link** which you can send to users to use to sign in. The link name displayed here will default to showing your AWS account number. You **should not share this number with other people**.

You can **customize the IAM sign-in link** by clicking `customize` and creating a custom URL (that is unique to AWS globally).

## Creating IAM User Accounts

You can **create a new user** by going to the `Users` menu item on the left and then selecting `Add User`.

There are **three ways to allow access for IAM accounts**:

1. **Programmatic access**: using the command line
2. **AWS Management Console access**: through a web GUI
3. **SDK Access**

You can **set user permissions** in three different ways:

1. **Adding the user to a group**
2. **Copying permissions from another user**
3. **Setting permissions specific to this user**

## Group Policies

A user that is placed in a group **inherits all the permissions that that group has**. Groups are usually structured around roles, such as Sys Admins, HR or Finance.

To **create a new group**, select a policy to base the group on and then enter a name for the new group then click `Create Group`.

There are a **set of pre-built access policies** managed by Amazon. These have an orange box logo in front of them if they are managed by Amazon.

You can **filter access policies by job function** through the `Filter Policies` drop down which allows you to set policies more appropriately for creating user accounts.

Policies are represented using `JSON`.
```yaml
# example admin policy
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "*", # match all actions
      "Resource": "*", # match all resources
    }
  ]
}
```

## Tags

You can **add tags** as key value pairs which contain meta-data about your IAM user, things like `Employee_Id` or `Department`.

## Password Policy

You can **set a password policy** for IAM users by clicking the `Set Password Policy` from the `Account Settings` menu item on the left.