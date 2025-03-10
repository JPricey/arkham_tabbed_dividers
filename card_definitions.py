from typing import Optional
from dataclasses import dataclass


@dataclass
class Card:
    text: str
    tab_icon: str
    colour: str
    back_icon: Optional[str] = None
    tab_text: Optional[str] = None


def make_set(cards, *, num_tabs=5):
    res = []
    for i, card in enumerate(cards):
        res.append((card, i % num_tabs, num_tabs))
    return res


###############################################################################
# Night of the Zealot
###############################################################################

NOTZ_COLOR = "#88aed0"
NOTZ_ICON = "notz/elder.svg"
RTNOTZ_COLOR = "#6995bb"
RTNOTZ_ICON = "notz/rset.svg"

NOTZ_MISSIONS = make_set(
    [
        Card("I: The Gathering", "notz/notz-g668.svg", NOTZ_COLOR, NOTZ_ICON),
        Card("II: The Midnight Masks", "notz/notz-g498.svg", NOTZ_COLOR, NOTZ_ICON),
        Card("III: The Devourer Below", "notz/notz-g618.svg", NOTZ_COLOR, NOTZ_ICON),
    ]
)

NOTZ_ENCOUNTERS = make_set(
    [
        Card("Rats", "notz/notz-g684.svg", NOTZ_COLOR, NOTZ_ICON),
        Card("Gouls", "notz/notz-g708.svg", NOTZ_COLOR, NOTZ_ICON),
        Card("Striking Fear", "notz/notz-g916.svg", NOTZ_COLOR, NOTZ_ICON),
        Card("Ancient Evils", "notz/notz-g776.svg", NOTZ_COLOR, NOTZ_ICON),
        Card("Chilling Cold", "notz/notz-g860.svg", NOTZ_COLOR, NOTZ_ICON),
        Card("Nightgaunts", "notz/notz-g602.svg", NOTZ_COLOR, NOTZ_ICON),
        Card("Dark Cult", "notz/notz-g630.svg", NOTZ_COLOR, NOTZ_ICON),
        Card("Locked Doors", "notz/notz-g678.svg", NOTZ_COLOR, NOTZ_ICON),
        Card("Cult of Umôrdhoth", "notz/notz-g714.svg", NOTZ_COLOR, NOTZ_ICON),
        Card("Agents of Yog-Sothoth", "notz/notz-g870.svg", NOTZ_COLOR, NOTZ_ICON),
        Card("Agents of Shub-Niggurath", "notz/notz-g922.svg", NOTZ_COLOR, NOTZ_ICON),
        Card("Agents of Cthulhu", "notz/notz-g966.svg", NOTZ_COLOR, NOTZ_ICON),
        Card("Agents of Hastur", "notz/notz-g1014.svg", NOTZ_COLOR, NOTZ_ICON),
    ]
)

# Same as NOTZ_ENCOUNTERS but replace Cult of Umôrdhoth with midnight masks encounter set
CORE_SET_ENCOUNTERS = make_set(
    [
        Card("Rats", "notz/notz-g684.svg", NOTZ_COLOR, NOTZ_ICON),
        Card("Gouls", "notz/notz-g708.svg", NOTZ_COLOR, NOTZ_ICON),
        Card("Striking Fear", "notz/notz-g916.svg", NOTZ_COLOR, NOTZ_ICON),
        Card("Ancient Evils", "notz/notz-g776.svg", NOTZ_COLOR, NOTZ_ICON),
        Card("Chilling Cold", "notz/notz-g860.svg", NOTZ_COLOR, NOTZ_ICON),
        Card("Nightgaunts", "notz/notz-g602.svg", NOTZ_COLOR, NOTZ_ICON),
        Card("Dark Cult", "notz/notz-g630.svg", NOTZ_COLOR, NOTZ_ICON),
        Card("Locked Doors", "notz/notz-g678.svg", NOTZ_COLOR, NOTZ_ICON),
        Card(
            "The Midnight Masks (Encounters)",
            "notz/notz-g498.svg",
            NOTZ_COLOR,
            NOTZ_ICON,
        ),
        Card("Agents of Yog-Sothoth", "notz/notz-g870.svg", NOTZ_COLOR, NOTZ_ICON),
        Card("Agents of Shub-Niggurath", "notz/notz-g922.svg", NOTZ_COLOR, NOTZ_ICON),
        Card("Agents of Cthulhu", "notz/notz-g966.svg", NOTZ_COLOR, NOTZ_ICON),
        Card("Agents of Hastur", "notz/notz-g1014.svg", NOTZ_COLOR, NOTZ_ICON),
    ]
)

RTNOTZ_MISSIONS = make_set(
    [
        Card("I: Return to The Gathering", "notz/rtm1.svg", RTNOTZ_COLOR, RTNOTZ_ICON),
        Card(
            "II: Return to The Midnight Masks",
            "notz/rtm2.svg",
            RTNOTZ_COLOR,
            RTNOTZ_ICON,
        ),
        Card(
            "III: Return to The Devourer Below",
            "notz/rtm3.svg",
            RTNOTZ_COLOR,
            RTNOTZ_ICON,
        ),
    ]
)

RTNOTZ_ENCOUNTERS = make_set(
    [
        Card("Gouls of Umôrdhoth", "notz/rte2.svg", RTNOTZ_COLOR, RTNOTZ_ICON),
        Card("The Devourer's Cult", "notz/rte3.svg", RTNOTZ_COLOR, RTNOTZ_ICON),
        Card("Cult of Umôrdhoth", "notz/rte1.svg", RTNOTZ_COLOR, RTNOTZ_ICON),
    ]
)

###############################################################################
# The Dunwich Legacy
###############################################################################

DUNWICH_COLOR = "#C7E9B0"
DUNWICH_ICON = "dunwich/set.svg"
RTDUNWICH_COLOR = "#B3C99C"
RTDUNWICH_ICON = "dunwich/rset.svg"

DUNWICH_MISSIONS = make_set(
    [
        Card(
            "Ia: Extracurricular Activity",
            "dunwich/m1.svg",
            DUNWICH_COLOR,
            DUNWICH_ICON,
        ),
        Card(
            "Ib: The House Always Wins", "dunwich/m2.svg", DUNWICH_COLOR, DUNWICH_ICON
        ),
        Card(
            "Interlude: Armitage's Fate", "dunwich/m3.svg", DUNWICH_COLOR, DUNWICH_ICON
        ),
        Card(
            "II: The Miskatonic Museum", "dunwich/m4.svg", DUNWICH_COLOR, DUNWICH_ICON
        ),
        Card(
            "III: The Essex County Express",
            "dunwich/m5.svg",
            DUNWICH_COLOR,
            DUNWICH_ICON,
        ),
        Card("IV: Blood on the Altar", "dunwich/m6.svg", DUNWICH_COLOR, DUNWICH_ICON),
        Card(
            "V: Undimensioned and Unseen", "dunwich/m7.svg", DUNWICH_COLOR, DUNWICH_ICON
        ),
        Card("VI: Where Doom Awaits", "dunwich/m8.svg", DUNWICH_COLOR, DUNWICH_ICON),
        Card(
            "VII: Lost in Time and Space", "dunwich/m9.svg", DUNWICH_COLOR, DUNWICH_ICON
        ),
    ]
)

