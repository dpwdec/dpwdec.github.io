---
title: ASP
layout: page
exclude: true
---

## Project

You can **access your project's configuration file** which is found in the corresponding project's `.csproj` file by going to the project file in the solution browser, then `RMB (on Project) -> Edit Project File`.

If you **add a NuGet package or dependency** this will be reflected in the project's `.csproj` file with an `ItemGroup` with a `PackageReference` specifying the project's dependencies.
```xml
<ItemGroup>  
  <PackageReference  Include="SomeDependency"  Version="x.x.x"  />  
</ItemGroup>
```

You can **configure how your web application runs** such as the *port* it runs on, or its *environment variables* using the `priopreties/launchSettings.json` file in your project.

You can **set environment variables** using the `environmentVariables` section of the `launchSettings.json` file for the profile that you are running your application on.
```json
"environmentVariables": {
  // environment variables here
}
```

You can **set the application environment as development** by assigning the `ASPNETCORE_ENVIRONMENT` variable to `Development` in the `environmentVariables` section of the `launchSettings.json` file.
```json
"environmentVariables": {
  "ASPNETCORE_ENVIRONMENT": "Development"
}
```

You can **configure other settings for your project** such as database connection strings etc. from the `appsettings.json` file, there is also an `appsetttings.Development.json` for settings specific to the development environment.

You can **define different profiles here with which to run your application** which change how the application is built and operated when developing. For example you may want to define a *debug* profile with specific variables to debug an application, or you may want to develop something using a *release-like* profile.

You should **store static files for your website** in the `wwwroot` folder within your project. This contains static dependencies like `JavaScript` and `CSS`.

Like other .NET programs ASP applications **start running from the `Main` method** in the `Program` class. Generally this use a `Startup` class to build and then run the application.

You can **configure you project's routing pipeline, middleware and services** from the `Startup` class. The `Configure` method is used from controlling how middleware and requests function in your application and the `ConfigureServices` method is used for registering and configuring new services to work with the application.

### ConfigureServices

You can **specify the mapping of an injection of the concrete instances of interfaces as dependencies for a class at start up** using the `ConfigureServices` method of the `StartUp` class with the `services` object. This mapping takes the interface name and the concrete implementation as type arguments, then whenever that interface is required as a dependency it will provide the concrete implementation.

Dependencies can be **provided using three different that change the properties of the concrete instance**, these are:

 1. `AddSingleton` which always provides the same object no matter what the request is
 2. `AddScoped` which provides a different object per client request
 3. `Transient` which provides new instance every time one is requested

You can **create a new mapping** by using the `services` object inside the `ConfigureServices` method with one of the above methods and adding the from and to mappings as types.
```csharp
services.AddScoped<IMyInterface, MyInterfaceImplementation>();
```

## Controllers

You should **make a controller for each resource type in your project**, that being, each distinct model in your database that makes up your system.

You should **name your individual controllers after a pluralised form of the resource they refer to** followed by the word `Controller`. For example, if our resource was a `User` table then the associated controller would be named `UsersController.cs`.
```yaml
Controllers
├── AddressesController.cs # controller for the Address model
├── PeopleController.cs # controller for the Person model
└── UsersController.cs # controller for the User model
```

You can **create a new minimal controller** (ideal when just creating an API) by inheriting from the `ControllerBase` class from the `Microsoft.AspNetCore.Mvc`. This class provides a minimal controller without specific assumptions about the "view" that your application might take.
```csharp
// ControllerBase for APIs without views
using using  Microsoft.AspNetCore.Mvc;

public class MyController : ControllerBase { ... }
```

You can **create a fully featured controller** with view support by using the `Controller` class from `Microsoft.AspNetCore.Mvc`.
```csharp
// General Controller for web apps WITH views
using using  Microsoft.AspNetCore.Mvc;

public class MyController : Controller { ... }
```

You can **define a route for an entire controller** by using the `[Route]` attribute before a controller class definition with an argument of the route name as a string. The `/` extension on the controller route is implicit.
```csharp
[Route("api/")
public class UsersController : Controller { ... }
```

