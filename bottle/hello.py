from bottle import route, run, template
import sys, re
import makeUl 

filename = re.search(r'(.*)[^\.py$]', sys.argv[0])
pagename = '/' + filename.group()
pnum =8080

IP = {0:'localhost', 1:'192.168.12.68'}
ul =  makeUl.re_l()

print('\n[local]{}//{}:{}{}'.format('http:', IP[0], pnum, pagename))
print('[net]{}//{}:{}{}\n'.format('http:', IP[1], pnum, pagename))


@route('/')
@route('/hello/<name>')
def greet(name='Stranger'):
    return template('Hello {{name}}, how are you?', name=name)

@route('/object/<id:int>')
def callback(id):
    assert isinstance(id, int)
    return template('id = {{id}}', id=id)

@route('/show/<name:re:[a-z]+>')
def callback(name):
    assert name.isalpha()
    return template('name = {{name}}', name=name)

@route('/listpage')
def hello():
    global ul
    return ul

#localhost
run(host=IP[0], port=pnum)

#net
#run(host=IP[1], port=pnum)