DUNWICH_ENCOUNTERS = make_set(
    [
        Card("Sorcery", "dunwich/e1.svg", DUNWICH_COLOR, DUNWICH_ICON),
        Card("The Beyond", "dunwich/e2.svg", DUNWICH_COLOR, DUNWICH_ICON),
        Card("Bishop's Thralls", "dunwich/e3.svg", DUNWICH_COLOR, DUNWICH_ICON),
        Card("Whippoorwills", "dunwich/e4.svg", DUNWICH_COLOR, DUNWICH_ICON),
        Card("Bad Luck", "dunwich/e5.svg", DUNWICH_COLOR, DUNWICH_ICON),
        Card("Naomi's Crew", "dunwich/e6.svg", DUNWICH_COLOR, DUNWICH_ICON),
        Card("Hideous Abominations", "dunwich/e7.svg", DUNWICH_COLOR, DUNWICH_ICON),
        Card("Dunwich", "dunwich/e8.svg", DUNWICH_COLOR, DUNWICH_ICON),
        Card("Beast Thralls", "dunwich/e9.svg", DUNWICH_COLOR, DUNWICH_ICON),
    ]
)

RTDUNWICH_MISSIONS = make_set(
    [
        Card(
            "Ia: Return to Extracurricular Activity",
            "dunwich/rm1.svg",
            RTDUNWICH_COLOR,
            RTDUNWICH_ICON,
        ),
        Card(
            "Ib: Return to The House Always Wins",
            "dunwich/rm2.svg",
            RTDUNWICH_COLOR,
            RTDUNWICH_ICON,
        ),
        Card(
            "II: Return to The Miskatonic Museum",
            "dunwich/rm3.svg",
            RTDUNWICH_COLOR,
            RTDUNWICH_ICON,
        ),
        Card(
            "III: Return to The Essex County Express",
            "dunwich/rm4.svg",
            RTDUNWICH_COLOR,
            RTDUNWICH_ICON,
        ),
        Card(
            "IV: Return to Blood on the Altar",
            "dunwich/rm5.svg",
            RTDUNWICH_COLOR,
            RTDUNWICH_ICON,
        ),
        Card(
            "V: Return to Undimensioned and Unseen",
            "dunwich/rm6.svg",
            RTDUNWICH_COLOR,
            RTDUNWICH_ICON,
        ),
        Card(
            "VI: Return to Where Doom Awaits",
            "dunwich/rm7.svg",
            RTDUNWICH_COLOR,
            RTDUNWICH_ICON,
        ),
        Card(
            "VII: Return to Lost in Time and Space",
            "dunwich/rm8.svg",
            RTDUNWICH_COLOR,
            RTDUNWICH_ICON,
        ),
    ]
)

RTDUNWICH_ENCOUNTERS = make_set(
    [
        Card(
            "Beyond the Threshold", "dunwich/re6.svg", RTDUNWICH_COLOR, RTDUNWICH_ICON
        ),
        Card("Secret Doors", "dunwich/re4.svg", RTDUNWICH_COLOR, RTDUNWICH_ICON),
        Card(
            "Yog-Sothoth's Emissaries",
            "dunwich/re5.svg",
            RTDUNWICH_COLOR,
            RTDUNWICH_ICON,
        ),
        Card("Erratic Fear", "dunwich/re2.svg", RTDUNWICH_COLOR, RTDUNWICH_ICON),
        Card("Creeping Cold", "dunwich/re3.svg", RTDUNWICH_COLOR, RTDUNWICH_ICON),
        Card("Resurgent Evils", "dunwich/re1.svg", RTDUNWICH_COLOR, RTDUNWICH_ICON),
    ]
)

###############################################################################
# The Path to Carcosa
###############################################################################

CARCOSA_COLOR = "#FCF9BE"
CARCOSA_ICON = "carcosa/set.svg"
RTCARCOSA_COLOUR = "#F7F3B1"
RTCARCOSA_ICON = "carcosa/rset.svg"

CARCOSA_MISSIONS = make_set(
    [
        Card("I: Curtain Call", "carcosa/m1.svg", CARCOSA_COLOR, CARCOSA_ICON),
        Card("II: The Last King", "carcosa/m2.svg", CARCOSA_COLOR, CARCOSA_ICON),
        Card("III: Echoes of the Past", "carcosa/m3.svg", CARCOSA_COLOR, CARCOSA_ICON),
        Card("IV: The Unspeakable Oath", "carcosa/m4.svg", CARCOSA_COLOR, CARCOSA_ICON),
        Card("V: A Phantom of Truth", "carcosa/m5.svg", CARCOSA_COLOR, CARCOSA_ICON),
        Card("VI: The Pallid Mask", "carcosa/m6.svg", CARCOSA_COLOR, CARCOSA_ICON),
        Card("VII: Black Stars Rise", "carcosa/m7.svg", CARCOSA_COLOR, CARCOSA_ICON),
        Card("VIII: Dim Carcosa", "carcosa/m8.svg", CARCOSA_COLOR, CARCOSA_ICON),
    ]
)

CARCOSA_ENCOUNTERS = make_set(
    [
        Card("Evil Portents", "carcosa/e1.svg", CARCOSA_COLOR, CARCOSA_ICON),
        Card("Delusions", "carcosa/e2.svg", CARCOSA_COLOR, CARCOSA_ICON),
        Card("Hauntings", "carcosa/e3.svg", CARCOSA_COLOR, CARCOSA_ICON),
        Card("Cult of the Yellow Sign", "carcosa/e4.svg", CARCOSA_COLOR, CARCOSA_ICON),
        Card("Hastur's Gift", "carcosa/e5.svg", CARCOSA_COLOR, CARCOSA_ICON),
        Card("Decay & Filth", "carcosa/e6.svg", CARCOSA_COLOR, CARCOSA_ICON),
        Card("Byakhee", "carcosa/e9.svg", CARCOSA_COLOR, CARCOSA_ICON),
        Card("Inhabitants of Carcosa", "carcosa/e8.svg", CARCOSA_COLOR, CARCOSA_ICON),
        Card("The Stranger", "carcosa/e7.svg", CARCOSA_COLOR, CARCOSA_ICON),
    ]
)