You can **create controller routes with dynamically generated route names** by using `[controller]` in the route string argument and following the naming convention of appending the word `Controller` to the end of your controller classes. When the route is processed this will use the class name *before* the `Controller` keyword as a replacement for `[controller]` inside the `[Route]` attribute argument string. In the example below the result of the string argument to `[Route]` would be `"api/users"`. This is useful as it can dynamically update routing information based on class names.
```csharp
[Route("api/[controller]")
public class UsersController : Controller { ... }
```

### Methods

You can **define response methods for a controller** by creating methods with `ActionResult` as the return type. The **`ActionResult` should return type information for the expected response type** from the controller method. You must also use `Http` decorators to specify which HTTP verbs that different controller methods respond to. The example shows that the `UsersController` will be available at the `"api/users"` route, using the `[HttpGet]` attribute no further routing information needs to be supplied (although it can be!) and the `"api/users"` route will respond to a `GET` request with an `IEnumerable` of `User` objects to return data.
```csharp
[Route("api/users")]
public class UsersController : Controller 
{
  [HttpGet]
  public ActionResult<IEnumerable<User>> GetUsers() { ... }
}
```

You can **define further routing information using HTTP verb attributes** by adding the route as a string argument to the attribute. Again, this further routing information has an implicit `/` as an extension to the route.
```csharp
[Route("api/users")]
public class UsersController : Controller 
{
  [HttpGet("age")]
  public ActionResult<IEnumerable<int>> GetUserAges() { ... }
}
```

You can **combine the `[Route]` and `[HttpX]`** attributes. For example, the `"age"` controller route extension from above is rewritten below to use a combination of the RESTful verb and a route extension.
```csharp
[Route("age")]
[HttpGet]
public ActionResult<IEnumerable<int>> GetUserAges() { ... }
```

You can **define dynamic URLs with the HTTP verb attributes** by enclosing the argument to the attribute in `{}` curly brackets. This wildcard extension to the route is then passed into the decorated method as an attribute of the same name. The defined URL below would direct to `api/users/{id}` which would be replaced by the specific id of the user, then because the actually method takes an argument called `id`, then attribute knows to pass the result of this into that method as an argument when the API is triggered.
```csharp
[Route("api/users")
public class UsersController : Controller 
{
  [HttpGet("{id}")]
  public ActionResult<User> GetUser(int id) { ... }
}
```

You can **chain wildcard arguments** and they will generalise to multiple controller method input arguments.
```csharp
[HttpGet("{id}/{name}")]
public ActionResult<User> GetUser(int id, string name)
{
  // both id and name will be picked up as arguments from the URL
}
``` 

### API endpoint returns and status codes

You can **return an `ActionResult` from an API endpoint with a status code** by using the status code methods that are part pf `AspNetCore`. In the example below the `Ok` method wraps the result of getting the list of all `User`s in an `ActionResult` and returns it with a `200` status code.
```csharp
[HttpGet]
public ActionResult<IEnumerable<User>> GetUsers()
{
  return Ok(GetAllUser());
}
```

It also seems like `ActionResult` automatically formats an objects into JSON.

You can **return a specific status code in isolation** by using the `StatusCode` method and the status code you want to return as an argument. It also seems to return the `ActionResult` object.
```csharp
[HttpGet]
public ActionResult<string> ReturnInternalServerError()
{
  return StatusCode(500);
}
```

You can **return messages inside with your status code responses** by submitting a secondary argument to the `StatusCode` function. Similar to functions like `Ok`, the `StatusCode` will format objects into JSON.
```csharp
public ActionResult<string> GetMessage()
{
  return StatusCode(200, "This is a message");
}
```

You can **specify the status codes argument using semantically significant predefined constants** from the `StatusCodes` section of `Microsoft.AspNetCore.Http` library. For example, the `500` status code above can be aliased to `Status500InternalServerError` as part of this library.
```csharp
return StatusCode(StatusCodes.Status500InternalServerError);
```

## Binding Sources

## Controller Results

Controllers `return` concrete instances of `IActionResult` when they complete. These can indicate a range of actions such as `Ok` results with data or `Redirect` results to other addresses. Importantly **controller results are distinct from HTTP return objects**, they [do not contain status codes][nostatus] until later when they have been processed by the request pipeline.

[nostatus]: https://stackoverflow.com/a/50989283

### IActionResult

`IActionResult` is the interface which `ActionResult` implements.

### ActionResult

