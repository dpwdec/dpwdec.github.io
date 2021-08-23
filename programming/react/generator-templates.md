---
title: Generator Templates
layout: page
exclude: true
---

You can **display printed output from running the generator** by passing in the `--debug` flag.
```bash
ag --debug ./path/to/asycnapi/data ./path/to/generator/code
```

You can **ignore some of the more irritating requirements of the generator** such as the output folder being empty and changes being committed, by using the `--force-write` flag.
```bash
ag --force-write ./path/to/asycnapi/data ./path/to/generator/code
```

You **can render an array of elements** by wrapping the array in another element. The example below creates an array of `Text` elements and then returns the array of elements inside another `Text` element causing the elements in the array to be templated.
```js
import { Text } from '@asyncapi/generator-react-sdk'

export function MyElement() {
  const elements = [...Array(3)].map((_, index) => {
    return (<Text>{index}</Text>)
  })

  return <Text>{elements}</Text>
}

```