#!/usr/bin/env bash

# settings
PROJECT_NAME="DJANGOCMS_HTML_TAGS"

# colors
BLUE="\\033[1;34m"
GREEN="\\033[1;32m"
NORMAL="\\033[0;39m"

print_help() {
    echo -e "${BLUE}Available environments${NORMAL}"
    echo "  - DEV (default)"
    echo "  - PROD"
    echo "  - STAGING"
    echo ""
    echo -e "${BLUE}Available commands${NORMAL}"
    echo -e "  > docker [:command]      Run a Docker command."
    echo -e "  > runserver              Run the test server."
    echo -e "  > runtests               Run unit tests."
    echo -e "  > shell                  Open Bash session in the backend service."
}

docker_command() {
    command="docker-compose -p ${PROJECT_NAME} -f docker/docker-compose.yml "

    case ${ENV} in
        "PROD")
            file_prefix="prod"
            ;;
        "STAGING")
            file_prefix="staging"
            ;;
        *)
            file_prefix="dev"
            ;;
    esac

    command+="-f docker/docker-compose.${file_prefix}.yml ${@}"
    echo -e "${BLUE}    Command: ${NORMAL}${command}"
    echo -e ""
    eval ${command}
}

docker() {
    docker_command ${@}
}

runtests() {
    test_command="'
        coverage run setup.py test &&
        coverage html
    '"
    docker_command run --rm backend sh -c ${test_command}
}

runserver() {
    docker_command run --rm --service-ports --entrypoint /code/docker/backend/entrypoint.sh backend python manage.py runserver 0:8000
}

shell() {
    docker_command run --rm backend bash
}

if [ -z ${1} ]
then
    print_help
else
    case ${ENV} in
        "PROD")
            env_str="production"
            ;;
        "STAGING")
            env_str="staging"
            ;;
        *)
            env_str="development"
            ;;
    esac
    echo -e "${BLUE}Environment:${NORMAL} ${env_str}"
    ${@}
fi
