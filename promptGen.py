import streamlit
from tqdm import tqdm, trange
import pyinputplus as inp
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

#AI stuff
device = 'cuda' if torch.cuda.is_available() else 'cpu'
model_name = 'Rijgersberg/GEITje-7B-chat-v2'
model = AutoModelForCausalLM.from_pretrained(model_name, torch_dtype=torch.bfloat16,
                                             low_cpu_mem_usage=True, use_flash_attention_2=False,
                                             device_map=device)
tokenizer = AutoTokenizer.from_pretrained(model_name)

def generate(prompt, temperature=0.2, top_k=50, max_new_tokens=1_000):
    conversation = [
    {
        'role': 'user',
        'content': prompt
    }
    ]

    tokenized = tokenizer.apply_chat_template(conversation, add_generation_prompt=True,
                                              return_tensors='pt').to(device)
    outputs = model.generate(tokenized, do_sample=True, temperature=temperature,
                             top_k=top_k, max_new_tokens=max_new_tokens)

    return tokenizer.decode(outputs[0], skip_special_tokens=True)


#constanten
bedrijf = "Vrije Universiteit Amsterdam"
locatie = "Amsterdam"

#functie
functienaam = inp.inputStr(prompt="Voer naam functie in: ")
functiegebied = inp.inputMenu(["ICT", "HR"] , prompt="Wat is het functiegebied? ")
contracttype = inp.inputMenu(["Tijdelijk met uitzicht op vast dienstverband", "Tijdelijk", "Vast dienstverband"], prompt="Welk contracttype? ")
opleidingsniveau = inp.inputMenu(["MBO", "HBO", "Master"] , prompt="Wat is het opleidingsniveau? ")
taken = inp.inputStr(prompt="Wat zijn de taken van deze baan? (komma-gescheiden) ")
eisen = inp.inputStr(prompt="Wat zijn de functie-eisen van deze baan? (komma-gescheiden) ")
ufo_profielen = inp.inputStr(prompt="Wat is/zijn de ufo-profiel(en) van deze baan? (komma-gescheiden) ")

#team
dienst = inp.inputStr(prompt="Voer vu-eenheid in: ") 
afdeling = inp.inputStr(prompt="Voer afdeling/team in: ")

#tijd en geld
fte_min = inp.inputStr(prompt="Voer minimum FTE in: ")
fte_max = inp.inputStr(prompt="Voer maximum FTE in: ")
salaris_minimum = inp.inputStr(prompt="Voer minimum salaris in: ")
salaris_minimum_schaal = inp.inputStr(prompt="Voer minimum salarisschaal in: ")
salaris_maximum = inp.inputStr(prompt="Voer maximum salaris in: ")
salaris_maximum_schaal = inp.inputStr(prompt="Voer maximum salarisschaal in: ")

#contact
eigenaar = inp.inputStr(prompt="Wie is de functieeigenaar? ")
eigenaar_functie = inp.inputStr(prompt="Wat is de functie van de functieeigenaar? ")
eigenaar_telefoon = inp.inputStr(prompt="Wat is het telefoonnummer van de functieeigenaar? ")
eigenaar_email = inp.inputStr(prompt="Wat is het mailadres van de functieeigenaar? ")

# (Gen) Intro
prompt_intro = f"Schrijf een opvallende en uitnodigende introductie van 1 alinea voor een vacature van een {functienaam} bij {bedrijf}."

intro = generate(prompt_intro)

# (Vast) Data
data = f"""
Alle feiten op een rijtje: \n
Functiegebied: {functiegebied}
Opleidingsniveau: {opleidingsniveau} \n
VU-eenheid: {dienst} \n
Contracttype: {contracttype} \n
FTE: {fte_min}-{fte_max} \n
Minimale salarisschaal: €{salaris_minimum} (Schaal {salaris_minimum_schaal}) \n
Maximale salarisschaal: €{salaris_maximum} (Schaal {salaris_maximum_schaal}) \n
"""

# (Gen) Functieomschrijving
prompt_omschrijving = f"Schrijf in 1 alinea een nette en duidelijke functiebeschrijving voor een {functienaam} bij de afdeling {afdeling} van de VU. Noem het feit dat er 30.000 studenten en 5.000 medewerkers van het werk afhangen."
omschrijving = generate(prompt_omschrijving)

# (Vast) Taken
taken = " " + taken
takenlijst = taken.split(",")
takentekst = "Jouw taken hierbij zijn: \n"
for taak in takenlijst:
    takentekst += f"    ● {taak} \n"
