![image](http://owo.whats-th.is/BoLbteQ.jpg)
# Kpop Music Site!
Group Project for tri3!
### Links
- [Project Board](https://github.com/zenxha/kpop/projects/1)
- [Deployed Website](http://rubinfamily.dyndns.org:5000/)
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
- [Find Similar Songs Page](https://p3cowboys.nighthawkcodingsociety.com/quote/) (+0.5pt User interaction, +0.5pt Technical, +1pt Fun)
    - This page demonstrates usage and display of [online APIs that take parametrs](https://github.com/zenxha/kpop/blob/main/view/komay/classes/getsongs.py#L20)
    - User can input an Artist and the Track name as well as how they want the list sorted. The response displays song cards that the user can listen to. These cares provide info such as wear to listen and popularity info.
    - As a music-focused site, this page helps users find new songs if they ever want new songs that are similar to the ones they are currently listening to
- [Home page](https://github.com/TMarwah/P3Cowboys/blob/main/Cowboys/Allen/templates/upload.html) (+0.5pt*2 User interaction, +0.5pt Technical, +1pt Fun)
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
    - [Each folder](https://github.com/TMarwah/P3Cowboys/tree/e641f16f5d17751b83b95b243ae1013c0167d6c7/Cowboys) is labled with the corresponding member to indicate their individual blueprint
- Technicals (+1pt 2 Technicals)
    - Each minilab utilizes [classes](https://github.com/TMarwah/P3Cowboys/blob/c44d5b580d1db0821e71453ef1be321120e6a9fd/Cowboys/Allen/minilab1.py#L2-L32) in order to pass in [parameters](https://github.com/TMarwah/P3Cowboys/blob/c44d5b580d1db0821e71453ef1be321120e6a9fd/Cowboys/Allen/app.py#L130) that cause different functions to run 
    - 
## API Section (3pt)
- [API and Receiving](https://p3cowboys.nighthawkcodingsociety.com/quote/) (+2 Receive and API, +1 Visual)
    - API for quotes is used [here](https://github.com/TMarwah/P3Cowboys/blob/e641f16f5d17751b83b95b243ae1013c0167d6c7/main.py#L31) and the author and quote is stored as jinja variables
    - Jinja variables are then displayed on the front end [here](https://github.com/TMarwah/P3Cowboys/blob/d829f25775a369d12d43b9ad72c38f556e9b9064/templates/quotepage.html#L140-L150)
    - Used png of quotes to emphasize the quote and highlighted text to be easily seen, with author cited at bottom right as well
## Deployment Section (5pt)
- How It's Made section (+2pt How Its Made, +1pt Visuals)
    - Located in readme, section is labled How Its Made, is what you are currently looking at
- Commercial (+2pt)
    - [Link to video](https://www.youtube.com/watch?v=XnYaSJoKWxE&ab_channel=Purplebears)
# Code Explanations
## Home page: Displays random user submitted playlists on button click (Komay)
- [Link to RUNTIME](http://rubinfamily.dyndns.org:5000/)
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
- This CSS organizes the webpage to include a submit form and the card that Komay uses
- [Link to full css code for index.html](https://github.com/zenxha/kpop/blob/main/static/formstyle.css)
- [Link for home page html file](https://github.com/zenxha/kpop/blob/main/templates/index.html)
```
<div class="container">
    <div class="row justify-content-end">
        <div class="col-sm-4">
            <div class="container justify-content-start" style="margin-right: -25%; padding-right:-35%; margin-top: 2%; margin-bottom: 1%;">
                <button onclick="getPlaylist()" type="button" class="btn btn-info">Get random playlist</button>
            </div>
            <div class="card text-white card-has-bg click-col mx-auto" id="playlist_card" href="#" >
                <img class="card-img d-none" src="https://source.unsplash.com/600x900/?computer,design" alt="Goverment Lorem Ipsum Sit Amet Consectetur dipisi?">
                <div class="card-img-overlay d-flex flex-column">
                    <div class="card-body">
                        <small class="card-meta mb-2" id="playlist_id" >Playlist ID:</small>
                        <h4 class="card-title mt-0" id="playlist_name">Click the button to get a playlist!<a class="text-white" href="#"></a></h4>
                        <a onclick="Open()" id="playlist_text"></a>
                    </div>
                    <div class="card-footer">
                        <div class="media">
                            <img class="mr-3 rounded-circle" src="https://moonvillageassociation.org/wp-content/uploads/2018/06/default-profile-picture1.jpg" alt="Generic placeholder image" style="max-width:50px">
                            <div class="media-body">
                                <h6 class="my-0 text-white d-block">Submitted by</h6>
                                <h6 id="playlist_credits_text"></h6>
                            </div>
                        </div>
                    </div>
                </div>
            </div></div>
    </div>
    <div class="row justify-content-start">
        <div class="col-md-12">
            <body data-new-gr-c-s-check-loaded="14.1012.0" data-gr-ext-installed="">
                    <div class="container-contact2" style="margin-left:-20%; margin-top: -42%;min-height: 500px;width: 60%;" >
                        <div class="wrap-contact2">
                            <form class="contact2-form validate-form" name="playlistform" method='post' onsubmit="return validate()" >
                            <span class="contact2-form-title">
                                Submit your playlist
                            </span>
                                <div class="wrap-input2 validate-input" data-validate="Playlist Name is Required">
                                    <input class="input2" type="text" name="playlistname" id="playlistname" required>
                                    <span class="focus-input2" data-placeholder="Playlist Name"></span>
                                </div>
                                <div class="wrap-input2 validate-input" data-validate="">
                                    <input class="input2" type="text" name="username" id="username" required>
                                    <span class="focus-input2" data-placeholder="Your Username"></span>
                                </div>
                                <div class="wrap-input2 validate-input" data-validate="Playlist URL is Required">
                                    <textarea class="input2" name="url" required></textarea>
                                    <span class="focus-input2" data-placeholder="https://open.spotify.com/playlist/4CuSTeoPQlN3ltgbaJCfrX?si=ab3d0295bc334f69"></span>
                                </div>
                                <div class="container-contact2-form-btn">
                                    <div class="wrap-contact2-form-btn">
                                        <div class="contact2-form-bgbtn"></div>
                                        <button class="contact2-form-btn">
                                            Submit Playlist
                                        </button>
                                    </div>
                                </div>
                            </form>
                        </div>
                    </div>
            </body>
        </div>
    </div>
</div>
```

## About The Creators (Charlie)
- This code shows the page that users can access to find out more about the creators.
- [Runtime](http://rubinfamily.dyndns.org:5000/about)
- [Dataslides](https://github.com/zenxha/kpop/blob/main/templates/aboutus.html#L28-L34) are used to allow users easy and smooth access to all profiles.
- [Javascript/Styling](https://github.com/zenxha/kpop/blob/main/templates/aboutus.html#L99-L139) is placed near the bottom, where it helps enhance the page's visuals
- [Route](https://github.com/zenxha/kpop/blob/main/views.py#L98-L100) that leads to this page
```
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
## Feedback Page (Billy)
- This code snippet shows the Usage of Get and Post to retrieve feedback and post it on the response page.
- [Link to full code of app.py](https://github.com/TMarwah/P3Cowboys/blob/19fdd8cef62f8a8a662cf7a78a3730db92d346da/Cowboys/William/app.py#L1-L75)(Connects feedback/response pages together using Get and Post)
- [link to full code of feedback page](https://github.com/TMarwah/P3Cowboys/blob/d97d3988f9a8f043502862bf08fa68c03e42bae4/Cowboys/William/templates/feedback.html#L1-L106)(Feedback page html shows user input)
- [link to full code of response page](https://github.com/TMarwah/P3Cowboys/blob/7805f62499a5afa35aff51be5356c4b1cb0f3f20/Cowboys/William/templates/response.html#L1-L152)(Response page html shows jinja funtions)
```
@Cowboys_William_bp.route("/feedback", methods=["POST", "GET"])
def feedback():
    if request.method == 'POST':
        name = request.form.get('name')
        comment = request.form.get('comment')
        input1 = name
        input2 = comment
        return render_template("response.html", name=name, comment=comment, input1=input1, input2=input2)
    return render_template("feedback.html")
```




## Our Idea Including Support for Individuals (Routes, Blueprints etc.)
- We aim for a simple and clean site that contains everything about kpop and music in general. On the site you’ll be able to upload your favorite songs, and explore other people's musical interests.
- The site will contain blueprints and seperate routes that will directly lead to each of our individual work.
- Here is one such example:
![image](https://user-images.githubusercontent.com/72889453/112710377-dfb26a00-8e7d-11eb-8df4-5c0594f5edeb.png)
