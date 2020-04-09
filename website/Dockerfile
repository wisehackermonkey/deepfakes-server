FROM nginx:alpine
COPY src/ /usr/share/nginx/html
RUN echo "nginx:alpine started."
EXPOSE 80
CMD ["nginx","-g","daemon off;"]