takentekst += "\n \n"

# (Vast) Prerequisites

eisen = " " + eisen
eisenlijst = eisen.split(",")
eisentekst = "Functie-eisen: \n"
for taak in eisenlijst:
    eisentekst += f"    ● {taak} \n"
eisentekst += "\n \n"

# (Vast) aanbod

ufo_profielen = " " + ufo_profielen
profielenlijst = ufo_profielen.split(",")
profielentekst = ""
if len(profielenlijst) > 1:
    for profiel in profielenlijst:
        if profielenlijst.index(profiel) != 0:
            profielentekst += f", of{profiel}"
        else:
            profielentekst += profielenlijst[0]
else:
    profielentekst = profielenlijst[0]

aanbod = f"""
Wat bieden wij? \n
Een uitdagende functie bij een maatschappelijk betrokken organisatie. Het salaris bedraagt afhankelijk van opleiding en ervaring op voltijdse basis minimaal €{salaris_minimum} (Schaal {salaris_minimum_schaal}) en maximaal €{salaris_minimum} (Schaal {salaris_minimum_schaal}) bruto per maand. \n
De functie is ingedeeld volgens UFO-profiel(en): {profielentekst} en staat open voor ten minste {fte_min} fte. \n
\n
De arbeidsovereenkomst wordt in eerste instantie aangegaan voor een periode van 1 jaar.\n
Daarnaast beschikt de VU over aantrekkelijke secundaire arbeidsvoorwaarden en regelingen die een goede combinatie van werk en privé mogelijk maken, zoals: \n
● maximaal 41 vakantiedagen bij een voltijds dienstverband, \n
● 8% vakantietoeslag en 8,3% eindejaarsuitkering, goede en voordelige sportfaciliteiten, \n
● ruimte voor persoonlijke ontwikkeling, \n
● hybride werken maakt een goede werk/privébalans mogelijk \n \n
"""

# Over
# Keuze: standaard riedeltje kopieren of laten genereren
prompt_over = "Beschrijf kort hoe de VU de wereld verbetert "

over = f"""
Over de VU \n
Bijdragen aan een betere wereld door onderscheidend onderwijs en grensverleggend onderzoek, dat is de ambitie van de VU. Een universiteit waar persoonlijke vorming én maatschappelijke betrokkenheid centraal staan. Waar we vanuit verschillende disciplines en achtergronden samenwerken aan innovaties en nieuwe inzichten. Ons onderzoek beslaat het hele spectrum: van alfa, gamma en bèta tot leven en medische wetenschappen. \n \n
Aan de VU studeren ruim 30.000 studenten en werken meer dan 5.500 medewerkers. De uitstekend bereikbare VU-campus is gevestigd in het hart van de Amsterdamse Zuidas, een inspirerende omgeving voor onderwijs en onderzoek. \n \n
"""
over = generate(prompt_over)

# Waarden
# Keuze: standaard riedeltje kopieren of laten genereren
prompt_waarden = f"Beschrijf binnen 1 alinea de waarde van inclusie en diversiteit binnen de VU en noem dat het kernwaardes van de VU zijn"
waarden = """
Diversiteit \n
Diversiteit is een kernwaarde van de VU. Wij staan voor een inclusieve gemeenschap en geloven dat diversiteit en internationalisering bijdragen aan de kwaliteit van onderwijs en onderzoek. We zijn dan ook voortdurend op zoek naar mensen die door hun achtergrond en ervaring bijdragen aan de diversiteit van onze campus. \n \n
"""
waarden = generate(prompt_waarden)

# (Gen) Dienst
prompt_dienst = f"Beschrijf binnen twee alinea's wat de dienst {dienst} doet bij {bedrijf}"

dienst = generate(prompt_dienst)

# (Gen) Afdeling
prompt_afdeling = f"Beschrijf binnen 1 alinea wat de afdeling {afdeling} binnen {dienst} doet."

afdeling = generate(prompt_afdeling)

# Vragen
vragen = f"""
Vragen \n
Voor vragen over de vacature kun je contact opnemen met: \n
Naam: {eigenaar} \n
Functie: {eigenaar_functie} \n
Telefoonnummer: {eigenaar_telefoon} \n
E-mail: {eigenaar_email} \n \n
Acquisitie naar aanleiding van deze advertentie wordt niet op prijs gesteld.
"""

delen = [intro, data, omschrijving, takentekst, eisentekst, aanbod, over, waarden, dienst, afdeling, vragen]

vacature = ""
for deel in delen:
    vacature += deel

print(vacature)