RTCARCOSA_MISSIONS = make_set(
    [
        Card(
            "I: Return to Curtain Call",
            "carcosa/rm1.svg",
            RTCARCOSA_COLOUR,
            RTCARCOSA_ICON,
        ),
        Card(
            "II: Return to The Last King",
            "carcosa/rm2.svg",
            RTCARCOSA_COLOUR,
            RTCARCOSA_ICON,
        ),
        Card(
            "III: Return to Echoes of the Past",
            "carcosa/rm3.svg",
            RTCARCOSA_COLOUR,
            RTCARCOSA_ICON,
        ),
        Card(
            "IV: Return to The Unspeakable Oath",
            "carcosa/rm4.svg",
            RTCARCOSA_COLOUR,
            RTCARCOSA_ICON,
        ),
        Card(
            "V: Return to A Phantom of Truth",
            "carcosa/rm5.svg",
            RTCARCOSA_COLOUR,
            RTCARCOSA_ICON,
        ),
        Card(
            "VI: Return to The Pallid Mask",
            "carcosa/rm6.svg",
            RTCARCOSA_COLOUR,
            RTCARCOSA_ICON,
        ),
        Card(
            "VII: Return to Black Stars Rise",
            "carcosa/rm7.svg",
            RTCARCOSA_COLOUR,
            RTCARCOSA_ICON,
        ),
        Card(
            "VIII: Return to Dim Carcosa",
            "carcosa/rm8.svg",
            RTCARCOSA_COLOUR,
            RTCARCOSA_ICON,
        ),
    ]
)

RTCARCOSA_ENCOUNTERS = make_set(
    [
        Card(
            "Maddening Delusions", "carcosa/re5.svg", RTCARCOSA_COLOUR, RTCARCOSA_ICON
        ),  # Delusion
        Card(
            "Neurotic Fear", "carcosa/re2.svg", RTCARCOSA_COLOUR, RTCARCOSA_ICON
        ),  # Striking Fear
        Card(
            "Decaying Reality", "carcosa/re4.svg", RTCARCOSA_COLOUR, RTCARCOSA_ICON
        ),  # Decay & Filth
        Card(
            "Delusory Evils", "carcosa/re1.svg", RTCARCOSA_COLOUR, RTCARCOSA_ICON
        ),  # Ancient Evils
        Card(
            "Hastur's Envoys", "carcosa/re3.svg", RTCARCOSA_COLOUR, RTCARCOSA_ICON
        ),  # Agents of Hastur
    ]
)

###############################################################################
# Dark Matter
###############################################################################

DARK_MATTER_COLOR = "#957DAD"
DM_ICON = "dm/m1.svg"
DARK_MATTER_MISSIONS = make_set(
    [
        Card("I: The Tatterdemalion", "dm/m1.svg", DARK_MATTER_COLOR, DM_ICON),
        Card("II: Electric Nightmare", "dm/m2.svg", DARK_MATTER_COLOR, DM_ICON),
        Card("IIIa: Lost Quantum", "dm/m3.svg", DARK_MATTER_COLOR, DM_ICON),
        Card("IIIb: In the Shadow of Earth", "dm/m4.svg", DARK_MATTER_COLOR, DM_ICON),
        Card("IIIc: Strange Moons", "dm/m5.svg", DARK_MATTER_COLOR, DM_ICON),
        Card("IV: The Machine in Yellow", "dm/m6.svg", DARK_MATTER_COLOR, DM_ICON),
        Card("V: Fragment of Carcosa", "dm/m7.svg", DARK_MATTER_COLOR, DM_ICON),
        Card("VI: Starfall", "dm/m8.svg", DARK_MATTER_COLOR, DM_ICON),
    ]
)

DARK_MATTER_ENCOUNTERS = make_set(
    [
        Card("Anachronism", "dm/e1.svg", DARK_MATTER_COLOR, DM_ICON),
        Card("Dark Past", "dm/e2.svg", DARK_MATTER_COLOR, DM_ICON),
        Card("Artificial Intelligence", "dm/e3.svg", DARK_MATTER_COLOR, DM_ICON),
        Card("Endtimes", "dm/e4.svg", DARK_MATTER_COLOR, DM_ICON),
        Card("The Boogeyman", "dm/e5.svg", DARK_MATTER_COLOR, DM_ICON),
        Card("Deep Space", "dm/e6.svg", DARK_MATTER_COLOR, DM_ICON),
        Card("Interstellar Predators", "dm/e7.svg", DARK_MATTER_COLOR, DM_ICON),
        Card("Hastur's Gaze", "dm/e8.svg", DARK_MATTER_COLOR, DM_ICON),
    ]
)

###############################################################################
# The Forgotten Age
###############################################################################

TFA_COLOR = "#C37B89"
TFA_ICON = "tfa/tfa.svg"
RTTFA_COLOR = "#AE5F6E"
RTTFA_ICON = "tfa/rtfa.svg"

TFA_MISSIONS = make_set(
    [
        Card("I: The Untamed Wilds", "tfa/m1.svg", TFA_COLOR, TFA_ICON),
        Card("II: The Doom of Eztli", "tfa/m2.svg", TFA_COLOR, TFA_ICON),
        Card("III: Threads of Fate", "tfa/m3.svg", TFA_COLOR, TFA_ICON),
        Card("IV: The Boundary Beyond", "tfa/m4.svg", TFA_COLOR, TFA_ICON),
        Card("V: Heart of the Elders", "tfa/m5.svg", TFA_COLOR, TFA_ICON),
        Card("Va: Pillars of Judgement", "tfa/o1.svg", TFA_COLOR, TFA_ICON),
        Card("Vb: K'n-yan", "tfa/o2.svg", TFA_COLOR, TFA_ICON),
        Card("VI: The City of Archives", "tfa/m6.svg", TFA_COLOR, TFA_ICON),
        Card("VII: The Depths of Yoth", "tfa/m7.svg", TFA_COLOR, TFA_ICON),
        Card("VIII: Shattered Aeons", "tfa/m8.svg", TFA_COLOR, TFA_ICON),
        Card("IX: Turn Back Time", "tfa/m9.svg", TFA_COLOR, TFA_ICON),
    ]
)

TFA_ENCOUNTERS = make_set(
    [
        Card("Rainforests", "tfa/e8.svg", TFA_COLOR, TFA_ICON),
        Card("Serpents", "tfa/e9.svg", TFA_COLOR, TFA_ICON),
        Card("Expedition", "tfa/e5.svg", TFA_COLOR, TFA_ICON),
        Card("Guardians of Time", "tfa/e3.svg", TFA_COLOR, TFA_ICON),
        Card("Agents of Yig", "tfa/e1.svg", TFA_COLOR, TFA_ICON),
        Card("Yig's Venom", "tfa/e11.svg", TFA_COLOR, TFA_ICON),
        Card("Temporal Flux", "tfa/e10.svg", TFA_COLOR, TFA_ICON),
        Card("Deadly Traps", "tfa/e2.svg", TFA_COLOR, TFA_ICON),
        Card("Forgotten Ruins", "tfa/e4.svg", TFA_COLOR, TFA_ICON),
        Card("Pnakotic Brotherhood", "tfa/e6.svg", TFA_COLOR, TFA_ICON),
        Card("Poison", "tfa/e7.svg", TFA_COLOR, TFA_ICON),
    ]
)

