export HOST=http://localhost
export PORT=5000
export DATE=`date +%Y-%m-%d`

curl $HOST:$PORT/users/$DATE
