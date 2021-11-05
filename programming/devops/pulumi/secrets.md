---
title: Secrets
layout: page
exclude: true
---

You can **update the passphrase for a stack** by using the `change-secrets-provider` flag on the `stack` command followed by the `passphrase` provider. This indicates that you want to update the *local* provider that uses a passphrase rather than using any remote providers. You also need to have a stack `select`ed for this to work.
```bash
pulumi stack change-secrets-provider passphrase
```

You can **configure stack passphrases in your environment variables** using the `PULUMI_CONFIG_PASSPHRASE` variable. This *can* be an empty string but its not recommended.
```bash
export PULUMI_CONFIG_PASSPHRASE=<YOUR_PASSPHRASE>
```