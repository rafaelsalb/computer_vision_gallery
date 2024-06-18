FROM nginx
EXPOSE 5002:80
COPY pages /usr/share/nginx/html