RTTFA_MISSIONS = make_set(
    [
        Card("I: Return to The Untamed Wilds", "tfa/rm1.svg", RTTFA_COLOR, RTTFA_ICON),
        Card("II: Return to The Doom of Eztli", "tfa/rm2.svg", RTTFA_COLOR, RTTFA_ICON),
        Card("III: Return to Threads of Fate", "tfa/rm3.svg", RTTFA_COLOR, RTTFA_ICON),
        Card(
            "IV: Return to The Boundary Beyond", "tfa/rm4.svg", RTTFA_COLOR, RTTFA_ICON
        ),
        Card(
            "V: Return to Heart of the Elders", "tfa/rm5.svg", RTTFA_COLOR, RTTFA_ICON
        ),
        Card(
            "Va: Return to Pillars of Judgement", "tfa/rm9.svg", RTTFA_COLOR, RTTFA_ICON
        ),
        Card("Vb: Return to K'n-yan", "tfa/rm10.svg", RTTFA_COLOR, RTTFA_ICON),
        Card(
            "VI: Return to The City of Archives", "tfa/rm6.svg", RTTFA_COLOR, RTTFA_ICON
        ),
        Card(
            "VII: Return to The Depths of Yoth", "tfa/rm7.svg", RTTFA_COLOR, RTTFA_ICON
        ),
        Card("VIII: Return to Shattered Aeons", "tfa/rm8.svg", RTTFA_COLOR, RTTFA_ICON),
        Card("IX: Return to Turn Back Time", "tfa/rm11.svg", RTTFA_COLOR, RTTFA_ICON),
    ]
)

RTTFA_ENCOUNTERS = make_set(
    [
        Card("Return to Rainforest", "tfa/re1.svg", RTTFA_COLOR, RTTFA_ICON),
        Card("Cult of Pnakotus", "tfa/re2.svg", RTTFA_COLOR, RTTFA_ICON),
        Card("Doomed Expedition", "tfa/re3.svg", RTTFA_COLOR, RTTFA_ICON),
        Card("Temporal Hunters", "tfa/re4.svg", RTTFA_COLOR, RTTFA_ICON),
        Card("Venomous Hate", "tfa/re5.svg", RTTFA_COLOR, RTTFA_ICON),
    ]
)

###############################################################################
# The Circle Undone
###############################################################################

TCU_COLOR = "#9aa1aa"
TCU_ICON = "tcu/pic4892449.webp"

RTTCU_COLOR = "#77808a"
RTTCU_ICON = "tcu/rt/pic6419863.webp"

TCU_MISSIONS = make_set(
    [
        Card(
            "Prologue: Disappearance at the Twilight Estate",
            "tcu/pic4892450.webp",
            TCU_COLOR,
            TCU_ICON,
        ),
        Card("I: The Witching Hour", "tcu/pic4892451.webp", TCU_COLOR, TCU_ICON),
        Card("II: At Death's Doorstep", "tcu/pic4892452.webp", TCU_COLOR, TCU_ICON),
        Card("III: The Secret Name", "tcu/pic4892463.webp", TCU_COLOR, TCU_ICON),
        Card("IV: The Wages of Sin", "tcu/pic4892464.webp", TCU_COLOR, TCU_ICON),
        Card("V: For the Greater Good", "tcu/pic4892465.webp", TCU_COLOR, TCU_ICON),
        Card("VI: Union and Disillusion", "tcu/pic4892466.webp", TCU_COLOR, TCU_ICON),
        Card(
            "VII: In the Clutches of Chaos", "tcu/pic4892467.webp", TCU_COLOR, TCU_ICON
        ),
        Card(
            "VIII: Before the Black Throne", "tcu/pic4892470.webp", TCU_COLOR, TCU_ICON
        ),
    ]
)

# ['Spectral Predators', 'The Watcher', 'Trapped Spirits', 'Realm of Death', 'Inexorable Fate', 'Silver Twilight Lodge', "Annette's Coven", 'City of Sins', 'Witchcraft', 'Agents of Azathoth', 'Music of the Damned', 'Secrets of the Universe'] 14 574.4444444444443
TCU_ENCOUNTERS = make_set(
    [
        Card("Spectral Predators", "tcu/pic4892459.webp", TCU_COLOR, TCU_ICON),
        Card("The Watcher", "tcu/pic4892453.webp", TCU_COLOR, TCU_ICON),
        Card("Trapped Spirits", "tcu/pic4892460.webp", TCU_COLOR, TCU_ICON),
        Card("Realm of Death", "tcu/pic4892461.webp", TCU_COLOR, TCU_ICON),
        Card("Inexorable Fate", "tcu/pic4892462.webp", TCU_COLOR, TCU_ICON),
        Card("Silver Twilight Lodge", "tcu/pic4892457.webp", TCU_COLOR, TCU_ICON),
        Card("Annette's Coven", "tcu/pic4892455.webp", TCU_COLOR, TCU_ICON),
        Card("City of Sins", "tcu/pic4892458.webp", TCU_COLOR, TCU_ICON),
        Card("Witchcraft", "tcu/pic4892456.webp", TCU_COLOR, TCU_ICON),
        Card("Agents of Azathoth", "tcu/pic4892454.webp", TCU_COLOR, TCU_ICON),
        Card("Music of the Damned", "tcu/pic4892468.webp", TCU_COLOR, TCU_ICON),
        Card("Secrets of the Universe", "tcu/pic4892469.webp", TCU_COLOR, TCU_ICON),
    ]
)


RTTCU_MISSIONS = make_set(
    [
        Card(
            "Prologue: Return to Disappearance at the Twilight Estate",
            "tcu/rt/pic6419872.webp",
            RTTCU_COLOR,
            RTTCU_ICON,
        ),
        Card(
            "I: Return to The Witching Hour",
            "tcu/rt/pic6419875.webp",
            RTTCU_COLOR,
            RTTCU_ICON,
        ),
        Card(
            "II: Return to At Death's Doorstep",
            "tcu/rt/pic6419876.webp",
            RTTCU_COLOR,
            RTTCU_ICON,
        ),
        Card(
            "III: Return to The Secret Name",
            "tcu/rt/pic6419866.webp",
            RTTCU_COLOR,
            RTTCU_ICON,
        ),
        Card(
            "IV: Return to The Wages of Sin",
            "tcu/rt/pic6419867.webp",
            RTTCU_COLOR,
            RTTCU_ICON,
        ),
        Card(
            "V: Return to For the Greater Good",
            "tcu/rt/pic6419869.webp",
            RTTCU_COLOR,
            RTTCU_ICON,
        ),
        Card(
            "VI: Return to Union and Disillusion",
            "tcu/rt/pic6419870.webp",
            RTTCU_COLOR,
            RTTCU_ICON,
        ),
        Card(
            "VII: Return to In the Clutches of Chaos",
            "tcu/rt/pic6419877.webp",
            RTTCU_COLOR,
            RTTCU_ICON,
        ),
        Card(
            "VIII: Return to Before the Black Throne",
            "tcu/rt/pic6419880.webp",
            RTTCU_COLOR,
            RTTCU_ICON,
        ),
    ]
)

