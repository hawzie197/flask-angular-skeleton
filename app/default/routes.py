from . import default

@default.route('/')
def home():
    return default.send_static_file('index.html')

