const TITLE_CHAR_LIMIT = 70;
$().ready(function () {
  fetch("http://127.0.0.1:8000/news/read/items/", {
    // method: 'POST',
    // headers: {
    //   'Content-Type': 'application/json'
    // },
    // body: JSON.stringify(data),
  })
    .then((response) => response.json())
    // .then((data) => console.log(data));
    .then((data) => {
      console.log(data);
      res = data.results;
      for (var i = 0; i < res.length; i++) {
        title = res[i].title;
        if (title.length > TITLE_CHAR_LIMIT) {
          title = title.substring(0, TITLE_CHAR_LIMIT - 1);
          title += "...";
        }
        // <article class="col-lg-4 col-md-4 col-sm-4 col-xs-6 col-xxs-12">
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
