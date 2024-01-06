%#template to generate a HTML table from a list of tuples (or list of lists, or tuple of tuples or ...)
%# 1.06.24: Updating to generate an html form with a checkbox. If checkbox gets checked and "Submit" clicked should return the same table with the check removed
<p>Moonsteps</p>

%#<table border="1">
<form>
%for row in rows:
  %#NEED {{TaskNo}}, {{TaskName}}, and {{Task}} passed from main.py
  <br>
  %number = 0
  %for col in row:
    %if type(col) == int:
      %number = col
    
    %else:
      %task = col
      %name = "task" 
      <input type="checkbox" id={{number}} name={{name}} value = {{task}}>
      <label for={{number}}> {{task}} </label> 
    
  %end
%end
</form>
%#</table>