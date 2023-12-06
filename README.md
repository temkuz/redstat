redstat
---

# Content

- [Description](#description)
- [Install](#install)
- [Usage](#usage)
    - [Download module](#download-module)
        - [Help](#default-help)
            - [Subreddit help](#subreddit-help)
            - [User help](#user-help)
        - [Download subreddit](#download-subreddit)
        - [Download user](#download-user)
            - [Download user all data](#download-user-all-data)
            - [Download user comments](#download-user-comments)
            - [Download user posts](#download-user-posts)
        - [Change output file](#change-output-file)

# Description

Tools for working with reddit data without api

# Install

```commandline
pip install redstat
```

# Usage

# Download module

## Default help

```commandline
redload -h
```

Result

```commandline
usage: redload [-h] {subreddit,user} ...           
                                                   
positional arguments:                              
  {subreddit,user}                                 
    subreddit       subreddit parser               
    user            user parser                    
                                                   
options:                                           
  -h, --help        show this help message and exit
```

## Subreddit help

```commandline
redload subreddit -h
```

Result

```commandline
usage: redload subreddit [-h] [-t type] [-o OUTPUT] name

positional arguments:
  name                  subreddit name

options:
  -h, --help            show this help message and exit
  -t type, --type type  types ['all'] default: all
  -o OUTPUT, --output OUTPUT
                        output file
```

## User help

```commandline
redload user -h
```

Result

```commandline
usage: redload user [-h] [-t type] [-o OUTPUT] name    
                                                       
positional arguments:                                  
  name                  reddit username                
                                                       
options:                                               
  -h, --help            show this help message and exit
  -t type, --type type  types ['all', 'comment', 'post'] default: all
  -o OUTPUT, --output OUTPUT
                        output file
```

## Download subreddit

```commandline
redload subreddit $SUB_NAME
```

## Download user

## Download user all data

```commandline
redload user $USER_NAME
```

## Download user comments

```commandline
redload user $USER_NAME -t comment
```

## Download user posts

```commandline
redload user $USER_NAME -t post
```

## Change output file

You can change output file for user and subreddit

```commandline
redload user $USER_NAME -o OUTPUT_FILE.json
```