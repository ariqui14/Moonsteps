from bottle import run, route, debug, template, request, error, TEMPLATE_PATH
import sqlite3
import bottle

global TEMPLATE_PATH
TEMPLATE_PATH.insert(0, 'Moonsteps')
taskList = []
number = 0
@route('/', method='GET')
def todo_list():
    if request.GET.New:
        new = request.GET.task.strip()
        conn = sqlite3.connect('todo.db')
        c = conn.cursor()

        c.execute("INSERT INTO todo (task, status) VALUES (?,?)", (new, 1))
        taskNo = c.lastrowid

        conn.commit()
        result = c.fetchall()
        c.close()
        taskList = []
        for row in result:
    #NEED {{TaskNo}}, {{TaskName}}, and {{Task}} passed from main.py
            for col in row:
                if type(col) == int:
                    number = col
                else:
                 task = col
                 name = "task" 
                 taskList.append(task)
        
        return bottle.redirect('/')
    else:
        conn = sqlite3.connect('todo.db')
        c = conn.cursor()
        c.execute("SELECT id FROM todo")
        taskNo = c.fetchone() 

        c.execute("SELECT id, task FROM todo WHERE status LIKE '1'")

        result = c.fetchall()
        c.close()
        taskList = []
        for row in result:
    #NEED {{TaskNo}}, {{TaskName}}, and {{Task}} passed from main.py
            for col in row:
                if type(col) == int:
                    number = col
                else:
                 task = col
                 name = "task" 
                 taskList.append(task)
        return template('make_checklist', rows=result, TaskNo=taskNo, taskList = taskList)

#check page when someone clicks a check and check which item was clicked to remove it from the todo.db. 
    
#{{TaskNo}}, {{TaskName}}, and {{Task}}


@route('/edit/<no:int>', method='GET')
def edit_item(no):

    if request.GET.save:
        edit = request.GET.task.strip()
        status = request.GET.status.strip()

        if status == 'open':
            status= 1
        else:
            status = 0

        conn = sqlite3.connect('todo.db')
        c= conn.cursor()
        c.execute("UPDATE todo SET task = ?, status = ? WHERE id LIKE ?", (edit, status, no))
        conn.commit()

        return '<p>The item number %s was successfully updated</p>' % no 
    
    else:
        conn = sqlite3.connect('todo.db')
        c = conn.cursor()
        c.execute("SELECT task FROM todo WHERE id LIKE ?", (str(no),))
        cur_data = c.fetchone()

        return template('edit_task', old=cur_data, no=no)

@error(404)
def error404(error):
    return 'Nothing here, sorry'



if __name__ == '__main__': 
    run(debug=True, reloader = True)