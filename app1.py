from flask import Flask

FAI=Flask(__name__)

@FAI.route('/wish/<na>')

def wish(na):
    return f'hi how are u {na}'

if __name__=='__main__':

   FAI.run(debug=True)