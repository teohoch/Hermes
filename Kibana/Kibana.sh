#!/bin/bash
PATH=/sbin:/usr/sbin:/bin:/usr/bin
DESC="Kibana 4"
NAME=kibana
DAEMON=/var/www/html/Kibana/bin/$NAME
DAEMON_ARGS=""
PIDFILE=/var/run/$NAME.pid
SCRIPTNAME=/etc/init.d/$NAME
LOG=/var/www/html/Kibana/bin/kibana.log

pid_file_exists() {
    [ -f "$PIDFILE" ]
}

do_start()	{
	
	if pid_file_exists
	then
			echo "Kibana is already running"
	else
			$DAEMON $DAEMON_ARGS 1>"$LOG" 2>&1 &
			echo $! > "$PIDFILE"
			PID=$!
			if [ "$PID" > 0 ]
			then
				echo "Kibana started with pid $!"
			else
				echo "Kibana could not be started"
			fi    
	fi
		
	
}


do_status() {
	if pid_file_exists
	then	
		PID=$(cat $PIDFILE)
		STATUS=$(ps ax | grep $PID | grep -v grep | awk '{print $1}')
		
		if [ "$STATUS" == "$PID" ]
		then
				echo "Kibana is running on proccess $PID"
		else
				echo "Kibana is NOT running"
				rm $PIDFILE
		fi
	else
		echo "Kibana is NOT running"
	fi
}

do_stop() {
	if pid_file_exists
	then	
		PID=$(cat $PIDFILE)
		STATUS=$(ps ax | grep $PID | grep -v grep | awk '{print $1}')
		
		if [ "$STATUS" == "$PID" ]
		then
				echo "Killing Kibana...."
				KILL=$(kill -15 $PID)
				rm $PIDFILE
				sleep 1
				echo -e "\tKibana (PID:$PID) killed"
				
		else
				echo "Kibana is NOT running"
				rm $PIDFILE
		fi
	else
		echo "Kibana is NOT running"
	fi
}


case "$1" in
  start)
	do_start;;
  stop)
	do_stop
	;;
  status)
	do_status
	;;
  restart)
	do_stop
	do_start
	;;
  *)
	echo "Usage: $SCRIPTNAME {start|stop|status|restart}" >&2
	exit 3
	;;
esac

:




