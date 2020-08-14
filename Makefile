IMAGE_NAME=bireme/iahx-wizard
APP_VERSION=$(shell git describe --tags --long --always | sed 's/-g[a-z0-9]\{7\}//')
TAG_LATEST=$(IMAGE_NAME):latest

COMPOSE_FILE_DEV=docker-compose-dev.yml


## variable used in docker-compose for tag the build image
export IMAGE_TAG=$(IMAGE_NAME):$(APP_VERSION)

tag:
	@echo "IMAGE TAG:" $(IMAGE_TAG)

## docker-compose desenvolvimento
dev_build:
	@docker-compose -f $(COMPOSE_FILE_DEV) build

dev_up:
	@docker-compose -f $(COMPOSE_FILE_DEV) up -d

dev_run:
	@docker-compose -f $(COMPOSE_FILE_DEV) up

dev_logs:
	@docker-compose -f $(COMPOSE_FILE_DEV) logs -f

dev_stop:
	@docker-compose -f $(COMPOSE_FILE_DEV) stop

dev_ps:
	@docker-compose -f $(COMPOSE_FILE_DEV) ps

dev_rm:
	@docker-compose -f $(COMPOSE_FILE_DEV) rm -f

dev_exec_shell:
	@docker-compose -f $(COMPOSE_FILE_DEV) exec app_wizard sh

dev_make_test:
	@docker-compose -f $(COMPOSE_FILE_DEV) exec app_wizard make test


## docker-compose API
prod_build:
	@docker-compose --compatibility build
	@docker tag $(IMAGE_TAG) $(TAG_LATEST)

prod_up:
	@docker-compose --compatibility up -d

prod_logs:
	@docker-compose --compatibility logs -f

prod_stop:
	@docker-compose --compatibility stop

prod_ps:
	@docker-compose --compatibility ps

prod_exec_shell:
	@docker-compose --compatibility exec app_wizard sh

prod_exec_collectstatic:
	@docker-compose --compatibility exec -T app_wizard python manage.py collectstatic --noinput

prod_exec_webserver:
	@docker-compose --compatibility exec -T webserver sh

prod_make_test:
	@docker-compose --compatibility exec -T app_wizard make test
