from flask import Blueprint

from counter.models import Counter


# Instantiate blueprint for counter
counter_app = Blueprint('counter_app', __name__)

# Define root route
@counter_app.route('/')
def init():
    # use pdb to inspect values
    import pdb; pdb.set_trace()
    # Check if counter object exists
    counter = Counter.objects.all().first()
    
    # Increment it if exists, save changes
    if counter:
        counter.count +=1
        counter.save()

    # Create counter w/ initial value if it doesn't exist
    else:
        counter = Counter()
        counter.count = 1
        counter.save()

    # Return value in HTML
    return "<h1>Counter: " + str(counter.count) + "</h1>"