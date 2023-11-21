from typing import Optional
from dataclasses import dataclass

@dataclass
class Card:
    text: str
    tab_icon: str
    colour: str
    back_icon: Optional[str] = None

def make_set(cards, *, num_tabs = 5):
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
RTNOTZ_ICON = 'notz/rset.svg'

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

RTNOTZ_MISSIONS = make_set(
    [
        Card("I: Return to The Gathering", "notz/rtm1.svg", RTNOTZ_COLOR, RTNOTZ_ICON),
        Card("II: Return to The Midnight Masks", "notz/rtm2.svg", RTNOTZ_COLOR, RTNOTZ_ICON),
        Card("III: Return to The Devourer Below", "notz/rtm3.svg", RTNOTZ_COLOR, RTNOTZ_ICON),
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

DUNWICH_COLOR = '#C7E9B0'
DUNWICH_ICON = 'dunwich/set.svg'
RTDUNWICH_COLOR = '#B3C99C' 
RTDUNWICH_ICON = 'dunwich/rset.svg'

DUNWICH_MISSIONS = make_set([
    Card("Ia: Extracurricular Activity", "dunwich/m1.svg", DUNWICH_COLOR, DUNWICH_ICON),
    Card("Ib: The House Always Wins", "dunwich/m2.svg", DUNWICH_COLOR, DUNWICH_ICON),
    Card("Interlude: Armitage's Fate", "dunwich/m3.svg", DUNWICH_COLOR, DUNWICH_ICON),
    Card("II: The Miskatonic Museum", "dunwich/m4.svg", DUNWICH_COLOR, DUNWICH_ICON),
    Card("III: The Essex County Express", "dunwich/m5.svg", DUNWICH_COLOR, DUNWICH_ICON),
    Card("IV: Blood on the Altar", "dunwich/m6.svg", DUNWICH_COLOR, DUNWICH_ICON),
    Card("V: Undimensioned and Unseen", "dunwich/m7.svg", DUNWICH_COLOR, DUNWICH_ICON),
    Card("VI: Where Doom Awaits", "dunwich/m8.svg", DUNWICH_COLOR, DUNWICH_ICON),
    Card("VII: Lost in Time and Space", "dunwich/m9.svg", DUNWICH_COLOR, DUNWICH_ICON),
])

DUNWICH_ENCOUNTERS = make_set([
    Card("Sorcery", "dunwich/e1.svg", DUNWICH_COLOR, DUNWICH_ICON),
    Card("The Beyond", "dunwich/e2.svg", DUNWICH_COLOR, DUNWICH_ICON),
    Card("Bishop's Thralls", "dunwich/e3.svg", DUNWICH_COLOR, DUNWICH_ICON),
    Card("Whippoorwills", "dunwich/e4.svg", DUNWICH_COLOR, DUNWICH_ICON),
    Card("Bad Luck", "dunwich/e5.svg", DUNWICH_COLOR, DUNWICH_ICON),
    Card("Naomi's Crew", "dunwich/e6.svg", DUNWICH_COLOR, DUNWICH_ICON),
    Card("Hideous Abominations", "dunwich/e7.svg", DUNWICH_COLOR, DUNWICH_ICON),
    Card("Dunwich", "dunwich/e8.svg", DUNWICH_COLOR, DUNWICH_ICON),
    Card("Beast Thralls", "dunwich/e9.svg", DUNWICH_COLOR, DUNWICH_ICON),
])

RTDUNWICH_MISSIONS = make_set([
    Card("Ia: Return to Extracurricular Activity", "dunwich/rm1.svg", RTDUNWICH_COLOR, RTDUNWICH_ICON),
    Card("Ib: Return to The House Always Wins", "dunwich/rm2.svg", RTDUNWICH_COLOR, RTDUNWICH_ICON),
    Card("II: Return to The Miskatonic Museum", "dunwich/rm3.svg", RTDUNWICH_COLOR, RTDUNWICH_ICON),
    Card("III: Return to The Essex County Express", "dunwich/rm4.svg", RTDUNWICH_COLOR, RTDUNWICH_ICON),
    Card("IV: Return to Blood on the Altar", "dunwich/rm5.svg", RTDUNWICH_COLOR, RTDUNWICH_ICON),
    Card("V: Return to Undimensioned and Unseen", "dunwich/rm6.svg", RTDUNWICH_COLOR, RTDUNWICH_ICON),
    Card("VI: Return to Where Doom Awaits", "dunwich/rm7.svg", RTDUNWICH_COLOR, RTDUNWICH_ICON),
    Card("VII: Return to Lost in Time and Space", "dunwich/rm8.svg", RTDUNWICH_COLOR, RTDUNWICH_ICON),
])

RTDUNWICH_ENCOUNTERS = make_set([
    Card("Beyond the Threshold", "dunwich/re6.svg", RTDUNWICH_COLOR, RTDUNWICH_ICON),
    Card("Secret Doors", "dunwich/re4.svg", RTDUNWICH_COLOR, RTDUNWICH_ICON),
    Card("Yog-Sothoth's Emissaries", "dunwich/re5.svg", RTDUNWICH_COLOR, RTDUNWICH_ICON),
    Card("Erratic Fear", "dunwich/re2.svg", RTDUNWICH_COLOR, RTDUNWICH_ICON),
    Card("Creeping Cold", "dunwich/re3.svg", RTDUNWICH_COLOR, RTDUNWICH_ICON),
    Card("Resurgent Evils", "dunwich/re1.svg", RTDUNWICH_COLOR, RTDUNWICH_ICON),
])

###############################################################################
# The Path to Carcosa
###############################################################################

CARCOSA_COLOR = "#FCF9BE"
CARCOSA_ICON = "carcosa/set.svg"
RTCARCOSA_COLOUR = "#F7F3B1"
RTCARCOSA_ICON = "carcosa/rset.svg"

CARCOSA_MISSIONS = make_set([
    Card("I: Curtain Call", "carcosa/m1.svg", CARCOSA_COLOR, CARCOSA_ICON),
    Card("II: The Last King", "carcosa/m2.svg", CARCOSA_COLOR, CARCOSA_ICON),
    Card("III: Echoes of the Past", "carcosa/m3.svg", CARCOSA_COLOR, CARCOSA_ICON),
    Card("IV: The Unspeakable Oath", "carcosa/m4.svg", CARCOSA_COLOR, CARCOSA_ICON),
    Card("V: A Phantom of Truth", "carcosa/m5.svg", CARCOSA_COLOR, CARCOSA_ICON),
    Card("VI: The Pallid Mask", "carcosa/m6.svg", CARCOSA_COLOR, CARCOSA_ICON),
    Card("VII: Black Stars Rise", "carcosa/m7.svg", CARCOSA_COLOR, CARCOSA_ICON),
    Card("VIII: Dim Carcosa", "carcosa/m8.svg", CARCOSA_COLOR, CARCOSA_ICON),
])

CARCOSA_ENCOUNTERS = make_set([
    Card("Evil Portents", "carcosa/e1.svg", CARCOSA_COLOR, CARCOSA_ICON),
    Card("Delusions", "carcosa/e2.svg", CARCOSA_COLOR, CARCOSA_ICON),
    Card("Hauntings", "carcosa/e3.svg", CARCOSA_COLOR, CARCOSA_ICON),
    Card("Cult of the Yellow Sign", "carcosa/e4.svg", CARCOSA_COLOR, CARCOSA_ICON),
    Card("Hastur's Gift", "carcosa/e5.svg", CARCOSA_COLOR, CARCOSA_ICON),
    Card("Decay & Filth", "carcosa/e6.svg", CARCOSA_COLOR, CARCOSA_ICON),
    Card("Byakhee", "carcosa/e9.svg", CARCOSA_COLOR, CARCOSA_ICON),
    Card("Inhabitants of Carcosa", "carcosa/e8.svg", CARCOSA_COLOR, CARCOSA_ICON),
    Card("The Stranger", "carcosa/e7.svg", CARCOSA_COLOR, CARCOSA_ICON),
])

RTCARCOSA_MISSIONS = make_set([
    Card("I: Return to Curtain Call", "carcosa/rm1.svg", RTCARCOSA_COLOUR, RTCARCOSA_ICON),
    Card("II: Return to The Last King", "carcosa/rm2.svg", RTCARCOSA_COLOUR, RTCARCOSA_ICON),
    Card("III: Return to Echoes of the Past", "carcosa/rm3.svg", RTCARCOSA_COLOUR, RTCARCOSA_ICON),
    Card("IV: Return to The Unspeakable Oath", "carcosa/rm4.svg", RTCARCOSA_COLOUR, RTCARCOSA_ICON),
    Card("V: Return to A Phantom of Truth", "carcosa/rm5.svg", RTCARCOSA_COLOUR, RTCARCOSA_ICON),
    Card("VI: Return to The Pallid Mask", "carcosa/rm6.svg", RTCARCOSA_COLOUR, RTCARCOSA_ICON),
    Card("VII: Return to Black Stars Rise", "carcosa/rm7.svg", RTCARCOSA_COLOUR, RTCARCOSA_ICON),
    Card("VIII: Return to Dim Carcosa", "carcosa/rm8.svg", RTCARCOSA_COLOUR, RTCARCOSA_ICON),
])

RTCARCOSA_ENCOUNTERS = make_set([
    Card("Maddening Delusions", "carcosa/re5.svg", RTCARCOSA_COLOUR, RTCARCOSA_ICON), # Delusion
    Card("Neurotic Fear", "carcosa/re2.svg", RTCARCOSA_COLOUR, RTCARCOSA_ICON), # Striking Fear
    Card("Decaying Reality", "carcosa/re4.svg", RTCARCOSA_COLOUR, RTCARCOSA_ICON), # Decay & Filth
    Card("Delusory Evils", "carcosa/re1.svg", RTCARCOSA_COLOUR, RTCARCOSA_ICON), # Ancient Evils
    Card("Hastur's Envoys", "carcosa/re3.svg", RTCARCOSA_COLOUR, RTCARCOSA_ICON), # Agents of Hastur
])

###############################################################################
# The Forgotten Age
###############################################################################

TFA_COLOR = '#C37B89'
TFA_ICON = 'tfa/tfa.svg'
RTTFA_COLOR = '#AE5F6E'
RTTFA_ICON = 'tfa/rtfa.svg'

TFA_MISSIONS = make_set([
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
])

TFA_ENCOUNTERS = make_set([
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
])

RTFA_MISSIONS = make_set([
    Card("I: Return to The Untamed Wilds", "tfa/rm1.svg", RTTFA_COLOR, RTTFA_ICON),
    Card("II: Return to The Doom of Eztli", "tfa/rm2.svg", RTTFA_COLOR, RTTFA_ICON),
    Card("III: Return to Threads of Fate", "tfa/rm3.svg", RTTFA_COLOR, RTTFA_ICON),
    Card("IV: Return to The Boundary Beyond", "tfa/rm4.svg", RTTFA_COLOR, RTTFA_ICON),
    Card("V: Return to Heart of the Elders", "tfa/rm5.svg", RTTFA_COLOR, RTTFA_ICON),
    Card("Va: Return to Pillars of Judgement", "tfa/rm9.svg", RTTFA_COLOR, RTTFA_ICON),
    Card("Vb: Return to K'n-yan", "tfa/rm10.svg", RTTFA_COLOR, RTTFA_ICON),
    Card("VI: Return to The City of Archives", "tfa/rm6.svg", RTTFA_COLOR, RTTFA_ICON),
    Card("VII: Return to The Depths of Yoth", "tfa/rm7.svg", RTTFA_COLOR, RTTFA_ICON),
    Card("VIII: Return to Shattered Aeons", "tfa/rm8.svg", RTTFA_COLOR, RTTFA_ICON),
    Card("IX: Return to Turn Back Time", "tfa/rm11.svg", RTTFA_COLOR, RTTFA_ICON),
])

RTFA_ENCOUNTERS = make_set([
    Card("Return to Rainforest", "tfa/re1.svg", RTTFA_COLOR, RTTFA_ICON),
    Card("Cult of Pnakotus", "tfa/re2.svg", RTTFA_COLOR, RTTFA_ICON),
    Card("Doomed Expedition", "tfa/re3.svg", RTTFA_COLOR, RTTFA_ICON),
    Card("Temporal Hunters", "tfa/re4.svg", RTTFA_COLOR, RTTFA_ICON),
    Card("Venomous Hate", "tfa/re5.svg", RTTFA_COLOR, RTTFA_ICON),
])

###############################################################################
# Edge of the Earth:
###############################################################################

EOTE_COLOR = "#E3F4F4"
EOTE_ICON = "eote/set.svg"

EOTE_MISSIONS = make_set(
    [
        Card("I: Ice and Death", "eote/ice_and_death.svg", EOTE_COLOR, EOTE_ICON),
        Card("Ia: The Crash", "eote/the_crash.svg", EOTE_COLOR, EOTE_ICON),
        Card("Ib: Lost in the Night", "eote/lost_in_the_night.svg", EOTE_COLOR, EOTE_ICON),
        Card("Ic: Seeping Nightmares", "eote/seeping_nightmares.svg", EOTE_COLOR, EOTE_ICON),
        Card("* Fatal Mirage *", "eote/fatal_mirage.svg", EOTE_COLOR, EOTE_ICON),
        Card("II: To the Forbidden Peaks", "eote/to_the_forbidden_peaks.svg", EOTE_COLOR, EOTE_ICON),
        Card("III: City of the Elder Things", "eote/city_of_the_elder_things.svg", EOTE_COLOR, EOTE_ICON),
        Card("IV: The Heart of Madness", "eote/the_heart_of_madness.svg", EOTE_COLOR, EOTE_ICON),
        Card("IVa: The Great Seal", "eote/the_great_seal.svg", EOTE_COLOR, EOTE_ICON),
        Card("IVb: Stirring in the Deep", "eote/stirring_in_the_deep.svg", EOTE_COLOR, EOTE_ICON),
    ]
)

EOTE_ENCOUNTERS = make_set(
    [
        Card("Expedition Team", "eote/expedition_team.svg", EOTE_COLOR, EOTE_ICON),
        Card("Memorials of the Lost", "eote/memorials_of_the_lost.svg", EOTE_COLOR, EOTE_ICON),
        Card("Creatures in the Ice", "eote/creatures_in_the_ice.svg", EOTE_COLOR, EOTE_ICON),
        Card("Deadly Weather", "eote/deadly_weather.svg", EOTE_COLOR, EOTE_ICON),
        Card("Hazards of Antarctica", "eote/hazards_of_antarctica.svg", EOTE_COLOR, EOTE_ICON),
        Card("Silence and Mystery", "eote/silence_and_mystery.svg", EOTE_COLOR, EOTE_ICON),
        Card("Tekeli-li", "eote/tekeli_li.svg", EOTE_COLOR, EOTE_ICON),
        Card("Left Behind", "eote/left_behind.svg", EOTE_COLOR, EOTE_ICON),
        Card("Agents of the Unknown", "eote/agents_of_the_unknown.svg", EOTE_COLOR, EOTE_ICON),
        Card("Miasma", "eote/miasma.svg", EOTE_COLOR, EOTE_ICON),
        Card("Nameless Horrors", "eote/nameless_horrors.svg", EOTE_COLOR, EOTE_ICON),
        Card("Elder Things", "eote/elder_things.svg", EOTE_COLOR, EOTE_ICON),
        Card("Penguins", "eote/penguins.svg", EOTE_COLOR, EOTE_ICON),
        Card("Shoggoths", "eote/shoggoths.svg", EOTE_COLOR, EOTE_ICON),
    ]
)

###############################################################################
# The Scarlet Keys
###############################################################################

SCARLET_COLOR = "#FD8A8A"
SCARLET_ICON = "scarlet/set.svg"

SCARLET_MISSIONS = make_set(
    [
        Card("Riddles and Rain", "scarlet/riddles_and_rain.svg", SCARLET_COLOR, SCARLET_ICON),
        Card("Dead Heat", "scarlet/dead_heat.svg", SCARLET_COLOR, SCARLET_ICON),
        Card("Sanguine Shadows", "scarlet/sanguine_shadows.svg", SCARLET_COLOR, SCARLET_ICON),
        Card("Dealings in the Dark", "scarlet/dealings_in_the_dark.svg", SCARLET_COLOR, SCARLET_ICON),
        Card("Dancing Mad", "scarlet/dancing_mad.svg", SCARLET_COLOR, SCARLET_ICON),
        Card("On Thin Ice", "scarlet/on_thin_ice.svg", SCARLET_COLOR, SCARLET_ICON),
        Card("Dogs of War", "scarlet/dogs_of_war.svg", SCARLET_COLOR, SCARLET_ICON),
        Card("Shades of Suffering", "scarlet/shades_of_suffering.svg", SCARLET_COLOR, SCARLET_ICON),
        Card("Without a Trace", "scarlet/without_a_trace.svg", SCARLET_COLOR, SCARLET_ICON),
        Card("Congress of the Keys", "scarlet/congress_of_the_keys.svg", SCARLET_COLOR, SCARLET_ICON),
    ]
)

SCARLET_ENCOUNTERS = make_set(
    [
        Card("Crimson Conspiracy", "scarlet/crimson_conspiracy.svg", SCARLET_COLOR, SCARLET_ICON),
        Card("Dark Veiling", "scarlet/dark_veiling.svg", SCARLET_COLOR, SCARLET_ICON),
        Card("Outsiders", "scarlet/outsiders.svg", SCARLET_COLOR, SCARLET_ICON),
        Card("Shadow of a Doubt", "scarlet/shadow_of_a_doubt.svg", SCARLET_COLOR, SCARLET_ICON),
        Card("Strange Happenings", "scarlet/strange_happenings.svg", SCARLET_COLOR, SCARLET_ICON),
        Card("Scarlet Sorcery", "scarlet/scarlet_sorcery.svg", SCARLET_COLOR, SCARLET_ICON),
        Card("Spreading Corruption", "scarlet/spreading_corruption.svg", SCARLET_COLOR, SCARLET_ICON),
        Card("Mysteries Abound", "scarlet/mysteries_abound.svg", SCARLET_COLOR, SCARLET_ICON),
        Card("Agents of Yuggoth", "scarlet/agents_of_yuggoth.svg", SCARLET_COLOR, SCARLET_ICON),
        Card("Agents of the Outside", "scarlet/agents_of_the_outside.svg", SCARLET_COLOR, SCARLET_ICON),
        Card("Cleanup Crew", "scarlet/cleanup_crew.svg", SCARLET_COLOR, SCARLET_ICON),
        Card("Secret War", "scarlet/secret_war.svg", SCARLET_COLOR, SCARLET_ICON),
        Card("Spatial Anomaly", "scarlet/spatial_anomaly.svg", SCARLET_COLOR, SCARLET_ICON),
        Card("Beyond the Beyond", "scarlet/beyond_the_beyond.svg", SCARLET_COLOR, SCARLET_ICON),
        Card("Red Coterie", "scarlet/red_coterie.svg", SCARLET_COLOR, SCARLET_ICON),
        Card("Globetrotting", "scarlet/globetrotting.svg", SCARLET_COLOR, SCARLET_ICON),
    ]
)

###############################################################################
# Challenge Missions
###############################################################################

CHALLENGE_COLOR = "#FFD4B2"
CHALLENGE_MISSIONS = make_set(
    [
        Card("By the Book", "challenge/by_the_book.svg", CHALLENGE_COLOR, "challenge/by_the_book.svg"),
        Card("Read or Die", "challenge/read_or_die.svg", CHALLENGE_COLOR, "challenge/read_or_die.svg"),
        Card("All or Nothing", "challenge/all_or_nothing.svg", CHALLENGE_COLOR, "challenge/all_or_nothing.svg"),
        Card("Bad Blood", "challenge/bad_blood.svg", CHALLENGE_COLOR, "challenge/bad_blood.svg"),
        Card("Red Tide Rising", "challenge/red_tide_rising.svg", CHALLENGE_COLOR, "challenge/red_tide_rising.svg"),
    ]
)

###############################################################################
# Curse of the Rougarou
###############################################################################

ROUGAROU_COLOR = "#BFCCB5"
ROUGAROU_ICON = "standalones/curse/set.svg"
ROUGAROU = make_set(
    [
        Card("Curse of the Rougarou: Setup", "standalones/curse/set.svg", ROUGAROU_COLOR, ROUGAROU_ICON),
        Card("The Bayou", "standalones/curse/bayou.svg", ROUGAROU_COLOR, ROUGAROU_ICON),
        Card("Curse of the Rougarou: Encounters", "standalones/curse/curse.svg", ROUGAROU_COLOR, ROUGAROU_ICON),
    ], num_tabs=3
)

###############################################################################
# Carnivale of Horrors
###############################################################################

CARNEVALE_COLOR = "#FFF89A"
CARNEVALE_ICON = "standalones/carnival/set.svg"
CARNEVALE = make_set(
    [
        Card("Carnevale of Horrors: Setup", "standalones/carnival/set.svg", CARNEVALE_COLOR, CARNEVALE_ICON),
        Card("Carnevale of Horrors: Encounters", "standalones/carnival/carnevale.svg", CARNEVALE_COLOR, CARNEVALE_ICON),
    ], num_tabs=3
)

###############################################################################
# Murder at the Excelsior Hotel
###############################################################################

HOTEL_COLOR = "#F1D3B3"
HOTEL_ICON = "standalones/hotel/set.svg"
HOTEL = make_set(
    [
        Card("Murder at the Excelsior Hotel", "standalones/hotel/murder.svg", HOTEL_COLOR, HOTEL_ICON),
        Card("Alien Interference", "standalones/hotel/alien_interference.svg", HOTEL_COLOR, HOTEL_ICON),
        Card("Dark Rituals", "standalones/hotel/dark_rituals.svg", HOTEL_COLOR, HOTEL_ICON),
        Card("Excelsior Management", "standalones/hotel/excelsior_management.svg", HOTEL_COLOR, HOTEL_ICON),
        Card("Sins of the Past", "standalones/hotel/sins_of_the_past.svg", HOTEL_COLOR, HOTEL_ICON),
        Card("Vile Experiments", "standalones/hotel/vile_experiments.svg", HOTEL_COLOR, HOTEL_ICON),
    ], num_tabs=3
)

###############################################################################
# Guardians of the Abyss
###############################################################################

ABYSS_COLOR = "#7286D3"
ABYSS_ICON = "standalones/abyss/set.svg"
ABYSS = make_set(
    [
        Card("I: The Eternal Slumber", "standalones/abyss/the_eternal_slumber.svg", ABYSS_COLOR, ABYSS_ICON),
        Card("II: The Night's Usurper", "standalones/abyss/the_nights_usurper.svg", ABYSS_COLOR, ABYSS_ICON),
        Card("Sands of Egypt", "standalones/abyss/sands_of_egypt.svg", ABYSS_COLOR, ABYSS_ICON),
        Card("Brotherhood of the Beast", "standalones/abyss/brotherhood_of_the_beast.svg", ABYSS_COLOR, ABYSS_ICON),
        Card("Abyssal Tribute", "standalones/abyss/abyssal_tribute.svg", ABYSS_COLOR, ABYSS_ICON),
        Card("Abyssal Gifts", "standalones/abyss/abyssal_gifts.svg", ABYSS_COLOR, ABYSS_ICON),
    ], num_tabs=3
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
