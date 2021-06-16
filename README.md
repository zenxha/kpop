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
- [Quote Page](https://p3cowboys.nighthawkcodingsociety.com/quote/) (+0.5pt User interaction, +0.5pt Technical, +1pt Fun)
    - Quote page demonstrates usage and display of [online APIs](https://github.com/TMarwah/P3Cowboys/blob/e641f16f5d17751b83b95b243ae1013c0167d6c7/main.py#L31)
    - User can refresh the page to get a new response each time
    - Quotes add to the theme of the project by giving users inspirational quotes to help with their buisness ideas
- [Upload Page](https://github.com/TMarwah/P3Cowboys/blob/main/Cowboys/Allen/templates/upload.html) (+0.5pt User interaction, +0.5pt Technical, +1pt Fun)
    - Upload page demonstrates usage and display of user interaction 
    - User can upload their websites advertisement and then it will be viewable from the "Browse" page
    - This relates to the theme as it is the main point of interaction for the advertisements to be posted
- Database (+0.5pt User interaction, +0.5pt Technical)
    - This code shows the database that takes the user input from the upload page and connects it to the browse page.
    - [Link to full code for app.py](https://github.com/TMarwah/P3Cowboys/blob/main/Cowboys/Allen/app.py)
    - [Link to database setup part 1](https://github.com/TMarwah/P3Cowboys/blob/main/Cowboys/Allen/model.py)
    - [Link to database setup part 2](https://github.com/TMarwah/P3Cowboys/blob/main/Cowboys/Allen/db.py)
    - [Link for browse page](https://github.com/TMarwah/P3Cowboys/blob/main/Cowboys/Allen/templates/browse.html)
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

## Login Page (Tanmay)
- This code shows the login page that accepts a username and password then identifies the user
- [Link to full code for app.py](https://github.com/TMarwah/P3Cowboys/blob/main/Cowboys/Tanmay/app.py)
- [Link for login page](https://github.com/TMarwah/P3Cowboys/blob/main/Cowboys/Tanmay/templates/login.html)
```
from flask import Blueprint
from flask import render_template, request
from Cowboys.Tanmay.tanmayminilab import  Counters

Cowboys_Tanmay_bp = Blueprint('Cowboys_Tanmay', __name__,
                              template_folder='templates',
                              static_folder='static', static_url_path='assets')

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

@Cowboys_Tanmay_bp.route('/login', methods=["POST", "GET"])
def login_route():
    logform = LoginForm()
    if logform.validate_on_submit():
        user = User.query.filter_by(username=logform.username.data).first()
        if user is None or not user.check_password(logform.password.data):
            flash("Login Failed")
            return redirect("/login")
        login_user(user)
        flash("Login Successful!")
        if logform.username.data == "secret":
            return redirect("/secret")
        nextpage = request.args.get("next")
        if not nextpage or url_parse(nextpage).netloc != '':
            return redirect('/')
        return redirect(nextpage)
    else:
        return render_template("login.html", form = logform)

@Cowboys_Tanmay_bp.route('/minilab', methods=["POST", "GET"])
def minilab():
    if(request.method == 'POST'):
        sentence = request.form.get('sentence')
        sentencesort = request.form.get('sentencesort')
        input = sentence
        input2 = sentencesort
        return render_template("tanmayminilab.html",wordcount = Counters(input).wordcount(),
                               lettercount = Counters(input).lettercount(), sorted = Counters(input2).bubblesort())

    return render_template("tanmayminilab.html",wordcount = Counters(2).wordcount(),
                           lettercount = Counters(2).lettercount(), sorted = Counters(2).bubblesort())
```

## Database (Marc)
- This code shows the database that takes the user input from the upload page and connects it to the browse page.
- [Link to full code for app.py](https://github.com/TMarwah/P3Cowboys/blob/main/Cowboys/Allen/app.py)
- [Link to database setup part 1](https://github.com/TMarwah/P3Cowboys/blob/main/Cowboys/Allen/model.py)
- [Link to database setup part 2](https://github.com/TMarwah/P3Cowboys/blob/main/Cowboys/Allen/db.py)
- [Link for browse page](https://github.com/TMarwah/P3Cowboys/blob/main/Cowboys/Allen/templates/browse.html)
```
@Cowboys_minilab1_bp.route('/cowboys/minilab1/browse')
def browse():
    backgrounds = ["https://cdn.discordapp.com/attachments/784178874303905792/818606015494094868/812382.png"]
    review_query = Review.query.all()
    reviews = []

    for review in review_query:
        websiteurl = url_for('get_img', id=review.id)

        review_dict = {
            'id': review.id,
            'username': review.username,
            'content': review.content,
            'image':  websiteurl
        }
        reviews.append(review_dict)
    return render_template("browse.html", reviews=reviews, background=random.choice(backgrounds))
    
@Cowboys_minilab1_bp.route('/cowboys/minilab1/upload', methods=["POST", 'GET'])
def upload():
    background = random.choice(backgrounds)
    if request.method == "POST":
        name = request.form["username"]
        content = request.form["content"]
        image = request.files.get('img')
        if not image:
            return 'bad news ur image did not make it to our servers :((((', 400

        filename = secure_filename(image.filename)
        mimetype = image.mimetype
        if not filename or not mimetype:
            return 'Bad upload', 400

        review = Review(username=name, content=content, img=image.read(), filename=filename, mimetype=mimetype)
        db.session.add(review)
        db.session.commit()
        return redirect(url_for("browse.html"))
    return render_template("upload.html", background=background)
    
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
