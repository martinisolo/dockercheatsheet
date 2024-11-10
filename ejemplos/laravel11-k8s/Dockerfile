FROM php:8.2-apache
#COPY src/ /var/www/html/

RUN apt-get update && apt-get install -y nano zip unzip libzip-dev curl 

RUN docker-php-ext-install zip && docker-php-ext-install mysqli pdo pdo_mysql && docker-php-ext-enable pdo_mysql && a2enmod rewrite


RUN mv /etc/apache2/sites-available/000-default.conf /etc/apache2/sites-available/000-default.conf.bak
COPY laravel-apache2.conf  /etc/apache2/sites-available/000-default.conf

# Instalamos composer, si utilizamos algun framework como symfony nos hara falta
RUN curl https://getcomposer.org/composer.phar -o /usr/bin/composer && chmod +x /usr/bin/composer

# Nodejs 20
RUN apt-get update \
&& apt-get install -y ca-certificates gnupg \
&& mkdir -p /etc/apt/keyrings \
&& curl -fsSL https://deb.nodesource.com/gpgkey/nodesource-repo.gpg.key | gpg --dearmor -o /etc/apt/keyrings/nodesource.gpg \
&& echo "deb [signed-by=/etc/apt/keyrings/nodesource.gpg] https://deb.nodesource.com/node_20.x nodistro main" | tee /etc/apt/sources.list.d/nodesource.list \
&& apt-get update \
&& apt-get install nodejs -y

RUN apt install build-essential python3 python3-pip python3-dev python3.11-venv wget -y

# Create the virtual environment
RUN python3 -m venv /venv
ENV PATH=/venv/bin:$PATH
RUN pip3 install transformers torch torchvision

# Le decimos que escuche en el puerto 80 para el servidor Web
EXPOSE 80
