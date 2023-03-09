#!/bin/bash
exec celery flower --app petstore --workdir src
