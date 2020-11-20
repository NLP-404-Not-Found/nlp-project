"""
A module for obtaining repo readme and language data from the github API.
Before using this module, read through it, and follow the instructions marked TODO.
After doing so, run it like this:
    python acquire.py
To create the `data.json` file that contains the data.
"""
import os
import json
from typing import Dict, List, Optional, Union, cast
import requests

from env import github_token, github_username

# TODO: Make a github personal access token.
#     1. Go here and generate a personal access token https://github.com/settings/tokens
#        You do _not_ need select any scopes, i.e. leave all the checkboxes unchecked
#     2. Save it in your env.py file under the variable `github_token`
# TODO: Add your github username to your env.py file under the variable `github_username`
# TODO: Add more repositories to the `REPOS` list below.

REPOS = [
    "gocodeup/codeup-setup-script",
    "gocodeup/movies-application",
    "torvalds/linux",
    "beetbox/beets",
    "scottschiller/SoundManager2",
    "CreateJS/SoundJS",
    "musescore/MuseScore",
    "tomahawk-player/tomahawk",
    "cashmusic/platform",
    "mopidy/mopidy",
    "AudioKit/AudioKit",
    "Soundnode/soundnode-app",
    "gillesdemey/Cumulus",
    "metabrainz/picard",
    "overtone/overtone",
    "sonic-pi-net/sonic-pi",
    "nukeop/nuclear",
    "twbs/bootstrap",
    "animate-css/animate.css",
    "designmodo/Flat-UI",
    "h5bp/html5-boilerplate",
    "foundation/foundation-sites",
    "Modernizr/Modernizr",
    "twbs/ratchet",
    "atlemo/SubtlePatterns",
    "fivethirtyeight/data",
    "datadesk/notebooks",
    "newsapps/beeswithmachineguns",
    "voxmedia/meme",
    "censusreporter/censusreporter",
    "nprapps/app-template",
    "TimeMagazineLabs/babynames",
    "guardian/frontend",
    "dukechronicle/chronline",
    "BloombergMedia/whatiscode",
    "aduggin/accessibility-fails",
    "Heydon/REVENGE.CSS",
    "aseprite/aseprite",
    "piskelapp/piskel",
    "jvalen/pixel-art-react",
    "kitao/pyxel",
    "cloudhead/rx",
    "godotengine/godot",
    "turbulenz/turbulenz_engine",
    "Gamua/Starling-Framework",
    "jMonkeyEngine/jmonkeyengine",
    "SFTtech/openage",
    "MonoGame/MonoGame",
    "gabrielecirulli/2048",
    "ellisonleao/clumsy-bird",
    "mozilla/BrowserQuest",
    "AlexNisnevich/untrusted",
    "doublespeakgames/adarkroom",
    "Hextris/hextris",
    "Greenstand/Development-Overview",
    "GliaX/Stethoscope",
    "HospitalRun/hospitalrun-frontend",
    "get-alex/alex",
    "coralproject/talk",
    "hotosm/tasking-manager",
    "OptiKey/OptiKey",
    "ifmeorg/ifme",
    "RefugeRestrooms/refugerestrooms",
    "hurricane-response/florence-api",
    "Terrastories/terrastories",
    "rubyforgood/diaper",
    "ebimodeling/ghgvc",
    "raksha-life/rescuekerala",
    "Data4Democracy/ethics-resources",
    "civicdata/civicdata.github.io",
    "EFForg/action-center-platform",
    "fightforthefuture/battleforthenet",
    "fightforthefuture/battleforthenet-widget",
    "mariechatfield/call-my-congress",
    "mozilla/advocacy.mozilla.org",
    "panxzz/NN-blackout",
    "j2kao/fcc_nn_research",
    "berkmancenter/internet_monitor",
    "ahmia/ahmia-site",
    "apache/spark",
    "apache/hadoop",
    "jbhuang0604/awesome-computer-vision",
    "GSA/data",
    "GoogleTrends/data",
    "nationalparkservice/data",
    "beamandrew/medical-data",
    "src-d/awesome-machine-learning-on-source-code",
    "igrigorik/decisiontree",
    "keon/awesome-nlp",
    "openai/gym",
    "aikorea/awesome-rl",
    "umutisik/Eigentechno",
    "jpmckinney/tf-idf-similarity",
    "scikit-learn-contrib/lightning",
    "gwding/draw_convnet",
    "scikit-learn/scikit-learn",
    "tensorflow/tensorflow",
    "Theano/Theano",
    "shogun-toolbox/shogun",
    "davisking/dlib",
    "apache/predictionio",
    "deepmind/pysc2",
    "gokceneraslan/awesome-deepbio",
    "buriburisuri/ByteNet",
    "josephmisiti/awesome-machine-learning",
    "ujjwalkarn/Machine-Learning-Tutorials",
    "ChristosChristofidis/awesome-deep-learning",
    "fastai/courses",
    "Yorko/mlcourse.ai",
    "jtoy/awesome-tensorflow",
    "nlintz/TensorFlow-Tutorials",
    "pkmital/tensorflow_tutorials",
    "tomgenoni/cssdig",
    "heynemann/pyccuracy",
    "tmm1/gdb.rb",
    "binaryage/firelogger.py",
    "fbzhong/sublime-jslint",
    "epio/mantrid",
    "evannuil/aws-snapshot-tool",
    "nlloyd/SubliminalCollaborator",
    "rayokota/generator-angular-flask",
    "samuel/kokki",
    "tspurway/hustle",
    "jamesgolick/timeline_fu",
    "bigbinary/admin_data",
    "techiferous/tabulous",
    "pelle/oauth",
    "ezmobius/chef-deploy",
    "meldium/breach-mitigation-rails",
    "wvanbergen/state_machine-audit_trail",
    "anthonyshort/stitch-css",
    "bpot/poseidon",
    "alindeman/zonebie",
    "bigbinary/admin_data",
    "hashrocket/hr-til",
    "nesquena/dante",
    "leppert/remotipart",
    "leshill/resque_spec",
    "berkshelf/ridley",
    "marianoguerra/rst2html5",
    "propublica/landline",
    "lmaccherone/sb-admin-2-meteor",
    "rikitanone/drunken-parrot-flat-ui",
    "joeferraro/MavensMate-Desktop",
    "osis/simple_fb_html5_sidebar",
    "matthutchinson/paging_keys_js",
    "craigfrancis/dev-security",
    "nealrs/readsure",
    "egoist/data-tip.css",
    "Nemo64/meteor-bootstrap",
    "beakerbrowser/explore",
    "StarterSquad/ngseed",
    "MicrosoftLearning/Bootstrap-edX",
    "dmfrancisco/activo",
    "treeder/go-polymer",
    "mavenecommerce/mbootstrap",
    "fdisotto/SlimBlog",
    "lashford/modern-web-template",
    "gastonmorixe/MessengerNative",
    "aliceatlas/hexagen",
    "ldiqual/tesseract-ios-lib",
    "mangecoeur/ipython-desktop",
    "Slashed/daemon.node",
    "patriciogonzalezvivo/KinectCoreVision",
    "highpower/xiva",
    "shmuelyr/CaptainHook",
    "kylemcdonald/Makerbot",
    "KoffeinFlummi/AGM",
    "kellabyte/rewind",
    "naibaf7/libdnn",
    "vincentriemer/yoga-dom",
    "mana/manaserv",
    "ROCmSoftwarePlatform/hipCaffe",
    "google/crunchy",
    "j-cube/multiverse",
    "ArbiterLib/Arbiter",
    "laurentlb/Ctrl-Alt-Test",
    "memo/ofxKinect-demos",
    "lluisgomez/text_extraction",
    "macmade/FaceDetect"
]

