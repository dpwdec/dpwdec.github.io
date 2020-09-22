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

You can **define a route for an entire controller** by using the `[Route]` attribute before a controller class definition with an argument of the route name as a string.
```csharp
[Route("api/")
public class UsersController : Controller { ... }
```

You can **create controller routes with dynamically generated route names** by using `[controller]` in the route string argument and following the naming convention of appending the word `Controller` to the end of your controller classes. When the route is processed this will use the class name *before* the `Controller` keyword as a replacement for `[controller]` inside the `[Route]` attribute argument string. In the example below the result of the string argument to `[Route]` would be `"api/users"`. This is useful as it can dynamically update routing information based on class names.
```csharp
[Route("api/[controller]")
public class UsersController : Controller { ... }
```

You can **define response methods for a controller** by creating methods with `ActionResult` as there return type. The **`ActionResult` should return type information for the expected response type** from the controller method. You must also use `Http` decorators to specify which HTTP verbs that different controller methods respond to. The example shows that the `UsersController` will be available at the `"api/users"` route, using the `[HttpGet]` attribute no further routing information needs to be supplied (although it can be!) and the `"api/users"` route will respond to a `GET` request with an `IEnumerable` of `User` objects to return data.
```csharp
[Route("api/users")
public class UsersController : Controller 
{
  [HttpGet]
  public ActionResult<IEnumerable<User>> GetUsers() { ... }
}
```

You can **define further routing information using HTTP verb attributes** by adding the route as a string argument to the attribute.
```csharp
[Route("api/users")
public class UsersController : Controller 
{
  [HttpGet("age")]
  public ActionResult<IEnumerable<int>> GetUserAges() { ... }
}
```

You can **define dynamic URLs with the HTTP verb attributes** by enclosing the argument to the attribute in `{}` curly brackets. *This name is then passed into the method that calls it as an argument of the same name???* The defined URL below would direct to `api/users/{id}` which would be replaced by the specific id of the user.
```csharp
[Route("api/users")
public class UsersController : Controller 
{
  [HttpGet("{id}")]
  public ActionResult<User> GetUser(int id) { ... }
}
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
eyJoaXN0b3J5IjpbLTIyMDU1ODYzNCwtMzI2NTUyMzIsLTM0NT
czMjMwMCw0NDM0NTM4MTAsMTQwNTkxMjIyNCwxNTU2MTE4NTk4
LDEzNTI0ODQ2MDUsLTE2MjgxNjIyMTcsMTkzNTI1MTc2NiwxMz
g0MDg3MjA2LC02Mzg0MzUwMzddfQ==
-->