# for some reason the matches DIR kept storing previous iterations
# this file is used to reset the server see "reload_server" function in app.py
def reload_server():
    f = open("reload_server.py", "a")
    f.write(" ")
    print('Write Complete, Server Reloaded')
    f.close()                    