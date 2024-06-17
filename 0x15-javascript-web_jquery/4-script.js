$("DIV#toggle_header").click(function() {
    let currentClass = $("header").attr("class");

    if (currentClass === "red") {
      $("header").removeClass("red").addClass("green");
    } else {
      $("header").removeClass("green").addClass("red");
    }
  });
});
