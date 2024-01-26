%#template to generate a HTML table from a list of tuples (or list of lists, or tuple of tuples or ...)
%# 1.06.24: Updating to generate an html form with a checkbox. If checkbox gets checked and "Submit" clicked should return the same table with the checked task removed
<p>Moonsteps</p>

 <head>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.7.1/jquery.min.js"></script>
<script> 
$(document).on("dblclick", "#content", function(){
  var current = $(this).text();
  $("#content").html('<textarea class ="form-control" id="newcont" rows="5">'+current+'</textarea>');
    $("#newcont").focus();

    $ ("#newcont").focus(function() {
        console.log('in');
    }).blur(function() {
        var newcont = $("#newcont").val();
        $("#content").text(newcont);
    });
})

</script>

  <script type="text/javascript">
    document.querySelector("input[type=checkbox]").addEventListener("change", function(){
      check.style.visibility = 'hidden';
    }, false);
  </script>
</head>

%#<table border="1">

<form action="/" method="GET">

%index = 0
%for task in taskList:
  %index = taskList.index(task)
  <div id = "content">
  

  <input type="checkbox" id={{index}} name={{task}} value = {{task}}>

  <div id="content"><label for={{index}}> {{task}} </label> </div>
  </div>
%end

  <input type="text" size="100" maxlength="100" name="task">
  <input type="submit" name="New" value="New">
</form>

