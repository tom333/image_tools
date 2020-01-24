import eel

eel.init('web')
eel.start('index.html', size=(600, 400))@eel.expose
def hello_world():
    return "Hello from python"