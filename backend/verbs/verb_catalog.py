"""
The 50 most common irregular English verbs with their three forms, and the scene file that draws each one.
"""
from dataclasses import dataclass

FORM_LABELS = ("infinitive", "past", "past participle")
FORM_FILE_NAMES = ("infinitive", "past", "participle")


@dataclass(frozen=True)
class IrregularVerb:
    key: str
    infinitive: str
    past: str
    past_participle: str
    scene_module: str

    @property
    def forms(self):
        return (self.infinitive, self.past, self.past_participle)


def _verb(
    key,
    past,
    past_participle,
    scene_module,
):
    return IrregularVerb(key=key, infinitive=key, past=past, past_participle=past_participle, scene_module=scene_module)


IRREGULAR_VERBS = [
    _verb(key="go", past="went", past_participle="gone", scene_module="scenes_motion"),
    _verb(key="come", past="came", past_participle="come", scene_module="scenes_motion"),
    _verb(key="run", past="ran", past_participle="run", scene_module="scenes_motion"),
    _verb(key="fall", past="fell", past_participle="fallen", scene_module="scenes_motion"),
    _verb(key="rise", past="rose", past_participle="risen", scene_module="scenes_motion"),
    _verb(key="leave", past="left", past_participle="left", scene_module="scenes_motion"),
    _verb(key="drive", past="drove", past_participle="driven", scene_module="scenes_motion"),
    _verb(key="stand", past="stood", past_participle="stood", scene_module="scenes_motion"),
    _verb(key="sit", past="sat", past_participle="sat", scene_module="scenes_motion"),
    _verb(key="begin", past="began", past_participle="begun", scene_module="scenes_motion"),
    _verb(key="know", past="knew", past_participle="known", scene_module="scenes_mind"),
    _verb(key="think", past="thought", past_participle="thought", scene_module="scenes_mind"),
    _verb(key="understand", past="understood", past_participle="understood", scene_module="scenes_mind"),
    _verb(key="mean", past="meant", past_participle="meant", scene_module="scenes_mind"),
    _verb(key="feel", past="felt", past_participle="felt", scene_module="scenes_mind"),
    _verb(key="choose", past="chose", past_participle="chosen", scene_module="scenes_mind"),
    _verb(key="see", past="saw", past_participle="seen", scene_module="scenes_mind"),
    _verb(key="hear", past="heard", past_participle="heard", scene_module="scenes_mind"),
    _verb(key="find", past="found", past_participle="found", scene_module="scenes_mind"),
    _verb(key="lose", past="lost", past_participle="lost", scene_module="scenes_mind"),
    _verb(key="say", past="said", past_participle="said", scene_module="scenes_speech"),
    _verb(key="tell", past="told", past_participle="told", scene_module="scenes_speech"),
    _verb(key="speak", past="spoke", past_participle="spoken", scene_module="scenes_speech"),
    _verb(key="write", past="wrote", past_participle="written", scene_module="scenes_speech"),
    _verb(key="read", past="read", past_participle="read", scene_module="scenes_speech"),
    _verb(key="draw", past="drew", past_participle="drawn", scene_module="scenes_speech"),
    _verb(key="meet", past="met", past_participle="met", scene_module="scenes_speech"),
    _verb(key="send", past="sent", past_participle="sent", scene_module="scenes_speech"),
    _verb(key="give", past="gave", past_participle="given", scene_module="scenes_objects"),
    _verb(key="take", past="took", past_participle="taken", scene_module="scenes_objects"),
    _verb(key="get", past="got", past_participle="gotten", scene_module="scenes_objects"),
    _verb(key="bring", past="brought", past_participle="brought", scene_module="scenes_objects"),
    _verb(key="buy", past="bought", past_participle="bought", scene_module="scenes_objects"),
    _verb(key="pay", past="paid", past_participle="paid", scene_module="scenes_objects"),
    _verb(key="put", past="put", past_participle="put", scene_module="scenes_objects"),
    _verb(key="hold", past="held", past_participle="held", scene_module="scenes_objects"),
    _verb(key="keep", past="kept", past_participle="kept", scene_module="scenes_objects"),
    _verb(key="let", past="let", past_participle="let", scene_module="scenes_objects"),
    _verb(key="spend", past="spent", past_participle="spent", scene_module="scenes_objects"),
    _verb(key="make", past="made", past_participle="made", scene_module="scenes_making"),
    _verb(key="build", past="built", past_participle="built", scene_module="scenes_making"),
    _verb(key="break", past="broke", past_participle="broken", scene_module="scenes_making"),
    _verb(key="cut", past="cut", past_participle="cut", scene_module="scenes_making"),
    _verb(key="grow", past="grew", past_participle="grown", scene_module="scenes_making"),
    _verb(key="wear", past="wore", past_participle="worn", scene_module="scenes_making"),
    _verb(key="have", past="had", past_participle="had", scene_module="scenes_making"),
    _verb(key="do", past="did", past_participle="done", scene_module="scenes_making"),
    _verb(key="be", past="was / were", past_participle="been", scene_module="scenes_making"),
    _verb(key="become", past="became", past_participle="become", scene_module="scenes_making"),
    _verb(key="lead", past="led", past_participle="led", scene_module="scenes_making"),
]


# The verbs that are drawn and built right now. Add a key here to build more of the 50.
BUILT_VERB_KEYS = ("be", "go", "run", "fall", "know", "think", "see", "give", "break", "write")


def find_built_verbs():
    return [verb for verb in IRREGULAR_VERBS if verb.key in BUILT_VERB_KEYS]


def build_image_name(
    verb,
    form,
):
    return f"{verb.key}_{FORM_FILE_NAMES[form]}.png"


def build_image_title(
    verb,
    form,
):
    return f"{verb.forms[form].title()} ({FORM_LABELS[form]})"
