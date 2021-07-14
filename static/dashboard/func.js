// todo editor here //
var todo_title, todo_date, todo_id;
$(".editor-pen").click(function () {
  todo_title = $(this).parent().text();
  todo_date = $(this).parent().parent().children(".js-date-picker").text();
  todo_id = $(this).parent().parent().children(".todo-id").text();
  $("#todo").val(todo_title);
  $("#due_date").val(todo_date);
  $(".edited-todo-id").val(todo_id);
  $(".todo-editor").css("display", "block");
});
$(".trash").click(function () {
  todo_title = $(this).parent().text();
  todo_date = $(this).parent().parent().children(".js-date-picker").text();
  todo_id = $(this).parent().parent().children(".todo-id").text();
  $("#dtodo").val(todo_title);
  $("#ddue_date").val(todo_date);
  $(".deleted-todo-id").val(todo_id);
  $(".todo-deletor").css("display", "block");
});

$(".editor-form-close").click(function () {
  $(".todo-editor").css("display", "none");
  $(".todo-deletor").css("display", "none");
});

$("#demo-login").click(function () {
  $(".demo-password").val("test");
  $(".demo-user").val("test");
  $("#login-form").submit();
});
var pageId = $(".content-center").attr("id");
$("." + pageId).addClass("active");
