import sys; sys.path.append("../lib")
from architecture_support import *

from bottle import route, run, template, request, get, post, put, delete
import thread

class Server(object):
    def __init__(self, host, port):
        self.app = None  # inject
        self.model = None # inject
        self.host = host
        self.port = port
        self.thread_id = None
        self.observers = multicast()
        self.json_from_dict = None  # inject
        
    @property
    def url_server(self):
        return "http://%s:%s" % (self.host, self.port)
        
    def StartServer(self):
        self.thread_id = thread.start_new_thread(self._Serve, ())

    def StopServer(self):
        print "stopping server thread..." # actually cannot kill python threads!?
        
    def _Serve(self):
        print "starting server thread..."

        def report_error(inst):
            msg = "Server exception: %s" % inst
            print msg
            return msg

        @route('/')
        def index():
            return "G'day"
        
        @route('/modelsize')
        def modelsize():
            return 'The model length is %d' % self.model.size

        @route('/dumpthings')
        def dumpthings():
            s = ""
            for thing in self.model.things:
                s += str(thing) + '<BR>'
            return s

        @route('/addthing')
        def addthing():
            self.observers.CMD_ADD_THING("fred")
            return 'The model length is now %d' % self.model.size

        # JSON

        @route('/jsontest')
        def jsontest():
            import time
            return {'status':'online', 'servertime':time.time()}

        # REST API
        
        @get('/things')
        def things():
            """
            GET /things
            Comment: List of things in json format, incl. link to full object. e.g.
                { "things": [ {"info": "some thing", "link": "http://localhost:8081/things/1", "id": 1},
                              {"info": "another thing", "link": "http://localhost:8081/things/2", "id": 2}
                            ]}
            Example: GET http://localhost:8081/things
            """
            try:
                return self.app.controller.CmdGetThingsAsDict()  # no need to call self.json_from_dict as bottle handles it
            except Exception, inst:
                return report_error(inst)

        @get('/things/:id')
        def things_id(id):
            """
            GET /things/id
            Comment: Displays just the one thing object. The id is supplied for convenience
                     even though its also on the url. e.g. {"id":1, "info":"thing info content here"}
            Example: GET http://localhost:8081/things/1
            """
            try:
                return self.app.controller.CmdGetThingAsDict(id)  # no need to call self.json_from_dict as bottle handles it
            except Exception, inst:
                return report_error(inst)

        @post('/things')
        def things_post():
            """
            POST /things, thing
            Comment: Adds a thing.
                     We get a link back e.g. http://localhost:8081/things/2
            Example: POST http://localhost:8081/things, info=thing+info+content+here
            Note: Is there a way to send json to the server? e.g. {"info":"thing info content here"}
            """
            try:
                info = request.forms.get('info')
                return self.app.controller.CmdAddThing(info)  # no need to call self.json_from_dict as bottle handles it
            except Exception, inst:
                return report_error(inst)

        @put('/things')
        def thing_put():
            """
            PUT /things, thing
            Comment: Modifes a thing.
            Example: POST http://localhost:8081/things, id=1&info=fred
               Note: Is there a way to send json to the server? e.g. {"id":1, "info":"MODIFIED info content here"}
            """
            try:
                id = request.forms.get("id")
                info = request.forms.get("info")
                return self.app.controller.CmdModifyThing(id, info)  # no need to call self.json_from_dict as bottle handles it
            except Exception, inst:
                return report_error(inst)

        @delete('/things/:id')
        def thing_delete(id):
            """
            DELETE /things/id
            Comment: Deletes a thing.
            Example: DELETE http://localhost:8081/things/1
            """
            try:
                return self.app.controller.CmdDeleteThing(id)
            except Exception, inst:
                return report_error(inst)
            
            
        # REST API - Support
            
        @get('/add') # or @route('/add')
        def add_form():
            return '''<form action="/things" method="POST">
                        <input name="info"     type="text" />
                      </form>'''

        @get('/modify') # or @route('/add')
        def modify_form():
            """
            Note PUT and DELETE are not supported in normal forms, so we have to do it via ajax
            """
            return '''
<!DOCTYPE html>

<html>
<head>
    <title>Put</title>
    <script src="//ajax.googleapis.com/ajax/libs/jquery/1.7.1/jquery.min.js" type="text/javascript"></script>
    <script>

    function submitForm() {
        $.ajax({type:'PUT', url: 'things', data:$('#ContactForm').serialize(), success: function(response) {
            $('#ContactForm').find('.form_result').html(response);
        }});
        return false;
    }
    
    
    // why doesn't this version work?
    // see http://www.jstiles.com/Blog/How-To-Submit-a-Form-with-jQuery-and-AJAX
    
    $('#delete').click(function (e) { 
    e.preventDefault();
    console.log("fred");
    $.ajax(
        {type:'PUT', url: 'things', data:$('#ContactForm').serialize(), success: function(response) {
                    $('#ContactForm').find('.form_result').html(response);
        }}    
    ); 
    });
    
    </script>
</head>

<body>
    
    <form id="ContactForm" onsubmit="return submitForm();">
        id: <input type="text" name="id" value="" /><br/> 
        info: <input type="text" name="info" value="" /><br/> 
        <br/>
        <input type="submit" name="submit" value="Submit" /><br />
        <input type="submit" name="delete" value="delete" /><br />
        <div class="form_result"> </div>
    </form>

</body>
</html>
'''
    

        run(host=self.host, port=self.port)
        # nothing runs after this point
