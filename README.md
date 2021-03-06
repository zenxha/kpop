![image](http://owo.whats-th.is/BoLbteQ.jpg)
# Kpop Music Site!
Group Project for tri3!
### Links
- [Project Board](https://github.com/zenxha/kpop/projects/1) | [Project Board last 3 weeks](https://github.com/zenxha/kpop/projects/2)
- [Deployed Website](http://rubinfamily.dyndns.org:5000/)
- [Deployed Webiste ON TEACHER HARDWARE](https://kpop.nighthawkcodingsociety.com/)
- [Project Plan](https://docs.google.com/document/d/19tdgx0iDYYwwMcTxbIoo4nPW9igqUoKptFVv5eDoNms/edit)
- [Folder Containing Justifications for Minilab](https://drive.google.com/drive/u/1/folders/1rY2DlSWzvpxBbPOH8zE3hpo2-O9kGwoX)

### Collaborators
- Charlie Zhu ID: #72889453
- Komay Sugiyama ID: #30739783
- Chris Rubin ID: #72892271
- Devam Shrivastava ID: #51984972
- Eshaan Parlikar ID: #32022538

# How It's Made
## Theme Section (5pt)
- [Find Similar Songs Page](https://kpop.nighthawkcodingsociety.com/ks) (+0.5pt User interaction, +0.5pt Technical, +1pt Fun)
    - This page demonstrates usage and display of [online APIs that take parametrs](https://github.com/zenxha/kpop/blob/main/view/komay/classes/getsongs.py#L20)
    - User can input an Artist and the Track name as well as how they want the list sorted. The response displays song cards that the user can listen to. These cares provide info such as wear to listen and popularity info.
    - As a music-focused site, this page helps users find new songs if they ever want new songs that are similar to the ones they are currently listening to
- [Home page](https://kpop.nighthawkcodingsociety.com/) (+0.5pt*2 User interaction, +0.5pt Technical, +1pt Fun)
    - [Source Code](https://github.com/zenxha/kpop/blob/main/templates/index.html) Bootstrap use.
    - Has TWO user interactions. One, users can submit links to their spotify playlist that they want to share with the world.
    - Two, they can browse through other users' random submitted spotify playlists with the click of a button 
    - Using jquery [GET requests](https://github.com/zenxha/kpop/blob/main/templates/index.html#L90) to our own [API endpoint](https://github.com/zenxha/kpop/blob/main/view/api/app.py#L37-L51), we avoid having to refresh the page for new playlists by dynamically editing the DOM
    - This relates to the theme as it allows users to share music with the world
- Database (+0.5pt Technical)
    - This code shows the database that takes the user input from the submit form and connects it to our API, which our site sends request to using ajax.
    - [Link to database WRITING](https://github.com/zenxha/kpop/blob/main/views.py#L60-L63)
    - [Link to database model](https://github.com/zenxha/kpop/blob/main/model.py)
- OUR API (+0.5 Technical)
    - Serves data that drives our site, devs can access all user submitted data/playlists with a plethora of different endpoints.
    - 5 different endpoints. [backend code](https://github.com/zenxha/kpop/blob/main/view/api/app.py#L11-L73)
    - Serves as our API that other teams can use for crossover
## Individual Section (4.5pt)
- Blueprints (+4pt 4 labs)
    - [Each folder](https://github.com/zenxha/kpop/tree/main/view) is labled with the corresponding member to indicate their individual blueprint
- Technicals (+1pt 2 Technicals)
    - Each minilab utilizes [classes](https://github.com/zenxha/kpop/blob/main/view/komay/classes/getsongs.py) in order to pass in [parameters](https://github.com/zenxha/kpop/blob/main/view/komay/classes/getsongs.py#L11) that cause different functions to run 
    - 
## API Section (4pt)
- [API Endpoints](https://kpop.nighthawkcodingsociety.com/api/) (+2 [Receiving](https://github.com/zenxha/kpop/blob/main/view/komay/classes/getsongs.py#L20)  API, +2 Developing own endpoints)
- ![image](http://owo.whats-th.is/8NTno86.png)
    - [Source Code](https://github.com/zenxha/kpop/blob/main/view/api/app.py)
    - API serves data that drives our site to anyone in the form of JSON
    - API for finding songs is used [here](https://github.com/zenxha/kpop/blob/main/view/komay/classes/getsongs.py#L20-L38) and song data is stored as a class attribute in a jinja variable
    - Jinja variables are then displayed on the front end [here](https://github.com/zenxha/kpop/blob/main/view/komay/templates/getsongs.html#L51-L63)
    - We used our own API a lot of the times when using jquery ajax
## Deployment Section (5pt)
- How It's Made section (+2pt How Its Made, +1pt Visuals)
    - Located in readme, section is labled How Its Made, is what you are currently looking at
- Commercial (+2pt)
    - [LINK TO VIDEO](https://www.youtube.com/watch?v=wpCmiDVF604)
# Code Explanations
## Home page: Displays random user submitted playlists on button click (Komay)
- [Link to RUNTIME](https://kpop.nighthawkcodingsociety.com/ks/)
- [Link to html and js code](https://github.com/zenxha/kpop/blob/main/templates/index.html#L1-L106) 
```html
            <div class="container justify-content-start" style="margin-right: -25%; padding-right:-35%; margin-top: 2%; margin-bottom: 1%;">
                <button onclick="getPlaylist()" type="button" class="btn btn-info">Get random playlist</button>
            </div>
<script>
    const getPlaylist = () => {
        $.getJSON('{{websiteurl}}' + '/api/playlists/random', (data) => {
        document.getElementById("playlist_credits_text").innerHTML = data.username
        document.getElementById("playlist_name").innerHTML = data.playlistname
        //document.getElementById("playlist_text").href = data.url
        document.getElementById("playlist_text").innerHTML = data.url
        document.getElementById("playlist_id").innerHTML = "Playlist ID: " + data.id
        console.log(data)
        });
    }
    const ee = () => {
        console.log('ee')
    }
    console.log('hi')
    function Open() {
        window.open(document.getElementById("playlist_text").innerHTML, "_blank");
    }
</script>
```

## Finding similar song recommendations [API USE!] (Komay)
- This code shows the API and code used to provide a well sorted list of songs similar to the one they type in that the user might enjoy 
- [Link to backend used](https://github.com/zenxha/kpop/blob/main/view/komay/classes/getsongs.py).
- [Link to routing of backend to frontend](https://github.com/zenxha/kpop/blob/main/view/komay/app.py)
- [Link to runtime](http://rubinfamily.dyndns.org:5000/ks/)


API use Code
```python
import requests
import json
import os



# http://ws.audioscrobbler.com/2.0/?method=track.getsimilar&artist=official+hige+dandism&track=pretender&api_key=630846faaf3ca8d5cf4d712e56bd4989&format=json
class Song:
    """Initializer of class takes song info parameters and returns Class Object"""

    def __init__(self, artist, song, sorttype):
        self._artist = artist
        self._song = song
        self._sorttype = sorttype

    @property
    def similar_songs_list(self):
        artist_query_name = self._artist.replace(' ', '+')
        song_query_name = self._song.replace(' ', '+')
        response = requests.get('http://ws.audioscrobbler.com/2.0/?method=track.getsimilar&artist=' + artist_query_name + '&track=' + song_query_name + '&api_key=630846faaf3ca8d5cf4d712e56bd4989&format=json')
        res = response.json()

        res_array = []

        if 'similartracks' in res:
            for song in res['similartracks']['track']:
                res_array.append(song)


            if (self._sorttype == 'playcount'):
                res_array.sort(key=lambda x: x['playcount'], reverse=True)
            if (self._sorttype == 'alphabetical'):
                res_array.sort(key=lambda x: x['name'])
            if self._sorttype == 'similarity':
                res_array = res_array
                print(self._sorttype)

            return res_array
        else:
            return [                {
                "name": "Check your parameters again",
                "playcount": 0,
                "match": 0,
                "url": "https://www.last.fm/music/Official+HIGE+DANdism/_/Shukumei",
                "artist": {
                    "name": "Invalid Artist Link",
                    "url": "https://www.last.fm/music/Official+HIGE+DANdism"
                },
            }]
 ```

## Home Page CSS(Chris)
- This code shows the backend of the form on the home page of the kpop website, which users can see results on anohter part of the index page
- [runtime](https://kpop.nighthawkcodingsociety.com/)
- [Link for homepage playlist submit form](https://github.com/zenxha/kpop/blob/main/views.py#L52-L61)
``` py
@app.route('/', methods=["POST", 'GET'])
def index():
    background = random.choice(backgrounds)
    if request.method == "POST":
        playlistname = request.form["playlistname"]
        username = request.form["username"]
        if username == "mort":
            return render_template('aboutus.html')
        url = request.form["url"]
        submit = Playlist(playlistname=playlistname, username=username, url=url)
        db.session.add(submit)
        db.session.commit()
    return render_template("index.html", background=background, websiteurl=config['websiteURL'])
```


## About The Creators (Charlie)
- This code shows the page that users can access to find out more about the creators.
- [Runtime](http://rubinfamily.dyndns.org:5000/about)
- [Dataslides](https://github.com/zenxha/kpop/blob/main/templates/aboutus.html#L28-L34) are used to allow users easy and smooth access to all profiles.
- [Javascript/Styling](https://github.com/zenxha/kpop/blob/main/templates/aboutus.html#L99-L139) is placed near the bottom, where it helps enhance the page's visuals
- [Route](https://github.com/zenxha/kpop/blob/main/views.py#L98-L100) that leads to this page
```html
{% extends "base2.html" %}
{% block header %}

<!-- ABOUT US -->
<!-- body -->
<div class="main-layout" style="background-color:transparent;">

    <!--Our  Clients -->
    <div id="plant" class="section_Clients layout_padding padding_bottom_0">
        <div class="container">
            <div class="row">
                <div class="col-md-12 ">
                    <div class="titlepage" style="color: white; padding-top: 5%;">
                        <h2> About The Creators</h2>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <div class="section Clients_2 layout_padding padding-top_0">
        <div class="container">
            <div class="row">
                <div class="col-sm-12">

                    <div id="testimonial" class="carousel slide" data-ride="carousel">

                        <!-- Indicators -->
                        <ul class="carousel-indicators">
                            <li data-target="#testimonial" data-slide-to="0" class="active"></li>
                            <li data-target="#testimonial" data-slide-to="1"></li>
                            <li data-target="#testimonial" data-slide-to="2"></li>
                            <li data-target="#testimonial" data-slide-to="3"></li>
                            <li data-target="#testimonial" data-slide-to="4"></li>
                        </ul>

                        <!-- The slideshow -->
                        <div class="carousel-inner">
                            <div class="carousel-item active">
                                <div class="titlepage">
                                    <div class="john">
                                        <div class="john_image"><img src="/static/images/czpfp.gif" style="max-width:100%; padding-left: 40%;"></div>
                                        <div class="john_text" style="color: white">Charlie Zhu</div>
                                        <p class="lorem_ipsum_text" style="color: white">"I am a junior at Del Norte High School. I was born in San Diego
                                            and am currently 16 years old. I have an older sister who is in college.
                                            Some things I like to do in my free time are play video games and run."</p>
                                    </div>
                                </div>
                            </div>
                            <div class="carousel-item">
                                <div class="titlepage">
                                    <div class="john">
                                        <div class="john_image"><img src="https://media1.tenor.com/images/14de8c9e35e27ac8e91f532e8d079677/tenor.gif?itemid=17355571" style="max-width:100%; padding-left: 30%;"></div>
                                        <div class="john_text" style="color: white">Komay Sugiyama</div>
                                        <p class="lorem_ipsum_text" style="color: white">"I am a 17 year old Junior at Del Norte High School. I also really like music. My favorite geners are R&B, Jazz, jpop, kpop, indie, rock, funk, soul and hiphop. My favorite band is Official HIGE DANdism, you should check them out too"</p>
                                    </div>
                                </div>
                            </div>
                            <div class="carousel-item">
                                <div class="titlepage">
                                    <div class="john">
                                        <div class="john_image"><img src="/static/images/devampfp.gif" style="max-width:100%; padding-left: 35%;"></div>
                                        <div class="john_text" style="color: white">Devam Shrivastava</div>
                                        <p class="lorem_ipsum_text" style="color: white">"I am a junior at Del Norte High School. I am 17 years old and I was born in Scripps Ranch. In my free time I like to watch anime and play video games with my friends. My favorite anime is Jujutsu Kaisen."</p>
                                    </div>
                                </div>
                            </div>
                            <div class="carousel-item">
                                <div class="titlepage">
                                    <div class="john">
                                        <div class="john_image"><img src="/static/images/Chris.png" style="max-width:100%; padding-left: 40%;"></div>
                                        <div class="john_text" style="color: white">Chris Rubin</div>
                                        <p class="lorem_ipsum_text" style="color: white">"I am a junior at Del Norte High School. I am 18 years old and I was born in Pomerado. I have 10 siblings, 6 sisters and 4 brothers. Four of them have graduated from college and two of them are in college currently. In my free time I like playing video games, hanging out with friends, skateboarding, watching anime, and my favorite anime is Black Clover."</p>
                                    </div>
                                </div>
                            </div>
                            <div class="carousel-item">
                                <div class="titlepage">
                                    <div class="john">
                                        <div class="john_image"><img src="/static/images/deeppfp.png" style="max-width:100%; padding-left: 40%;"></div>
                                        <div class="john_text" style="color: white">Eshaan Parlikar</div>
                                        <p class="lorem_ipsum_text" style="color: white">"I am a 17 year old junior at Del Norte High School who was born in San Diego. I have two older sisters, one who currently attends Abraxas and the other recently graduating from NYU with a politics major. Currently, I enjoy playing video games and drumming, and my favorite anime is Fullmetal Alchemist: Brotherhood."</p>
                                    </div>
                                </div>
                            </div>
                            <a class="carousel-control-prev" href="#testimonial" data-slide="prev"><span class="carousel-control-prev-icon"></span></a> <a class="carousel-control-next" href="#testimonial" data-slide="next"><span class="carousel-control-next-icon"></span></a></div>



                    </div>
                </div>
            </div>
        </div>
    </div>
</div>
</div>
<!-- end Our  Clients -->
<!-- END OF ABOUT US -->
<!-- Javascript files-->
<script src="js/jquery.min.js"></script>
<script src="js/popper.min.js"></script>
<script src="js/bootstrap.bundle.min.js"></script>
<script src="js/jquery-3.0.0.min.js"></script>
<script src="js/plugin.js"></script>
<script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
<!-- sidebar -->
<script src="js/jquery.mCustomScrollbar.concat.min.js"></script>
<script src="js/custom.js"></script>
<!-- javascript -->
<script src="js/owl.carousel.js"></script>
<script src="https:cdnjs.cloudflare.com/ajax/libs/fancybox/2.1.5/jquery.fancybox.min.js"></script>
<script>
    $(document).ready(function(){
        $(".fancybox").fancybox({
            openEffect: "none",
            closeEffect: "none"
        });

        $(".zoom").hover(function(){

            $(this).addClass('transition');
        }, function(){

            $(this).removeClass('transition');
        });
    });

</script>
</div>

<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
</div>
<style>
    body,html{
        overflow-y: hidden;
    }
</style>
{% endblock %}
```
## Database Functions (Devam)
- Controls the inputs of the form
- Holds all the URL's to the spotify playlist links that people input
```python
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


# Function that initializes the db and creates the tables
def db_init(app):
    db.init_app(app)

    # Creates the logs tables if the db doesnt already exist
    with app.app_context():
        db.create_all()
        print('h')

class Playlist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    playlistname = db.Column(db.Text, nullable=False)
    username = db.Column(db.Text, nullable=False)
    url = db.Column(db.Text, nullable=False)

class MV(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    songname = db.Column(db.Text, nullable=False)
    username = db.Column(db.Text, nullable=False)
    url = db.Column(db.Text, nullable=False)
```
## Rating Page (Eshaan)
- The HTML and CSS used here create a page where users can give ratings for the website.
- [Runtime](https://kpop.nighthawkcodingsociety.com/rate)
- [CSS](https://github.com/zenxha/kpop/blob/main/templates/rate.html#L55-L193) that includes font API and hover mechanism
- [HTML](https://github.com/zenxha/kpop/blob/main/templates/rate.html#L1-L54) that creates outline for stars
- [Route](https://github.com/zenxha/kpop/blob/main/views.py#L102-L104) to page
```html
<html lang="en" dir="ltr">
<head>
  <meta charset="utf-8">
  <title>Rate our website!</title>
  <link rel="stylesheet" href="style.css">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css"/>
</head>
<body>
<div class="container">
  <div class="post">
    <div class="text">
      Thanks for rating us!
    </div>
    <div class="edit">

    </div>
  </div>
  <div class="star-widget">
    <input type="radio" name="rate" id="rate-5">
    <label for="rate-5" class="fas fa-star"></label>
    <input type="radio" name="rate" id="rate-4">
    <label for="rate-4" class="fas fa-star"></label>
    <input type="radio" name="rate" id="rate-3">
    <label for="rate-3" class="fas fa-star"></label>
    <input type="radio" name="rate" id="rate-2">
    <label for="rate-2" class="fas fa-star"></label>
    <input type="radio" name="rate" id="rate-1">
    <label for="rate-1" class="fas fa-star"></label>
    <form action="#">
      <header></header>
      <div class="textarea">
        <textarea cols="30" placeholder="Describe your experience.."></textarea>
        <br />
        <div class="btn">
          <button type="submit">Post</button>
        </div>
        <script>
         const btn = document.querySelector("button");
         const post = document.querySelector(".post");
         const widget = document.querySelector(".star-widget");
         const editBtn = document.querySelector(".edit");
         btn.onclick = ()=>{
           widget.style.display = "none";
           post.style.display = "block";
           editBtn.onclick = ()=>{
             widget.style.display = "block";
             post.style.display = "none";
           }
           return false;
         }
      </script>
</body>
</html>

<style>
@import url('https://fonts.googleapis.com/css?family=Poppins:400,500,600,700&display=swap');
*{
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    font-family: 'Poppins', sans-serif;
}
html,body{
    display: grid;
    height: 100%;
    place-items: center;
    text-align: center;
    background: #000;
}
.container{
    position: relative;
    width: 400px;
    background: #111;
    padding: 20px 30px;
    border: 1px solid #444;
    border-radius: 5px;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-direction: column;
}
.container .post{
    display: none;
}
.container .text{
    font-size: 25px;
    color: #666;
    font-weight: 500;
}
.container .edit{
    position: absolute;
    right: 10px;
    top: 5px;
    font-size: 16px;
    color: #666;
    font-weight: 500;
    cursor: pointer;
}
.container .edit:hover{
    text-decoration: underline;
}
.container .star-widget input{
    display: none;
}
.star-widget label{
    font-size: 40px;
    color: #444;
    padding: 10px;
    float: right;
    transition: all 0.2s ease;
}
input:not(:checked) ~ label:hover,
input:not(:checked) ~ label:hover ~ label{
    color: #fd4;
}
input:checked ~ label{
    color: #fd4;
}
input#rate-5:checked ~ label{
    color: #fe7;
    text-shadow: 0 0 20px #952;
}
#rate-1:checked ~ form header:before{
    content: "Immediate update needed! ";
}
#rate-2:checked ~ form header:before{
    content: "Lacks some features or is a little too buggy. ";
}
#rate-3:checked ~ form header:before{
    content: "It's alright, nothing too special.";
}
#rate-4:checked ~ form header:before{
    content: "Pretty good, but I wish there was one more thing.";
}
#rate-5:checked ~ form header:before{
    content: "It's perfect! ";
}
.container form{
    display: none;
}
input:checked ~ form{
    display: block;
}
form header{
    width: 100%;
    font-size: 25px;
    color: #fe7;
    font-weight: 500;
    margin: 5px 0 20px 0;
    text-align: center;
    transition: all 0.2s ease;
}
form .textarea{
    height: 100px;
    width: 100%;
    overflow: hidden;
}
form .textarea textarea{
    height: 100%;
    width: 100%;
    outline: none;
    color: #eee;
    border: 1px solid #333;
    background: #222;
    padding: 10px;
    font-size: 17px;
    resize: none;
}
.textarea textarea:focus{
    border-color: #444;
}
form .btn{
    height: 45px;
    width: 100%;
    margin: 15px 0;
}
form .btn button{
    height: 100%;
    width: 100%;
    border: 1px solid #444;
    outline: none;
    background: #222;
    color: #999;
    font-size: 17px;
    font-weight: 500;
    text-transform: uppercase;
    cursor: pointer;
    transition: all 0.3s ease;
}
form .btn button:hover{
    background: #1b1b1b;
}
</style>
```


## Our Idea Including Support for Individuals (Routes, Blueprints etc.)
- We aim for a simple and clean site that contains everything about kpop and music in general. On the site you???ll be able to upload your favorite songs, and explore other people's musical interests.
- The site will contain blueprints and seperate routes that will directly lead to each of our individual work.
- Here is one such example:
![image](https://user-images.githubusercontent.com/72889453/112710377-dfb26a00-8e7d-11eb-8df4-5c0594f5edeb.png)
