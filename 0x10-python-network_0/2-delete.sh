#!/bin/bash
# Bash script that sends a DELETE request to the URL passed
#curl -sX DELETE "$1"
URL=$1

reply=$(curl -X DELETE -s -w "%{http_code}" $URL)
http_reply_status=${reply:(-3)}
reply_body=${reply:0:${#reply}-3}
echo "I'm a DELETE request$reply_body"
