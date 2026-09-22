---
title: "How to Fix a Broken Flask Application after SQLAlchemy Update"
date: 2021-03-16T15:33:05
categories: ["Tuts"]
tags: ["tutorial"]
image: /assets/uploads/2021/03/sqlalchemy_docker_update_error.jpg
---

I was working on my website and while everything was running smoothly on my Docker instances, suddenly the newly deployed Docker images were returning errors.

My application is using Flask and communicating with a PostgresQL database using SQLAlchemy. Pretty standard solution which had no issue at all, till yesterday. When a valid page was requested the following error was shown.

```generic
sqlalchemy.exc.NoSuchModuleError: Can't load plugin: sqlalchemy.dialects:postgres
```

What I got out of it was that for some reason the application could not contact with the Database. So I checked the code to verify that there was no major change and I was wrong, because SQLAlchemy released their version 1.4 which changes a lot of things. This was breaking the application. The solution to that was to specify in `requirements.txt` that I do not want version 1.4, but an older version.

```generic
SQLAlchemy<1.4
```

After this change the application is running again without any issues. The next step would be to make the application run normally using SQLAlchemy 1.4+ and not be dependant on older releases.