You can **get the value from a successful `ActionResult`** by destructuring the object into an `OkObjectResult` and then destructuring it again into the expected value. The example below demonstrates a controller route that contains a string,  unfortunately **casting must be done between the `ActionResult` and `OkObjectResult`** to successfully destructure the object with the `Result` and `Value` properties.
```csharp
ActionResult<string> actionResult = MyController.MyRoute();
OkObjectResult okObject = (OkObjectResult) actionResult.Result;
string result = (string) okObject.Value;
```

### Ok (200)

You can **implicitly return a `204` from a controller route** by returning an `Ok` response `ActionResult` that contains nothing.
```csharp
public ActionResult<string> NoContentRoute()
{
  var message = null;
  return Ok();
}
```

### Not Found (404)

You can **return a `404` status code** by returning a `NotFound` response `IActionResult` object.
```csharp
public IActionResult NotFoundRoute()
{
  return NotFound();
}
```

### ForbidResult

You can **return a `ForbidResult`** from a controller by using the `Forbid()` method, this is used for `403` type responses. The `ForbidResult` class inherits from `ActionResult`.
```csharp
[HttpGet]
public IActionResult ForbiddenRoute()
{
  return Forbid();
}
```

## Internal Domain Models and Data Transfer Objects

**Sending back data directly from a class implementation** is **not recommended** because it couples the internal implementation of a class and its data with external access.

This causes problems because **if you want to change the internal implementation of your codes structure** this will impact the way APIs return data to clients which will potentially cause many problems.

Essentially, your **internal implementation should be decoupled from data that is sent and received**.

A solution to this is a **Data Transfer Object** (DTO) which is a representation of your internal data structures for external use. For example, if our system implements a class called `User` which has a number of properties, such as `Name`, `DateOfBirth`, `Height` etc. and the type formats that those are stored in and any other database specific or data processing methods, we would not want to expose this directly to parts of your application that send and receive data, because we might want to return the User's age instead of their `DateOfBirth` directly, for this we would create a DTO that mirrors the structure of the internal `User` implementation for the purposes of this data transfer. Furthermore we may also not want to expose clients to database specific information like the `Id` of a `User` record, which could also be omitted into the DTO mapping.

### DTO Classes

You can **create a new DTO** by defining a class with only the fields that you want to return to a client. For example if our user model was defined as below, with the `Id`, `Name`, `Height` and `DateOfBirth` fields.
```csharp
public class User
{
  public int Id { get; set; }
  public string Name { get; set; }
  public int Height { get; set; }
  public Date DateOfBirth { get; set; }
}
```

Then a corresponding DTO might have a structure like the example below, with `Name`, `Height` and `Age` fields. It's a general **convention to name a DTO in the format `<SOURCE CLASS><INTENDED ACTION>Dto`**. So, the DTO defined below is for the purpose of a client `Read`ing information. However, we might define DTOs for writing information to our database etc.
```csharp
public class UserReadDto
{
  public string Name { get; set; }
  public int Height { get; set; }
  public int Age { get; set; }
}
```

### Profiles

You can **define a mapping between a DTO and a real class** by using the `AutoMapper` library and creating a class that extends `AutoMapper`'s `Profile` class to define a mapping. You then define the `Profile` class' constructor to use `AutoMapper`'s `CreateMap` function with types between its `<>` angle brackets with the class you're mapping from as the first type argument and the class you're mapping two as the second type argument.
```csharp
using AutoMapper;

public class UserProfile : Profile
{
  public UserProfile()
  {
    CreateMap<User, UserReadDto>();
  }
}
```

`AutoMapper` will **automatically map fields of the same name and type in the source class to the target DTO** *and* **remove fields not present in the DTO**.

### Mapping

You can **convert an instance of a model to an instance of a DTO in a controller route** by using an object that implements that `IMapper` interface. This interface contains a method called `Map` which takes an instance of a model class with real data its argument and the DTO to map to as its type argument.

You can **insert an instance of `IMapper` into your controller class** using dependency injection. `IMapper` is **automatically dependency injected**.

**Controller routes** will also need to **return a DTO** instead of a model object directly.
```csharp
[Route("api/route")]  
[ApiController]
public class MyController : ControllerBase
{
  private readonly IMapper _mapper;
  public MyController(IMapper mapper)
  {
    _mapper = mapper;
  }

  [HttpGet("{id}")]
  public ActionResult<UserReadDto> GetData(int id)
  {
    var userData = Database.GetUserById(id);
    return Ok(_mapper.Map<UserReadDto>(userData));
  }
}
```

