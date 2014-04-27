#!/bin/sh
### BEGIN INIT INFO
# Provides:          ozzie
# Required-Start:    $time $network $remote_fs
# Required-Stop:
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
# Short-Description: Updates Ozzie server
# Description: Polls Ozzie periodically or if state changes
### END INIT INFO

dir="/home/pi/batcave"
cmd="ozzie"

name=`basename $0`
pid_file="/var/run/$name.pid"
stdout_log="$dir/syslog.log"
stderr_log="$dir/errlog.log"

get_pid() {
    cat "$pid_file"
}

is_running() {
    [ -f "$pid_file" ] && ps `get_pid` > /dev/null 2>&1
}

case "$1" in
    start)
    if is_running; then
        echo "Ozzie is already running."
    else
        echo "Starting Ozzie..."
        cd "$dir"
        sudo $dir/$cmd >> "$stdout_log" 2>> "$stderr_log" &
        echo $! > "$pid_file"
        if ! is_running; then
            echo "Ozzie could not be started. (see $stdout_log and $stderr_log)"
            exit 1
        fi
    fi
    ;;
    stop)
    if is_running; then
        echo -n "Stopping Ozzie..."
        kill `get_pid`
        for i in {1..10}
        do
            if ! is_running; then
                break
            fi

            echo -n "."
            sleep 1
        done
        echo

        if is_running; then
            echo "Ozzie could not be stopped!"
            exit 1
        else
            echo "Ozzie rests"
            if [ -f "$pid_file" ]; then
                rm "$pid_file"
            fi
        fi
    else
        echo "Ozzie is already stopped!"
    fi
    ;;
    restart)
    $0 stop
    if is_running; then
        echo "Ozzie could not be stopped, restart impossible"
        exit 1
    fi
    $0 start
    ;;
    status)
    if is_running; then
        echo "Ozzie is running"
    else
        echo "Ozzie is not running"
        exit 1
    fi
    ;;
    *)
    echo "Usage: $0 {start|stop|restart|status}"
    exit 1
    ;;
esac

exit 0
