cliche_list = [
 "absolutely conclusive",
"agricultural crops",
"awkward dilemma",
"close proximity",
"complete monopoly",
"completely full",
"divisive quarrel",
"end result ",
"entirely absent",
"exact counterpart",
"future plan",
"general public",
"grateful thanks",
"hired mercenary",
"irreducible minimum",
"lonely hermit",
"lifeless corpse",
"meaningless gibberish",
"mutual cooperation",
"new record ",
"old adage",
"organic life ",
"original founder",
"patently obvious",
"personal friend",
"personal opinion",
"pragmatic realist",
"present incumbent",
"sworn affidavit",
"true facts",
"ultimate outcome",
"violent explosion",
"determined the truth of",
"gave permission to ",
"held a meeting",
"proved of benefit to",
"put in an appearance",
"reached an agreement",
"submitted his resignation",
"take into consideration",
"established conclusive evidence of",
"take into custody",
"accommodations",
"ameliorate",
"approximately",
"assistance",
"commence",
"deactivate",
"endeavor",
"finalize",
"implement",
"in consequence of",
"initiate",
"methodology",
"motivation ",
"objective",
"peruse",
"prior to",
"proliferation",
"purchase ",
"remuneration",
"replicate",
"socialize",
"substantial proportion",
"underprivileged",
"utilize",
"armed to the teeth ",
"banker's hours ",
"battle royal",
"beat a hasty retreat ",
"beauty and the beast ",
"bewildering variety",
"beyond the shadow of a doubt",
"bite the dust",
"blazing inferno",
"blessed event",
"blessing in disguise",
"blissful ignorance",
"bull in a china shop",
"burn one's bridges ",
"burn the midnight oil",
"burning issue",
"calm before the storm",
"cherished belief ",
"clear the decks",
"club-wielding police",
"colorful scene",
"conspicuous by its absence",
"coveted award",
"crack troops",
"curvaceous blonde",
"dramatic new move",
"dread disease",
"dream come true",
"drop in the bucket",
"fame and fortune",
"feast or famine",
"fickle fortune ",
"gentle hint",
"glaring omission",
"glutton for punishment",
"gory details?",
"grief-stricken",
"Grim Reaper",
"hand in glove",
"hammer out",
"happy couple",
"hook, line and sinker",
"head over heels in love",
"heart of gold",
"heavily armed troops",
"iron out",
"intensive investigation",
"Lady Luck",
"last-ditch stand",
"leave no stone unturned",
"leaps and bounds ",
"light at the end of the tunnel",
"lightning speed",
"limps into port",
"lock, stock and barrel",
"long arm of the law",
"man in the street",
"marvels of science",
"matrimonial bliss",
"meager pension ",
"miraculous escape",
"Mother Nature",
"moves into high gear",
"never a dull moment",
"Old Man Winter",
"paints a grim picture",
"pay the supreme penalty",
"picture of health",
"pillar of society",
"pillar of the church ",
"pinpoint the cause ",
"police dragnet ",
"pool of blood",
"posh resort",
"powder keg",
"pre-dawn darkness",
"prestigious law firm ",
"proud heritage",
"proud parents",
"pursuit of excellence",
"radiant bride",
"red faces",
"red-faced",
"reins of government",
"rushed to the scene",
"scantily clad",
"scintilla of evidence",
"scurried to shelter",
"selling like hotcakes",
"spearheading the campaign",
"spirited debate",
"scintilla of evidence",
"scurried to shelter",
"spotlessly clean",
"sprawling base",
"sprawling facility",
"spreading like wildfire",
"steaming jungle",
"sticks out like a sore thumb",
"stranger than fiction",
"storm of protest",
"supreme sacrifice",
"surprise move",
"sweep under the rug",
"sweet harmony",
"sweetness and light",
"tender mercies",
"terror-stricken",
"tie the knot ",
"tip of the iceberg",
"tower of strength",
"true colors",
"vanish in thin air",
"walking encyclopedia",
"wealth of information",
"whirlwind campaign",
"wouldn't touch with a ten foot pole",
"last but not least",
"beck and call",
"betwixt and between",
"bits and pieces",
"blunt and brutal",
"bound and determined",
"clear and simple ",
"confused and bewildered",
"death and destruction",
"disgraced and dishonored",
"each and every",
"fair and just",
"few and far between",
"nervous and distraught",
"nook and cranny",
"pick and choose",
"ready and willing",
"right and proper ",
"safe and sound",
"shy and withdrawn",
"smooth and silk",
"various and sundry",
"very unique",
]

def ask(prompt, type_=None, min_=None, max_=None, range_=None):
    """Get user input of a certain type, with range and min/max options."""
    # comes from stack overflow:
    """/questions/23294658/asking-the-user-for-input-until-they-give-a-valid-response/"""
    if min_ is not None and max_ is not None and max_ < min_:
        raise ValueError("min_ must be less than or equal to max_.")
    while True:
        ui = input(prompt)
        if type_ is not None:
            try:
                ui = type_(ui)
            except ValueError:
                print("Input type must be {0}.".format(type_.__name__))
                continue
        if max_ is not None and ui > max_:
            print("Input must be less than or equal to {0}.".format(max_))
        elif min_ is not None and ui < min_:
            print("Input must be greater than or equal to {0}.".format(min_))
        elif range_ is not None and ui not in range_:
            if isinstance(range_, range):
                template = "Input must be between {0.start} and {0.stop}."
                print(template.format(range_))
            else:
                template = "Input must be {0}."
                if len(range_) == 1:
                    print(template.format(*range_))
                else:
                    print(
                        template.format(
                            " or ".join(
                                (
                                    ", ".join(map(str, range_[:-1])),
                                    str(range_[-1]),
                                )
                            )
                        )
                    )
        else:
            return ui

text = ""
file_path = ask("Enter the absoulte or relative path to a text file for checking: ", type_ = str)
with open(file_path, "r") as my_file:
    text = my_file.read()

lowercase_text = text.lower()
print("List of cliches:\n")
for cliche in cliche_list:
  if cliche in lowercase_text:
    print(cliche)
  else:
    #print("ok")
    pass