RTTCU_ENCOUNTERS = make_set(
    [
        Card(
            "Bloodthirsty Spirits", "tcu/rt/pic6419881.webp", RTTCU_COLOR, RTTCU_ICON
        ),  # Trapped Spirits
        Card(
            "Unstable Realm", "tcu/rt/pic6419891.webp", RTTCU_COLOR, RTTCU_ICON
        ),  # Realm of Death
        Card(
            "Unspeakable Fate", "tcu/rt/pic6419889.webp", RTTCU_COLOR, RTTCU_ICON
        ),  # Inexorable Fate
        Card(
            "City of the Damned", "tcu/rt/pic6419884.webp", RTTCU_COLOR, RTTCU_ICON
        ),  # City of Sins
        Card(
            "Hexcraft", "tcu/rt/pic6419886.webp", RTTCU_COLOR, RTTCU_ICON
        ),  # Witchcraft
        Card(
            "Chilling Mists", "tcu/rt/pic6419882.webp", RTTCU_COLOR, RTTCU_ICON
        ),  # NotZ: Chilling Cold
        Card(
            "Impending Evils", "tcu/rt/pic6419887.webp", RTTCU_COLOR, RTTCU_ICON
        ),  # NotZ: Ancient Evils
    ]
)

###############################################################################
# The Dream Eaters
###############################################################################

TDE_COLOR = "#8674a8"
TDE_ICON = "tde/tde.webp"
TDE_MISSIONS = make_set(
    [
        Card("I-A: Beyond the Gates of Sleep", "tde/m1a.webp", TDE_COLOR, TDE_ICON),
        Card("I-B: Waking Nightmare", "tde/m1b.webp", TDE_COLOR, TDE_ICON),

        Card("II-A: The Search for Kadath", "tde/m2a.webp", TDE_COLOR, TDE_ICON),
        Card("II-B: A Thousand Shapes of Horror", "tde/m2b.webp", TDE_COLOR, TDE_ICON),

        Card("III-A: Dark Side of the Moon", "tde/m3a.webp", TDE_COLOR, TDE_ICON),
        Card("III-B: Point of No Return", "tde/m3b.webp", TDE_COLOR, TDE_ICON),

        Card("IV-A: Where the Gods Dwell", "tde/m4a.webp", TDE_COLOR, TDE_ICON),
        Card("IV-B: Weaver of the Cosmos", "tde/m4b.webp", TDE_COLOR, TDE_ICON),
    ]
)

TDE_ENCOUNTERS = make_set(
    [
        Card("Agents of Nyarlathotep", "tde/e_aon.webp", TDE_COLOR, TDE_ICON),
        Card("Zoogs", "tde/e_z.webp", TDE_COLOR, TDE_ICON),
        Card("Dreamer’s Curse", "tde/e_dc.webp", TDE_COLOR, TDE_ICON),
        Card("Dreamlands", "tde/e_d.webp", TDE_COLOR, TDE_ICON),
        Card("Corsairs", "tde/e_c.webp", TDE_COLOR, TDE_ICON),
        Card("Whispers of Hypnos", "tde/e_woh.webp", TDE_COLOR, TDE_ICON),
        Card("Dark Cult", "tde/e_dc.webp", TDE_COLOR, TDE_ICON),
        Card("Agents of Atlach-Nacha", "tde/e_aoan.webp", TDE_COLOR, TDE_ICON),
        Card("Spiders", "tde/e_s.webp", TDE_COLOR, TDE_ICON),
        Card("Creatures of the Underworld", "tde/e_cotu.webp", TDE_COLOR, TDE_ICON),
        Card("Merging Realities", "tde/e_mr.webp", TDE_COLOR, TDE_ICON),
        Card("Descent into the Pitch", "tde/e_ditp.webp", TDE_COLOR, TDE_ICON),
        Card("Terror of the Vale", "tde/e_totv.webp", TDE_COLOR, TDE_ICON),
    ]
)

###############################################################################
# The Innsmouth Conspiracy
###############################################################################

TIC_COLOR = "#7ca688"
TIC_ICON = "tic/tic.webp"
TIC_MISSIONS = make_set(
    [
        Card("I: The Pit of Despair", "tic/the_pit_of_despair.webp", TIC_COLOR, TIC_ICON),
        Card("II: The Vanishing of Elina Harper", "tic/the_vanishing_of_elina_harper.webp", TIC_COLOR, TIC_ICON),
        Card("III: In Too Deep", "tic/in_too_deep.webp", TIC_COLOR, TIC_ICON),
        Card("IV: Devil Reef", "tic/devil_reef.webp", TIC_COLOR, TIC_ICON),
        Card("V: Horror in High Gear", "tic/horror_in_high_gear.webp", TIC_COLOR, TIC_ICON),
        Card("VI: A Light in the Fog", "tic/a_light_in_the_fog.webp", TIC_COLOR, TIC_ICON),
        Card("VII: The Lair of Dagon", "tic/the_lair_of_dagon.webp", TIC_COLOR, TIC_ICON),
        Card("VIII: Into the Maelstrom", "tic/into_the_maelstrom.webp", TIC_COLOR, TIC_ICON),
    ]
)

TIC_ENCOUNTERS = make_set(
    [
        Card("Creatures of the Deep", "tic/creatures_of_the_deep.webp", TIC_COLOR, TIC_ICON),
        Card("Flooded Caverns", "tic/flooded_caverns.webp", TIC_COLOR, TIC_ICON),
        Card("Rising Tide", "tic/rising_tide.webp", TIC_COLOR, TIC_ICON),
        Card("Shattered Memories", "tic/shattered_memories.webp", TIC_COLOR, TIC_ICON),
        Card("Agents of Dagon", "tic/agents_of_dagon.webp", TIC_COLOR, TIC_ICON),
        Card("Fog over Innsmouth", "tic/fog_over_innsmouth.webp", TIC_COLOR, TIC_ICON),
        Card("The Locals", "tic/the_locals.webp", TIC_COLOR, TIC_ICON),
        Card("Syzygy", "tic/syzygy.webp", TIC_COLOR, TIC_ICON),
        Card("Agents of Hydra", "tic/agents_of_hydra.webp", TIC_COLOR, TIC_ICON),
        Card("Malfunction", "tic/malfunction.webp", TIC_COLOR, TIC_ICON),
        Card("Keys", "notz/notz-g870.svg", TIC_COLOR, TIC_ICON),
    ]
)


