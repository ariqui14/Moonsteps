from bottle import run, route, debug, template, request, error, TEMPLATE_PATH
import sqlite3
global TEMPLATE_PATH
TEMPLATE_PATH.insert(0, 'Moonsteps')

taskList = []

@route('/')
def todo_list():
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    c.execute("SELECT id FROM todo")
    taskNo = c.fetchone() 

    c.execute("SELECT id, task FROM todo WHERE status LIKE '1'")

    result = c.fetchall()
    c.close()
 
    return template('make_table', rows=result, TaskNo=taskNo, taskList = taskList)
#rows=result, TaskNo=, TaskName=, Task=

#{{TaskNo}}, {{TaskName}}, and {{Task}}

@route('/new', method='GET')
def new_item():
   #This page checks GETing the info from whether or not the user has saved to obtain a new task
    if request.GET.save:
        new = request.GET.task.strip()
        conn = sqlite3.connect('todo.db')
        c = conn.cursor()

        c.execute("INSERT INTO todo (task, status) VALUES (?,?)", (new, 1))
        new_id = c.lastrowid

        conn.commit()
        c.close()

        return '<p>The new task was inserted into the database, the ID is %s</p>' % new_id
    else:
        return template('new_task.tpl')
    

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