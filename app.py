from flask import Flask

FAI=Flask(__name__)
@FAI.route('/wish/<name>')

def wish(name):
    return f'Hello How Are You {name}'

if __name__=='__main__':
    FAI.run(debug=True)