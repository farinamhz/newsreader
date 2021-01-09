const TITLE_CHAR_LIMIT = 70;
$().ready(function () {
  /** Disable Filters */
  $("#show_all_btn").click(function () {
    $("#my_news")
      .children("article")
      .each(function () {
        $(this).show();
      });
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
          // alert(d)
          if (d < from_date || d > to_date) $(this).hide();
          else{
            $(this).show();
            news_count--;
          } 
        } else $(this).hide();
      });
    $(".js-fh5co-nav-toggle").click();
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
        var el = `
        <article class="col-lg-4 col-md-4 col-sm-4 col-xs-6 col-xxs-12" >
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
