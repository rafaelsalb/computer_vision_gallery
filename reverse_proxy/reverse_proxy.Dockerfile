FROM nginx

EXPOSE 5002:4443

COPY nginx.conf /etc/nginx/nginx.conf
# COPY computer_vision_gallery.conf.template /etc/nginx/conf.d/computer_vision_gallery.conf.template
COPY computer_vision_gallery.conf /etc/nginx/conf.d/computer_vision_gallery.conf
COPY cert.pem /etc/nginx/ssl/cert.pem
COPY key.pem /etc/nginx/ssl/key.pem
# COPY startup.sh /home/startup.sh
# RUN sh -c "envsubst '\$NG_NAME_SERVER \$NG_FRONTEND_HOST' < /etc/nginx/conf.d/computer_vision_gallery.conf.template > /etc/nginx/conf.d/computer_vision_gallery.conf"
CMD [ "nginx", "-g", "daemon off;" ]
