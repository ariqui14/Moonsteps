%#template to generate a HTML table from a list of tuples (or list of lists, or tuple of tuples or ...)
%# 1.06.24: Updating to generate an html form with a checkbox. If checkbox gets checked and "Submit" clicked should return the same table with the checked task removed
<p>Moonsteps</p>

%#<table border="1">

%index = 0
%for task in taskList:
  %index = taskList.index(task)
  <input type="checkbox" id={{index}} name={{task}} value = {{task}}>
  <label for={{index}}> {{task}} </label> 
%end

<form action="/new" method="GET">
  <input type="text" size="100" maxlength="100" name="task">
  <input type="submit" name="New" value="New">
</form>

