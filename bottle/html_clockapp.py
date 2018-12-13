from bottle import run, get, post, request, redirect
import serial

con = serial.Serial('/dev/ttyACM0', 9600)
addlist = list()
posthtml = {'a':'', 'w':'', 't':'', 'm':''}
formhtml = '''
        <h4>Arduino Clock Setting</h4>
            <form action="/setting" method="post" style="margin-top:2em;">
               <label for="adj"> Adjust:<input id="adj" name="Adjust" type="text" />yyyy,dd.hh,mm,ss<br></label>

               <label for="alm"> Alerm:<input id="alm" name="Alerm" type="text" />hh,mm,ss<br></label>

               <label for="tmr"> Timer:<input id="tmr" name="Timer" type="text" />hh,mm,ss<br></label>

               <label for="msg"> Message:<input id="msg" name="Message" type="text" /><br></label>


                <input name="sub" type="submit" />
            </form>
            <style>label{display:block; margin-bottom:1em; p{border:solid 1px #ccc;}</style>'''

@get('/setting')
def setting():
    global formhtml
             
    global posthtml

    addhtml = '<p>Adjust: ' + str(posthtml['a']) + '<br>' + 'Alerm: ' + str(posthtml['w']) + '<br>' + 'Timer: ' + str(posthtml['t']) + '<br>' + 'Message: ' + str(posthtml['m']) + '<br></p>'
  
    return formhtml + addhtml



@post('/setting')
def do_setting():
    req ={'a': request.forms.get('Adjust'),
          'w': request.forms.get('Alerm'),
          't': request.forms.get('Timer'),
          'm': request.forms.get('Message')}
             
    global posthtml

    print(posthtml)
    respons =''
    for i, j in req.items():
        if req[i]:
            print(i + ',' + j + '\n')
            cmd = i + ',' + j + '\n'
            buf = bytes(cmd, 'utf-8')
            con.write(buf)
            posthtml[i] = j
            
    return redirect('/setting')
       
        
if __name__ == '__main__':
    try:
        run(host='localhost', port=8080)

    except:
        pass

    finally:
        print('Close serial')
        con.close()

