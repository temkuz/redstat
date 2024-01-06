redload
---

# Content

- [Description](#description)
- [Usage](#usage)
    - [Get help](#get-help)
    - [Download user info](#download-user-info)
    - [Download subreddit info](#download-subreddit-info)
    - [Custom output file](#custom-output-file)

# Description

Cli tool for download statistic about user/subreddit

# Usage

## Get help

```commandline
redload -h
```

Output

```commandline
usage: redload [-h] [-of OUTPUT_FILE] [-v] name

Cli tool for download statistic about user/subreddit

positional arguments:
  name                  user/subreddit name. User starts with 'u/' subreddit 'r/'

options:
  -h, --help            show this help message and exit
  -of OUTPUT_FILE, --output_file OUTPUT_FILE
                        output file (default: 'result.json')
  -v, --verbose         verbose output
```

## Download user info

```commandline
redload u/$USERNAME
```

You got `result.json` file with information about `$USERNAME`

## Download subreddit info

```commandline
redload r/$SUBNAME
```

You got `result.json` file with information about `SUBNAME`

# Custom output file

You can change output file from `result.json` to your need

```commandline
redload u/$USERNAME -of $OUTPUT_JSON_FILE
```

or 
```commandline
redload u/$USERNAME --output_file $OUTPUT_JSON_FILE
```