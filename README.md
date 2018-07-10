# Docker-Nginx-Letsencrypt-Flask-Postgres
a Flask app using PostgreSQL and an Nginx proxy server with Letsencrypt, all through Docker containers

## Steps:
1. Clone this repository.
2. Edit `'.env'` file: set `'NGINX_FILES_PATH'` and `'WEB_STATIC_FILES_PATH'`
3. Execute `'start.sh'` file, and wait few seconds for the containers to be created.
4. Change `flask/web/` content with your flask app project. (or keep the example).
4. In `flask` directory, edit `'.env'` file (for the environment variables during docker build) 
and `'env_file'` (for environment variables within the containers):
5. Run `docker-compose up -d`
6. Wait few moments for the containers to build and certificates to generate.
7. Check your website, if you used the example, check if the database is working by submitting the form.

## Credits:

+ [docker-gen][5] and [nginx-proxy][6] by [Jason Wilder][7]
+ [docker-compose-letsencrypt-nginx-proxy-companion][8] by [Evert Ramos][9]

[5]: https://github.com/jwilder/docker-gen
[6]: https://github.com/jwilder/nginx-proxy
[7]: https://github.com/jwilder
[8]: https://github.com/evertramos/docker-compose-letsencrypt-nginx-proxy-companion
[9]: https://github.com/evertramos
