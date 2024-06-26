FROM nginx:stable-alpine3.19 as publish
ARG FRONTEND_HOST
ARG API_HOST
ARG MODEL_HOST
ENV FRONTEND_HOST=${FRONTEND_HOST}
EXPOSE 5002:4443
COPY nginx.conf /etc/nginx/nginx.conf
COPY computer_vision_gallery.conf /etc/nginx/conf.d/computer_vision_gallery.conf
COPY cert.pem /etc/nginx/ssl/cert.pem
COPY key.pem /etc/nginx/ssl/key.pem
CMD ["nginx", "-g", "daemon off;" ]