###############################################################################
# Edge of the Earth:
###############################################################################

EOTE_COLOR = "#E3F4F4"
EOTE_ICON = "eote/set.svg"

EOTE_MISSIONS = make_set(
    [
        Card("I: Ice and Death", "eote/ice_and_death.svg", EOTE_COLOR, EOTE_ICON),
        Card("Ia: The Crash", "eote/the_crash.svg", EOTE_COLOR, EOTE_ICON),
        Card(
            "Ib: Lost in the Night", "eote/lost_in_the_night.svg", EOTE_COLOR, EOTE_ICON
        ),
        Card(
            "Ic: Seeping Nightmares",
            "eote/seeping_nightmares.svg",
            EOTE_COLOR,
            EOTE_ICON,
        ),
        Card("* Fatal Mirage *", "eote/fatal_mirage.svg", EOTE_COLOR, EOTE_ICON),
        Card(
            "II: To the Forbidden Peaks",
            "eote/to_the_forbidden_peaks.svg",
            EOTE_COLOR,
            EOTE_ICON,
        ),
        Card(
            "III: City of the Elder Things",
            "eote/city_of_the_elder_things.svg",
            EOTE_COLOR,
            EOTE_ICON,
        ),
        Card(
            "IV: The Heart of Madness",
            "eote/the_heart_of_madness.svg",
            EOTE_COLOR,
            EOTE_ICON,
        ),
        Card("IVa: The Great Seal", "eote/the_great_seal.svg", EOTE_COLOR, EOTE_ICON),
        Card(
            "IVb: Stirring in the Deep",
            "eote/stirring_in_the_deep.svg",
            EOTE_COLOR,
            EOTE_ICON,
        ),
    ]
)

EOTE_ENCOUNTERS = make_set(
    [
        Card("Expedition Team", "eote/expedition_team.svg", EOTE_COLOR, EOTE_ICON),
        Card(
            "Memorials of the Lost",
            "eote/memorials_of_the_lost.svg",
            EOTE_COLOR,
            EOTE_ICON,
        ),
        Card(
            "Creatures in the Ice",
            "eote/creatures_in_the_ice.svg",
            EOTE_COLOR,
            EOTE_ICON,
        ),
        Card("Deadly Weather", "eote/deadly_weather.svg", EOTE_COLOR, EOTE_ICON),
        Card(
            "Hazards of Antarctica",
            "eote/hazards_of_antarctica.svg",
            EOTE_COLOR,
            EOTE_ICON,
        ),
        Card(
            "Silence and Mystery", "eote/silence_and_mystery.svg", EOTE_COLOR, EOTE_ICON
        ),
        Card("Left Behind", "eote/left_behind.svg", EOTE_COLOR, EOTE_ICON),
        Card(
            "Agents of the Unknown",
            "eote/agents_of_the_unknown.svg",
            EOTE_COLOR,
            EOTE_ICON,
        ),
        Card("Miasma", "eote/miasma.svg", EOTE_COLOR, EOTE_ICON),
        Card("Nameless Horrors", "eote/nameless_horrors.svg", EOTE_COLOR, EOTE_ICON),
        Card("Elder Things", "eote/elder_things.svg", EOTE_COLOR, EOTE_ICON),
        Card("Penguins", "eote/penguins.svg", EOTE_COLOR, EOTE_ICON),
        Card("Shoggoths", "eote/shoggoths.svg", EOTE_COLOR, EOTE_ICON),
        Card("Tekeli-li", "eote/tekeli_li.svg", EOTE_COLOR, EOTE_ICON),
    ]
)

###############################################################################
# The Scarlet Keys
###############################################################################

SCARLET_COLOR = "#FD8A8A"
SCARLET_ICON = "scarlet/set.svg"

SCARLET_MISSIONS = make_set(
    [
        Card(
            "Riddles and Rain",
            "scarlet/riddles_and_rain.svg",
            SCARLET_COLOR,
            SCARLET_ICON,
        ),
        Card("Dead Heat", "scarlet/dead_heat.svg", SCARLET_COLOR, SCARLET_ICON),
        Card(
            "Sanguine Shadows",
            "scarlet/sanguine_shadows.svg",
            SCARLET_COLOR,
            SCARLET_ICON,
        ),
        Card(
            "Dealings in the Dark",
            "scarlet/dealings_in_the_dark.svg",
            SCARLET_COLOR,
            SCARLET_ICON,
        ),
        Card("Dancing Mad", "scarlet/dancing_mad.svg", SCARLET_COLOR, SCARLET_ICON),
        Card("On Thin Ice", "scarlet/on_thin_ice.svg", SCARLET_COLOR, SCARLET_ICON),
        Card("Dogs of War", "scarlet/dogs_of_war.svg", SCARLET_COLOR, SCARLET_ICON),
        Card(
            "Shades of Suffering",
            "scarlet/shades_of_suffering.svg",
            SCARLET_COLOR,
            SCARLET_ICON,
        ),
        Card(
            "Without a Trace",
            "scarlet/without_a_trace.svg",
            SCARLET_COLOR,
            SCARLET_ICON,
        ),
        Card(
            "Congress of the Keys",
            "scarlet/congress_of_the_keys.svg",
            SCARLET_COLOR,
            SCARLET_ICON,
        ),
    ]
)

