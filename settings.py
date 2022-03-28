
# define address for mongoDB
MONGO_HOST = 'localhost'
MONGO_PORT = 27017 #default mongo port

# db name to log to
# will be created if does not currently exist
MONGO_DBNAME = 'CommandCenterLogs'


# Enable reads (GET), inserts (POST) and DELETE for resources/collections
# (if you omit this line, the API will default to ['GET'] and provide
# read-only access to the endpoint).
RESOURCE_METHODS = ['GET', 'POST', 'DELETE']

# Enable reads (GET), edits (PATCH), replacements (PUT) and deletes of
# individual items  (defaults to read-only item access).
ITEM_METHODS = ['GET', 'PATCH', 'PUT', 'DELETE']




log_schema = {
    # Schema definition, based on Cerberus grammar. Check the Cerberus project
    # (https://github.com/pyeve/cerberus) for details.
    'app': {
        'type': 'string',
        'minlength': 1,
        'maxlength': 100,
    },
    'status':{
        'type': 'string',
        'minlength': 1,
        'maxlength': 100,
    },
    'time': {
        'type': 'string',
        'minlength': 1,
        'maxlength': 30,
        'required': True,
        'unique': False,
    },
    'duration': {
        'type': 'string',
        'minlength': 1,
        'maxlength': 30,
        'required': True,
        'unique': False,
    }
   
}


logs = {
     # 'title' tag used in item links. Defaults to the resource title minus
    # the final, plural 's' (works fine in most cases but not for 'people')
    'item_title': 'logs',

    # by default the standard item entry point is defined as
    # '/people/<ObjectId>'. We leave it untouched, and we also enable an
    # additional read-only entry point. This way consumers can also perform
    # GET requests at '/people/<lastname>'.
    # 'additional_lookup': {
    #     'url': 'regex("[\w]+")',
    #     'field': 'lastname'
    # },

    # We choose to override global cache-control directives for this resource.
    'cache_control': 'max-age=10,must-revalidate',
    'cache_expires': 10,

    # most global settings can be overridden at resource level
    'resource_methods': ['GET','POST','DELETE'],

    'schema': log_schema
}



failures = {
    'item_title': 'failures',
    'cache_control': 'max-age=10,must-revalidate',
    'cache_expires': 10,
    # most global settings can be overridden at resource level
    'resource_methods': ['GET','POST','DELETE'],
    'schema': log_schema
}



DOMAIN = {
    'logs':logs,
    'failure':failures,
    'test':{}
    }

    