`IMapper` has built in support to allow you to **`Map` an `IEnumerable` collection of model instances to a collection of DTO instances**.
```csharp
[HttpGet]
public Acti
```

## Uri

You can **store URIs with predefined utilities** by using the `Uri` class. This is *not* part of `ASP` specifically, but has good applications in web development. You can **create a new `Uri` object** by passing in your actual uri as a string. You can **pass relative and absolute URIs** into the `Uri` object, if you pass poorly formed URIs this can cause cause errors later with other `Uri` methods.
```csharp
var absoluteUri = new Uri("https://website.com/hello");
var relativeUri = new Uri("/path/to/something");
```

You can **check what kind of URI a URI string is** by using the static `IsWellFormedString` method of the `Uri` class. This takes the URI string and an `UriKind` `enum` for the type of URI and returns a `bool`. Any string that **contains a protocol and a domain** is considered **absolute**, **everything else** is considered **relative**.
```csharp
var absoluteUri = "https://website.com/hello";
var relativeUri = "/path/to/something/"
var badUri = "website.com"
var nonsenseUri = "93480nmfmdsmf*ur"

Uri.IsWellFormedString(absoluteUri, UriKind.Absolute); // => true
Uri.IsWellFormedString(relative, UriKind.Absolute); // => false
Uri.IsWellFormedString(badUri, UriKind.Absolute); // => false
Uri.IsWellFormedString(nonsenseUri, UriKind.Absolute); // => false

Uri.IsWellFormedString(absoluteUri, UriKind.Relative); // => false
Uri.IsWellFormedString(relative, UriKind.Relative); // => true
Uri.IsWellFormedString(badUri, UriKind.Relative); // => true
Uri.IsWellFormedString(nonsenseUri, UriKind.Relative); // => true
```

There is also the option to **check if a URI is absolute or relative** using the `AbsoluteOrRelative` value of `UriKind`. However this might not be very useful.
```csharp
Uri.IsWellFormedString(anyUri, UriKind.AbsoluteOrRelative); // => true
```

 
## Razor Pages

The **primary code** for a razor pages application is contained in the `Pages` directory.

Razor pages contain **both a view and model** for each page. The **view is defined using a `.cshtml`file**, and the **model is defined using a standard `.cs` file**. The **naming convention for the model files** is to use `.cshtml.cs`. The example below shows the view and model files together as they appear in a razor pages file structure.
```
index.cshtml
└── index.cshtml.cs
```

To **createa a new razor page** it **must inherit from the `PageModel` class**. This is **imported** by `using Microsoft.AspNetCore.Mvc.RazorPages`.
```csharp
using Microsoft.AspNetCore.Mvc.RazorPages;

public class MyModel : PageModel
{
  // page model here
}
```

You can **specify the model that a page should use** by using the `@model` keyword in the corresponding `.cshtml` file.
```html
<!-- Index.cshtml -->
@model IndexModel

<h1>Hello!</h1>
```

### Shared

You can **create layout and page partials** in the the project's `Pages/Shared` folder. The **naming convention for these files** is to start with an `_` underscore, such as `_Layout.cshtml`. 

You can **define the master layout for your application** by using the `_ViewStart.cshtml` file and setting the `Layout` variable equal to the name of the partial you want to use from your `Shared` folder.
```csharp
@{
  Layout = "_Layout";
}
```

<!--stackedit_data:
eyJoaXN0b3J5IjpbLTI0MTU3NDQzNiwxNDAzODg4MDg1LDEwMj
IxMDIwNTYsNzkwNTQwODQwLDEyNTMwNDYyNzksODc2MTUzNzcz
LC0yMTA3ODI2NTQ0LDEzNzkyODExMzgsMTMxNzg4NDcwNiwxNT
cwNjg4NzcyLC0yMDMzNjUyODE0LC0xMDY1MzA0MTcxLDY1OTAw
NTMyMiwtMTM5NjQ1MTUyLC04ODE1MDUxOTQsMTcwMjk1OTI0NS
wyMzk4ODM5NzcsLTQzNTY3NDI4NSwxMDAxNjk5ODM3LC01NDI0
NzExMTBdfQ==
-->