SCARLET_ENCOUNTERS = make_set(
    [
        Card(
            "Crimson Conspiracy",
            "scarlet/crimson_conspiracy.svg",
            SCARLET_COLOR,
            SCARLET_ICON,
        ),
        Card("Dark Veiling", "scarlet/dark_veiling.svg", SCARLET_COLOR, SCARLET_ICON),
        Card("Outsiders", "scarlet/outsiders.svg", SCARLET_COLOR, SCARLET_ICON),
        Card(
            "Shadow of a Doubt",
            "scarlet/shadow_of_a_doubt.svg",
            SCARLET_COLOR,
            SCARLET_ICON,
        ),
        Card(
            "Strange Happenings",
            "scarlet/strange_happenings.svg",
            SCARLET_COLOR,
            SCARLET_ICON,
        ),
        Card(
            "Scarlet Sorcery",
            "scarlet/scarlet_sorcery.svg",
            SCARLET_COLOR,
            SCARLET_ICON,
        ),
        Card(
            "Spreading Corruption",
            "scarlet/spreading_corruption.svg",
            SCARLET_COLOR,
            SCARLET_ICON,
        ),
        Card(
            "Mysteries Abound",
            "scarlet/mysteries_abound.svg",
            SCARLET_COLOR,
            SCARLET_ICON,
        ),
        Card(
            "Agents of Yuggoth",
            "scarlet/agents_of_yuggoth.svg",
            SCARLET_COLOR,
            SCARLET_ICON,
        ),
        Card(
            "Agents of the Outside",
            "scarlet/agents_of_the_outside.svg",
            SCARLET_COLOR,
            SCARLET_ICON,
        ),
        Card("Cleanup Crew", "scarlet/cleanup_crew.svg", SCARLET_COLOR, SCARLET_ICON),
        Card("Secret War", "scarlet/secret_war.svg", SCARLET_COLOR, SCARLET_ICON),
        Card(
            "Spatial Anomaly",
            "scarlet/spatial_anomaly.svg",
            SCARLET_COLOR,
            SCARLET_ICON,
        ),
        Card(
            "Beyond the Beyond",
            "scarlet/beyond_the_beyond.svg",
            SCARLET_COLOR,
            SCARLET_ICON,
        ),
        Card("Red Coterie", "scarlet/red_coterie.svg", SCARLET_COLOR, SCARLET_ICON),
        Card("Globetrotting", "scarlet/globetrotting.svg", SCARLET_COLOR, SCARLET_ICON),
    ]
)

###############################################################################
# The Feast of Hemlock Vale
###############################################################################

FHV_COLOR = "#e39b5f"
FHV_ICON = "fhv/fhv.webp"

FHV_MISSIONS = make_set(
    [
        Card("The First Day", "fhv/m_tfd.webp", FHV_COLOR, FHV_ICON),
        Card("The Second Day", "fhv/m_tsd.webp", FHV_COLOR, FHV_ICON),
        Card("The Final Day", "fhv/m_ttd.webp", FHV_COLOR, FHV_ICON),
        Card("Written in Rock", "fhv/m_wir.webp", FHV_COLOR, FHV_ICON),
        Card("Hemlock House", "fhv/m_hemlock_house.webp", FHV_COLOR, FHV_ICON),
        Card("The Silent Heath", "fhv/m_tsh.webp", FHV_COLOR, FHV_ICON),
        Card("The Lost Sister", "fhv/m_tls.webp", FHV_COLOR, FHV_ICON),
        Card("The Thing in the Depths", "fhv/m_ttitd.webp", FHV_COLOR, FHV_ICON),
        Card("The Twisted Hollow", "fhv/m_tth.webp", FHV_COLOR, FHV_ICON),
        Card("The Longest Night", "fhv/m_tln.webp", FHV_COLOR, FHV_ICON),
        Card("Fate of the Vale", "fhv/m_fate_of_the_vale.webp", FHV_COLOR, FHV_ICON),
    ] 
)

FHV_ENCOUNTERS = make_set(
    [
        Card("The Vale", "fhv/e_the_vale.webp", FHV_COLOR, FHV_ICON,),
        Card("Residents", "fhv/e_residents.webp", FHV_COLOR, FHV_ICON,),
        Card("Hierlooms", "fhv/hierlooms.webp", FHV_COLOR, FHV_ICON,),
        Card("Day of Rest", "fhv/e_dor.webp", FHV_COLOR, FHV_ICON,),
        Card("Day of Rain", "fhv/e_day_of_rain.webp", FHV_COLOR, FHV_ICON,),
        Card("Day of the Feast", "fhv/e_day_of_the_feast.webp", FHV_COLOR, FHV_ICON,),
        Card("Horrors in the Rock", "fhv/e_hitr.webp", FHV_COLOR, FHV_ICON,),
        Card("Refractions", "fhv/e_refractions.webp", FHV_COLOR, FHV_ICON,),
        Card("Agents of the Colour", "fhv/e_aotc.webp", FHV_COLOR, FHV_ICON,),
        Card("Blight", "fhv/e_blight.webp", FHV_COLOR, FHV_ICON,),
        Card("Fire!", "fhv/e_fire.webp", FHV_COLOR, FHV_ICON,),
        Card("Transfiguration", "fhv/e_transfiguration.webp", FHV_COLOR, FHV_ICON,),
        Card("Mutations", "fhv/e_mutations.webp", FHV_COLOR, FHV_ICON,),
        Card("Myconids", "fhv/e_myconids.webp", FHV_COLOR, FHV_ICON,),
        Card("The Forest", "fhv/e_the_forest.webp", FHV_COLOR, FHV_ICON,),
    ]
)


###############################################################################
# Challenge Missions
###############################################################################

CHALLENGE_COLOR = "#FFD4B2"
CHALLENGE_MISSIONS = make_set(
    [
        Card(
            "By the Book",
            "challenge/by_the_book.svg",
            CHALLENGE_COLOR,
            "challenge/by_the_book.svg",
        ),
        Card(
            "Read or Die",
            "challenge/read_or_die.svg",
            CHALLENGE_COLOR,
            "challenge/read_or_die.svg",
        ),
        Card(
            "All or Nothing",
            "challenge/all_or_nothing.svg",
            CHALLENGE_COLOR,
            "challenge/all_or_nothing.svg",
        ),
        Card(
            "Bad Blood",
            "challenge/bad_blood.svg",
            CHALLENGE_COLOR,
            "challenge/bad_blood.svg",
        ),
        Card(
            "Red Tide Rising",
            "challenge/red_tide_rising.svg",
            CHALLENGE_COLOR,
            "challenge/red_tide_rising.svg",
        ),
    ]
)

###############################################################################
# Curse of the Rougarou
###############################################################################

ROUGAROU_COLOR = "#BFCCB5"
ROUGAROU_ICON = "standalones/curse/set.svg"
ROUGAROU = make_set(
    [
        Card(
            "Curse of the Rougarou: Setup",
            "standalones/curse/set.svg",
            ROUGAROU_COLOR,
            ROUGAROU_ICON,
        ),
        Card("The Bayou", "standalones/curse/bayou.svg", ROUGAROU_COLOR, ROUGAROU_ICON),
        Card(
            "Curse of the Rougarou: Encounters",
            "standalones/curse/curse.svg",
            ROUGAROU_COLOR,
            ROUGAROU_ICON,
        ),
    ],
    num_tabs=3,
)

###############################################################################
# Carnivale of Horrors
###############################################################################

CARNEVALE_COLOR = "#FFF89A"
CARNEVALE_ICON = "standalones/carnival/set.svg"
CARNEVALE = make_set(
    [
        Card(
            "Carnevale of Horrors: Setup",
            "standalones/carnival/set.svg",
            CARNEVALE_COLOR,
            CARNEVALE_ICON,
        ),
        Card(
            "Carnevale of Horrors: Encounters",
            "standalones/carnival/carnevale.svg",
            CARNEVALE_COLOR,
            CARNEVALE_ICON,
        ),
    ],
    num_tabs=3,
)

