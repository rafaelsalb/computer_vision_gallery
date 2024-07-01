#!/usr/bin/env bash
envsubst '$NG_SERVER_NAME $NG_FRONTEND_HOST $NG_BACKEND_HOST $NG_MODEL_HOST' < /etc/nginx/conf.d/computer_vision_gallery.conf.template > /etc/nginx/conf.d/computer_vision_gallery.conf;
nginx -g "daemon off;";
