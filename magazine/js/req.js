const TITLE_CHAR_LIMIT = 70;
$().ready(function () {
  // /** Disable Search */
  // $("#search_btn").click(function () {

  // });
  /** Do Search */
  $("#search_btn").click(function () {
    let param = $("#search_param").val();
    if (param == "") {
      $("#my_news")
        .children("article")
        .each(function () {
          $(this).removeClass("hide-from-search").removeClass("show-in-search");
        });
      $(".js-fh5co-nav-toggle").click();
      return;
    }
    fetch(`http://localhost:8000/news/read/items/search/?search=${param}`)
      .then((response) => response.json())
      .then((data) => {
        console.log(data);
        // alert(data.ids.includes("95"));
        // alert(data.ids.includes("86"));
        // alert(data.ids.includes("88"));
        $("#my_news")
          .children("article")
          .each(function () {
            // if (data.ids.includes(Number($(this).attr("id").split("n")[1]))) {
            //   console.log($(this).attr("id").split("n")[1]);
            // }
            if (data.ids.includes(Number($(this).attr("id").split("n")[1])))
              $(this)
                .removeClass("hide-from-search")
                .addClass("show-in-search");
            else
              $(this)
                .removeClass("show-in-search")
                .addClass("hide-from-search");
          });
      });

    // $(`#n${}`)
    $(".js-fh5co-nav-toggle").click();
  });
  /** Disable Filters */
  $("#show_all_btn").click(function () {
    $("#my_news")
      .children("article")
      .each(function () {
        $(this).show();
      });
    $("#from_date").val("");
    $("#to_date").val("");
    $(".js-fh5co-nav-toggle").click();
  });

  /** Do Filter */
  $("#filter_form").submit(function (e) {
    e.preventDefault();
    let from_date = $("#from_date").val();
    let to_date = $("#to_date").val();
    let news_count = $("#size").val();
    if (!from_date || from_date.length === 0) from_date = "0000-00-00 00:00:00";
    else from_date = from_date.replace("T", " ") + ":00";
    if (!to_date || to_date.length === 0)
      to_date = new Date().toISOString().split(".")[0].replace("T", " ");
    else to_date = to_date.replace("T", " ") + ":59";
    if (!news_count || news_count.length === 0) news_count = -1;
    $("#my_news")
      .children("article")
      .each(function () {
        if (news_count !== 0) {
          let d = $(this).children("span").first().html();
          if (d < from_date || d > to_date) {
              console.log(d);
            $(this).removeClass("show-by-filter").addClass("hide-by-filter");
          }
        //   $(this).hide();
          else {
            $(this).removeClass("hide-by-filter").addClass("show-by-filter");
            // $(this).show();
            news_count--;
          }
        } else $(this).removeClass("show-by-filter").addClass("hide-by-filter");
      });
    $(".js-fh5co-nav-toggle").click();
  });

  /** init */
  fetch("http://127.0.0.1:8000/news/read/channel/")
    .then((response) => response.json())
    .then((data) => {
      console.log(data);
      res = data.results[0];
      let el = `
        <a href="${res.base_link}">${res.title}</a>
        <br><br>
        <img src="${res.image}" alt="CNN News" class="img-responsive" style="margin: auto;">`;
      $("#fh5co-logo").append(el);
    });

  /** Get All News */
  fetch("http://127.0.0.1:8000/news/read/items/")
    .then((response) => response.json())
    .then((data) => {
      console.log(data);
      res = data.results;
      for (var i = 0; i < res.length; i++) {
        title = res[i].title;
        if (title.length > TITLE_CHAR_LIMIT) {
          title = title.substring(0, TITLE_CHAR_LIMIT - 1);
          title += "...";
        }
        let el = `
        <article class="col-lg-4 col-md-4 col-sm-4 col-xs-6 col-xxs-12 show-by-filter" id="n${res[i].id}" >
        <figure>
          <a href="${res[i].link}"><img src="${res[i].image_url}" alt="Image" class="img-responsive"></a>
        </figure>
        <h2 class="fh5co-article-title"><a href="${res[i].link}">${title}</a></h2>
        <span class="fh5co-meta fh5co-date">${res[i].published_date}</span>
        </article>`;
        $("#my_news").append(el);
      }
    });
});
