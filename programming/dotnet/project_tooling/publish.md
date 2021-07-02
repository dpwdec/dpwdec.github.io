---
title: Publish
layout: page
exclude: true
---

## Single Binary Publishing

You can **publish a dotnet project as a single self contained binary** by using the `publish` command in conjunction with the `--self-contained` flag and the `PublishSingleFile` property set to true.
```bash
dotnet publish --self-contained -r <PLATFORM> -c release -o <OUTPUT_PATH> -p:PublishingSingleFile=true
```

The platform value for targeting different operating systems can be
- `win-x86`
- `win-x64`
- `linux-x64`
- `osx-x64`

For example a **self contained linux deployment** would be
```bash
dotnet publish --self-contained -r linux-x64 -c release -o deploys/out -p:PublishingSingleFile=true
```