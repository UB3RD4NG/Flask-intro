from app import site

@site.route("/")
@site.route("/index")
def index():
    return "Hello, World!"
