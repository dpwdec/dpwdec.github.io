---
title: Publish
layout: page
exclude: true
---

## Single File Binary Publishing

You can **publish a dotnet project as a single file self-contained binary** by using the `publish` command in conjunction with the `PublishSingleFile` property set to true and the `--runtime` flag specified to the OS you want to deploy on. In tht example below it is the `PublishSingleFile` that actually causes the publisher to package the binary into a single self-contained file.
```bash
dotnet publish -r <PLATFORM> -c release -o <OUTPUT_PATH> -p:PublishingSingleFile=true
```

For example a **self-contained single file linux deployment** would be
```bash
dotnet publish -r linux-x64 -c release -o deploys/out -p:PublishingSingleFile=true
```

## Runtime

You can **set the deployment runtime** with the `-r` or `--runtime` flag. If this is not set it will default to the operating system you are developing on.

The platform value for targeting different operating systems can be
- `win-x86`
- `win-x64`
- `linux-x64`
- `osx-x64`

## Self-contained and Framework-dependent applications

There are two types of application deployments:
- self-contained: *applications have the entire .NET runtime and any dependency libraries bundled with it*
- framework-dependent: *applications have a cross platform `.dll` binary that can run on any system and a platform specific entry point*

It's important to note that **a self-contained application is NOT the same as a single file application**. The `--self-contained` flag is set to `true` by default. This will create a deploy that still has all the individual `.dll` files even though the entire application is self-contained and does not require the .NET run time to work. You can still set `--self-contained` to `true` for semantic significance or to combat other configuration changes in the future.

You can **deploy a framework-dependent binary** by specifying `--self-contained` as `false`.
```bash
dotnet publish --self-contained false
```

## Ready to Run applications

You can **improve run time speed with ahead-of-time (AOT) compilation** by using the `PublishReadyToRun` property. This substantially increases the size of the binary but can improve run time especially for large applications. It's not advisable to use this for small applications.
```bash
dotnet publish -p:PublishReadyToRun=true
```

## Trimmed applications

You can **trim the size of self-contained applications** by using the `PublishTrimmed` property. This will result in a substantially reduced binary size. This will strip out uneeded parts of the .NET runtime, however, its deemed an unstable feature and can cause issues when depdencies are not clearly indicated at runtime or when reflection is used. It's also possible to configure options for the trimming in the project file.
```bash
dotnet publish -p:PublishTrimmed=true
```

## Native Libraries

The `IncludeNativeLibrariesForSelfExtract` is used to make `5.x` .NET application to behave the same as a `3.x` application. When a `3.x` .NET application starts it creates a temporary extraction folder that it runs code out of, where as `5.x` applications load that code into memory. This `IncludeNativeLibrariesForSelfExtract` simply makes the `5.x` deploy behave the same as the `3.x`.