headers = {"Authorization": f"token {github_token}", "User-Agent": github_username}


if headers["Authorization"] == "token " or headers["User-Agent"] == "":
    raise Exception(
        "You need to follow the instructions marked TODO in this script before trying to use it"
    )

def github_api_request(url: str) -> Union[List, Dict]:
    response = requests.get(url, headers=headers)
    response_data = response.json()
    if response.status_code != 200:
        raise Exception(
            f"Error response from github api! status code: {response.status_code}, "
            f"response: {json.dumps(response_data)}"
        )
    return response_data

def get_repo_language(repo: str) -> str:
    url = f"https://api.github.com/repos/{repo}"
    repo_info = github_api_request(url)
    if type(repo_info) is dict:
        repo_info = cast(Dict, repo_info)
        return repo_info.get("language", None)
    raise Exception(
        f"Expecting a dictionary response from {url}, instead got {json.dumps(repo_info)}"
    )


def get_repo_contents(repo: str) -> List[Dict[str, str]]:
    url = f"https://api.github.com/repos/{repo}/contents/"
    contents = github_api_request(url)
    if type(contents) is list:
        contents = cast(List, contents)
        return contents
    raise Exception(
        f"Expecting a list response from {url}, instead got {json.dumps(contents)}"
    )


def get_readme_download_url(files: List[Dict[str, str]]) -> str:
    """
    Takes in a response from the github api that lists the files in a repo and
    returns the url that can be used to download the repo's README file.
    """
    for file in files:
        if file["name"].lower().startswith("readme"):
            return file["download_url"]
    return ""


def process_repo(repo: str) -> Dict[str, str]:
    """
    Takes a repo name like "gocodeup/codeup-setup-script" and returns a
    dictionary with the language of the repo and the readme contents.
    """
    contents = get_repo_contents(repo)
    readme_download_url = get_readme_download_url(contents)
    if readme_download_url == "":
        readme_contents = None
    else:
        readme_contents = requests.get(readme_download_url).text
    return {
        "repo": repo,
        "language": get_repo_language(repo),
        "readme_contents": readme_contents,
    }


def scrape_github_data() -> List[Dict[str, str]]:
    """
    Loop through all of the repos and process them. Returns the processed data.
    """
    return [process_repo(repo) for repo in REPOS]


if __name__ == "__main__":
    data = scrape_github_data()
    json.dump(data, open("data.json", "w"), indent=1)