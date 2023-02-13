
# **************************************************************************
# -
# Devoir 1
# ===========================================================================
# ===========================================================================
# YAO KEVIN AMOUZOU
# -
# ===========================================================================
# ===========================================================================
# 
# ===========================================================================



SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"

prefix_cmd() {
    local PREF="${1//\//\\/}" # replace / with \/
    shift
    local CMD=("$@")
    "${CMD[@]}" 1> >(sed "s/^/${PREF}/") 2> >(sed "s/^/${PREF}/" 1>&2)
}

ctrl_c() {
    echo "===> Shutting down services"

    echo "===> Shutting down mysql"
    kill "$mysql_pid"

    echo "===> Shutting down wsgi"
    kill "$wsgi_pid"
}

echo "===> Creating docker network"
docker network create db

echo "===> Starting mysql"
prefix_cmd "mysql: " "$SCRIPT_DIR/run_feed_db.sh" &
postgresql_pid=$!

echo "===> Starting minio"
prefix_cmd "wsgi: " "$SCRIPT_DIR/run_wsgi.sh" &
minio_pid=$!

trap ctrl_c INT

wait $mysql_pid $wsgi_pid

echo "===> All services stopped"