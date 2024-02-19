# Introduction

Fief is what is usually called an **identity provider**: it provides and secures user identities to external apps.

To allow this, Fief implements the [OpenID Connect](https://openid.net/connect/) protocol, an identity layer on top of the well-known [OAuth2 protocol](https://oauth.net/2/). Basically, it describes a secure way for a user to give access to its data to an external app.

So, how does everything will fit together? In a nutshell, **Fief** will store everything about your users data (email address, hashed passwords...) and give you a simple way to authenticate them in your application.

``` mermaid
graph TD
    U((User))
    A{Your application}
    subgraph FIEF [Fief]
        F[Fief API]
        FL[Login page]
        FD[(Fief database)]
    end
    U -- is not authenticated ----> FL
    U -- is authenticated ----> A
    A -- checks user identity on --> F
    FL -. redirects to .-> A
    F -- stores users on --> FD
```

## Let's get started!

The first thing to do is to start your Fief instance on your machine!
