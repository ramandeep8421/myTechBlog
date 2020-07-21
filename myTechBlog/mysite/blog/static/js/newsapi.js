
$(document).ready(function(){
  $('#searchbtn').on("click" ,function(e){
    e.preventDefault();

    let query = $("#searchquery").val();
    let url = "http://newsapi.org/v2/top-headlines?q="+query+"&country=us&category=business&apiKey=de1917a736a946658c36c3a0a11aa8ce";
    if(query != ""){

       $.ajax({
         url: url,
         method: "GET",
         dataType: "json",

         beforeSend: function(){
           $("#loader").show();
         },

         complete: function(){
           $("#loader").hide();
         },
         success: function(news){
           let output ="";
           let latestNews = news.articles;

           for(var i in latestNews){
             output +=`
                <h4>${latestNews[i].title}</h4>
                <img src = "${latestNews[i].urlToImage}">
                <p>${latestNews[i].description}</p>
                <p>${latestNews[i].description}</p>
                <p>published on :${latestNews[i].publishedAt}</p>
                <a>${latestNews[i].url}</a>

                            `;

           }
           if(output !== ""){
             $("#newsResults").html(output);
           }else{
             let newsNotFound = "This news isn't available. Sorry about that. search for something else.";
             $("#newsResults").html(newsNotFound);
           }
         },
         error: function(){
           console.log("error");
         }
       });
    }else {
      console.log("please enter something");

    }
  });
});
