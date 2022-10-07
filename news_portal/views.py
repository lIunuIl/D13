import logging

from django.http import HttpResponse

logger = logging.getLogger('django')


def index_test(request):
    logger.info('Hello! It`s INFO! :)')
    logger.debug('Hello! It`s DEBUG! :)')
    logger.warning('Hello! It`s WARNING! :)')
    logger.error('Hello! It`s ERROR! :)')
    logger.critical('Hello! It`s CRITICAL! :)')
    return HttpResponse('<p> Text for test <p>')
