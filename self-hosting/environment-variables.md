---
description: List of environment variables available and how to set them.
---

# Environment variables

Fief server relies heavily on environment variables for configuration. You'll likely need to adjust those settings for your deployment.

## Reference

### General

| Name         | Description                                                                                    | Default     | Allowed values                   |
| ------------ | ---------------------------------------------------------------------------------------------- | ----------- | -------------------------------- |
| ENVIRONMENT  | Name of the deployment environment                                                             | development | development, staging, production |
| LOG\_LEVEL   | Log verbosity                                                                                  | DEBUG       | DEBUG, INFO, WARNING, ERROR      |
| ROOT\_DOMAIN | Root domain where your server will be runnin. Mainly used for generating workspace subdomains. | localhost   |                                  |

* `ENVIRONMENT`: Name of the deployment environment
  *

