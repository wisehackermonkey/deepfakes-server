FROM nginx:alpine
COPY src/ /usr/share/nginx/html
COPY config/nginx.conf /etc/nginx/nginx.conf
RUN echo "nginx:alpine started."
EXPOSE 80
CMD ["nginx","-g","daemon off;"]