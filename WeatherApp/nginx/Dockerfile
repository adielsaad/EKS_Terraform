FROM nginx:alpine

# Override the default nginx configuration file
RUN rm /etc/nginx/conf.d/default.conf
COPY myapp.conf /etc/nginx/conf.d/
COPY nginx.conf /etc/nginx/nginx.conf
