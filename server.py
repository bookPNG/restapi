import app
from waitress import serve

host_name = '0.0.0.0'
port_num = 5100
while(True):
    print(host_name,":",port_num," is statred")
    serve(app.appflask,host=host_name,port=port_num)
