
#!/bin/bash
# Displays the body of the response of a curl POST request
curl -s  -X POST -d "email=test@gmail.com"&"subject=I will always be here for PLD" "$1"

