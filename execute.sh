sudo systemctl start mongod

IP=$(ip addr show |grep -w inet |grep -v 127.0.0.1|awk '{ print $2}'| cut -d "/" -f 1)

uvicorn main:app --reload --host $IP
