# Use the official PHP Apache image
FROM php:8.1-apache

# Enable necessary Apache modules
RUN a2enmod rewrite

# Set the working directory inside the container
WORKDIR /var/www/html

# Copy the application files into the container
COPY . /var/www/html

RUN mkdir /var/www/html/images

# Give permissions to the images folder to allow file uploads
RUN chown -R www-data:www-data /var/www/html/images && chmod -R 777 /var/www/html/images

# Expose port 80 for Apache
EXPOSE 80

# Start Apache in the foreground
CMD ["apache2-foreground"]