###############################################################################
# Murder at the Excelsior Hotel
###############################################################################

HOTEL_COLOR = "#F1D3B3"
HOTEL_ICON = "standalones/hotel/set.svg"
HOTEL = make_set(
    [
        Card(
            "Murder at the Excelsior Hotel",
            "standalones/hotel/murder.svg",
            HOTEL_COLOR,
            HOTEL_ICON,
        ),
        Card(
            "Alien Interference",
            "standalones/hotel/alien_interference.svg",
            HOTEL_COLOR,
            HOTEL_ICON,
        ),
        Card(
            "Dark Rituals",
            "standalones/hotel/dark_rituals.svg",
            HOTEL_COLOR,
            HOTEL_ICON,
        ),
        Card(
            "Excelsior Management",
            "standalones/hotel/excelsior_management.svg",
            HOTEL_COLOR,
            HOTEL_ICON,
        ),
        Card(
            "Sins of the Past",
            "standalones/hotel/sins_of_the_past.svg",
            HOTEL_COLOR,
            HOTEL_ICON,
        ),
        Card(
            "Vile Experiments",
            "standalones/hotel/vile_experiments.svg",
            HOTEL_COLOR,
            HOTEL_ICON,
        ),
    ],
    num_tabs=3,
)

###############################################################################
# Guardians of the Abyss
###############################################################################

ABYSS_COLOR = "#7286D3"
ABYSS_ICON = "standalones/abyss/set.svg"
ABYSS = make_set(
    [
        Card(
            "I: The Eternal Slumber",
            "standalones/abyss/the_eternal_slumber.svg",
            ABYSS_COLOR,
            ABYSS_ICON,
        ),
        Card(
            "II: The Night's Usurper",
            "standalones/abyss/the_nights_usurper.svg",
            ABYSS_COLOR,
            ABYSS_ICON,
        ),
        Card(
            "Sands of Egypt",
            "standalones/abyss/sands_of_egypt.svg",
            ABYSS_COLOR,
            ABYSS_ICON,
        ),
        Card(
            "Brotherhood of the Beast",
            "standalones/abyss/brotherhood_of_the_beast.svg",
            ABYSS_COLOR,
            ABYSS_ICON,
        ),
        Card(
            "Abyssal Tribute",
            "standalones/abyss/abyssal_tribute.svg",
            ABYSS_COLOR,
            ABYSS_ICON,
        ),
        Card(
            "Abyssal Gifts",
            "standalones/abyss/abyssal_gifts.svg",
            ABYSS_COLOR,
            ABYSS_ICON,
        ),
    ],
    num_tabs=3,
)

###############################################################################
# The Blob that Ate Everything
###############################################################################

BLOB_COLOR = "#b1e37b"
BLOB_ICON = "standalones/blob/set.webp"
BLOB = make_set(
    [
        Card(
            "The Blob that Ate Everything",
            "standalones/blob/set.webp",
            BLOB_COLOR,
            BLOB_ICON,
        ),
        Card(
            "Encounters",
            "standalones/blob/encounters.webp",
            BLOB_COLOR,
            BLOB_ICON,
        ),
        Card(
            "Mi-Go Incursion",
            "standalones/blob/mi_go_incursion.webp",
            BLOB_COLOR,
            BLOB_ICON,
        ),
        Card(
            "Single Group",
            "standalones/blob/single.webp",
            BLOB_COLOR,
            BLOB_ICON,
        ),
        Card(
            "Epic Multiplayer",
            "standalones/blob/multi.webp",
            BLOB_COLOR,
            BLOB_ICON,
        ),
    ],
    num_tabs=3,
)

###############################################################################
# War of the Outer Gods
###############################################################################

WAR_COLOR = "#84cbd9"
WAR_ICON = "standalones/wotog/set.webp"
WAR = make_set(
    [
        Card(
            "War of the Outer Gods",
            "standalones/wotog/set.webp",
            WAR_COLOR,
            WAR_ICON,
        ),
        Card(
            "Encounters",
            "standalones/wotog/encounters.webp",
            WAR_COLOR,
            WAR_ICON,
        ),
        Card(
            "Children of Paradise",
            "standalones/wotog/children.webp",
            WAR_COLOR,
            WAR_ICON,
        ),
        Card(
            "Swarm of Assimilation",
            "standalones/wotog/swarm.webp",
            WAR_COLOR,
            WAR_ICON,
        ),
        Card(
            "Death of Stars",
            "standalones/wotog/death.webp",
            WAR_COLOR,
            WAR_ICON,
        ),
    ],
    num_tabs=3,
)

###############################################################################
# Machinations Through Time
###############################################################################

MACH_COLOR = "#7f89c7"
MACH_ICON = "standalones/machinations_through_time/set.webp"
MACH = make_set(
    [
        Card(
            "Machinations Through Time",
            "standalones/machinations_through_time/set.webp",
            MACH_COLOR,
            MACH_ICON,
        ),
        Card(
            "Encounters",
            "standalones/machinations_through_time/encounters.webp",
            MACH_COLOR,
            MACH_ICON,
        ),
        Card(
            "Single Group",
            "standalones/blob/single.webp",
            MACH_COLOR,
            MACH_ICON,
        ),
        Card(
            "Epic Multiplayer",
            "standalones/blob/multi.webp",
            MACH_COLOR,
            MACH_ICON,
        ),
    ],
    num_tabs=4,
)

###############################################################################
# Fortune and Folly
###############################################################################

FORTUNE_COLOR = "#c77fa5"
FORTUNE_ICON = "standalones/fortune_and_folly/set.webp"
FORTUNE = make_set(
    [
        Card(
            "Fortune and Folly",
            "standalones/fortune_and_folly/set.webp",
            FORTUNE_COLOR,
            FORTUNE_ICON,
        ),
        Card(
            "Encounters",
            "standalones/fortune_and_folly/encounters.webp",
            FORTUNE_COLOR,
            FORTUNE_ICON,
        ),
        Card(
            "Fortune's Chosen",
            "standalones/fortune_and_folly/fortune.webp",
            FORTUNE_COLOR,
            FORTUNE_ICON,
        ),
        Card(
            "Plan in Shambles",
            "standalones/fortune_and_folly/shambles.webp",
            FORTUNE_COLOR,
            FORTUNE_ICON,
        ),
    ],
    num_tabs=4,
)



###############################################################################
# The Midwinter Gala
###############################################################################

GALA_COLOR = "#e3aa7b"
GALA_ICON = "standalones/the_midwinter_gala/set.svg"
GALA = make_set(
    [
        Card(
            "The Midwinter Gala",
            "standalones/the_midwinter_gala/set.svg",
            GALA_COLOR,
            GALA_ICON,
        ),
    ],
    num_tabs=2,
)

