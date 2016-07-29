web: python runserver.py -a "$AUTH_SERVICE" -u "$USERNAME" -p "$PASSWORD" -l "$LOCATION" -st $STEP_COUNT -H 0.0.0.0 -P $PORT -k $GMAPS_KEY $EXTRA_ARGS 
worker: python runserver.py -a "$AUTH_SERVICE" -u "$USERNAME" -p "$PASSWORD" -l "Sydney Opera House, Australia" -k $GMAPS_KEY $EXTRA_ARGS -st 15 -t 5 -sd 3 -ns
