 #!/bin/bash 
function delpyc {
find .. -name "*.py[co]" -delete
find .. -type d -name __pycache__  -delete
}

if [ "$1" == "delpyc" ]; then
    delpyc
fi