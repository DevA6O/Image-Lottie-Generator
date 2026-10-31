"""
The 50 most common irregular English verbs with their three forms, and the script that draws each one.
The scripts live in gen/, one folder per group (motion, mind, speech, objects, making).
"""
import keyword
from dataclasses import dataclass

FORM_LABELS = ("infinitive", "past", "past participle")
FORM_FILE_NAMES = ("infinitive", "past", "participle")


@dataclass(frozen=True)
class IrregularVerb:
    key: str
    infinitive: str
    past: str
    past_participle: str
    group: str

    @property
    def forms(self):
        return (self.infinitive, self.past, self.past_participle)

    @property
    def script(self):
        """Path of the script that draws this verb, relative to the verbs folder."""
        module_name = f"{self.key}_" if keyword.iskeyword(self.key) else self.key

        return f"gen/{self.group}/{module_name}.py"


def _verb(
    key,
    past,
    past_participle,
    group,
):
    return IrregularVerb(key=key, infinitive=key, past=past, past_participle=past_participle, group=group)


IRREGULAR_VERBS = [
    _verb(key="go", past="went", past_participle="gone", group="motion"),
    _verb(key="come", past="came", past_participle="come", group="motion"),
    _verb(key="run", past="ran", past_participle="run", group="motion"),
    _verb(key="fall", past="fell", past_participle="fallen", group="motion"),
    _verb(key="rise", past="rose", past_participle="risen", group="motion"),
    _verb(key="leave", past="left", past_participle="left", group="motion"),
    _verb(key="drive", past="drove", past_participle="driven", group="motion"),
    _verb(key="stand", past="stood", past_participle="stood", group="motion"),
    _verb(key="sit", past="sat", past_participle="sat", group="motion"),
    _verb(key="begin", past="began", past_participle="begun", group="motion"),
    _verb(key="know", past="knew", past_participle="known", group="mind"),
    _verb(key="think", past="thought", past_participle="thought", group="mind"),
    _verb(key="understand", past="understood", past_participle="understood", group="mind"),
    _verb(key="mean", past="meant", past_participle="meant", group="mind"),
    _verb(key="feel", past="felt", past_participle="felt", group="mind"),
    _verb(key="choose", past="chose", past_participle="chosen", group="mind"),
    _verb(key="see", past="saw", past_participle="seen", group="mind"),
    _verb(key="hear", past="heard", past_participle="heard", group="mind"),
    _verb(key="find", past="found", past_participle="found", group="mind"),
    _verb(key="lose", past="lost", past_participle="lost", group="mind"),
    _verb(key="say", past="said", past_participle="said", group="speech"),
    _verb(key="tell", past="told", past_participle="told", group="speech"),
    _verb(key="speak", past="spoke", past_participle="spoken", group="speech"),
    _verb(key="write", past="wrote", past_participle="written", group="speech"),
    _verb(key="read", past="read", past_participle="read", group="speech"),
    _verb(key="draw", past="drew", past_participle="drawn", group="speech"),
    _verb(key="meet", past="met", past_participle="met", group="speech"),
    _verb(key="send", past="sent", past_participle="sent", group="speech"),
    _verb(key="give", past="gave", past_participle="given", group="objects"),
    _verb(key="take", past="took", past_participle="taken", group="objects"),
    _verb(key="get", past="got", past_participle="gotten", group="objects"),
    _verb(key="bring", past="brought", past_participle="brought", group="objects"),
    _verb(key="buy", past="bought", past_participle="bought", group="objects"),
    _verb(key="pay", past="paid", past_participle="paid", group="objects"),
    _verb(key="put", past="put", past_participle="put", group="objects"),
    _verb(key="hold", past="held", past_participle="held", group="objects"),
    _verb(key="keep", past="kept", past_participle="kept", group="objects"),
    _verb(key="let", past="let", past_participle="let", group="objects"),
    _verb(key="spend", past="spent", past_participle="spent", group="objects"),
    _verb(key="make", past="made", past_participle="made", group="making"),
    _verb(key="build", past="built", past_participle="built", group="making"),
    _verb(key="break", past="broke", past_participle="broken", group="making"),
    _verb(key="cut", past="cut", past_participle="cut", group="making"),
    _verb(key="grow", past="grew", past_participle="grown", group="making"),
    _verb(key="wear", past="wore", past_participle="worn", group="making"),
    _verb(key="have", past="had", past_participle="had", group="making"),
    _verb(key="do", past="did", past_participle="done", group="making"),
    _verb(key="be", past="was / were", past_participle="been", group="making"),
    _verb(key="become", past="became", past_participle="become", group="making"),
    _verb(key="lead", past="led", past_participle="led", group="making"),
]


# The verbs that are drawn and built right now. Add a key here to build more of the 50.
BUILT_VERB_KEYS = ("be", "go", "run", "fall", "know", "think", "see", "give", "break", "write", "come", "leave", "rise", "drive", "stand", "sit", "begin", "choose", "feel", "find", "understand", "mean", "hear", "lose", "say", "tell", "speak", "read", "draw", "meet", "send", "take", "get", "bring", "buy", "pay", "put", "hold", "keep", "let", "spend", "make", "build", "cut", "grow", "wear", "have", "do", "become", "lead")


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
