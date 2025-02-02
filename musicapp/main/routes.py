from flask import render_template, request, Blueprint
from flask_login import current_user, login_required
from musicapp.models import Song, Playlist
from musicapp.songs.forms import SearchForm

main = Blueprint('main', __name__)


@main.context_processor
def layout():
    form = SearchForm()
    return dict(form=form)


@main.route('/')
@main.route('/home')
@login_required
def home():
    page = request.args.get('page', 1, type=int)
    songs = Song.query.filter_by(
        owner_id=current_user.id).paginate(page=page, per_page=12)
    return render_template('home.html', songs=songs)


@main.route('/collection')
@login_required
def collection():
    songs_page = request.args.get('songs_page', 1, type=int)
    playlists_page = request.args.get('playlists_page', 1, type=int)
    songs = Song.query.paginate(page=songs_page, per_page=12)
    playlists = Playlist.query.paginate(page=playlists_page, per_page=5)
    return render_template('collection.html', title='All Songs', songs=songs, playlists=playlists)
