import streamlit as st

#constanten
bedrijf = "Vrije Universiteit Amsterdam"
locatie = "Amsterdam"


def gebruikers_input():
    """gebruiker geeft de benodigde input
    param: geen
    return: alle input van de gebruiker
    """
    dict_gebruikers_input = {}
    with st.sidebar:
        st.title("VU Vacature generator")
        st.write("Selecteer de volgende items en klik dan op genereer")
        functienaam = st.text_input("Voer naam functie in: ", "Senior Microsoft Systems Engineer")
        functiegebied = st.selectbox("Wat is het functiegebied?", ["ICT", "HR"])
        contracttype = st.selectbox("Welk contracttype?", ["Tijdelijk met uitzicht op vast dienstverband", "Tijdelijk", "Vast dienstverband"])
        opleidingsniveau = st.selectbox("Wat is het opleidingsniveau?", ["MBO", "HBO", "Master"])
        taken = st.text_input("Wat zijn de taken van deze baan? (komma-gescheiden)", "Beheer en optimalisatie van IT-systemen, Beheer van IT-systemen, Optimalisatie van complexe IT-systemen")
        eisen = st.text_input("Wat zijn de functie-eisen van deze baan? (komma-gescheiden)", "Expertise in Microsoft-technologieën, zoals Azure, Windows Server en Office 365, Ervaring met beheer en optimalisatie van complexe IT-systemen, Ervaring met beheer van IT-systemen")
        ufo_profielen = st.text_input("Wat is/zijn de ufo-profiel(en) van deze baan? (komma-gescheiden)", "Senior Microsoft Systems Engineer")

        #team
        dienst = st.text_input("Voer vu-eenheid in: ", "ICT")
        afdeling = st.text_input("Voer afdeling/team in: ", "IT-afdeling")

        #tijd en geld
        fte_min = st.text_input("Voer minimum FTE in: ", "0.8")
        fte_max = st.text_input("Voer maximum FTE in: ", "1.0")
        salaris_minimum = st.text_input("Voer minimum salaris in: ", "3500")
        salaris_minimum_schaal = st.text_input("Voer minimum salarisschaal in: ", "11")
        salaris_maximum = st.text_input("Voer maximum salaris in: ", "5000")
        salaris_maximum_schaal = st.text_input("Voer maximum salarisschaal in: ", "12")

        #contact
        eigenaar = st.text_input("Wie is de functieeigenaar? ", "Dhr. Jansen")
        eigenaar_functie = st.text_input("Wat is de functie van de functieeigenaar? ", "Hoofd ICT")
        eigenaar_telefoon = st.text_input("Wat is het telefoonnummer van de functieeigenaar? ", "020-1234567")
        eigenaar_email = st.text_input("Wat is het mailadres van de functieeigenaar? ", "example@vu.com")






        dict_gebruikers_input = {"functienaam": functienaam, "functiegebied": functiegebied, "contracttype": contracttype, "opleidingsniveau": opleidingsniveau, "taken": taken, "eisen": eisen, "ufo_profielen": ufo_profielen, "dienst": dienst, "afdeling": afdeling, "fte_min": fte_min, "fte_max": fte_max, "salaris_minimum": salaris_minimum, "salaris_minimum_schaal": salaris_minimum_schaal, "salaris_maximum": salaris_maximum, "salaris_maximum_schaal": salaris_maximum_schaal, "eigenaar": eigenaar, "eigenaar_functie": eigenaar_functie, "eigenaar_telefoon": eigenaar_telefoon, "eigenaar_email": eigenaar_email}
    return dict_gebruikers_input


def prompts(dict_gebruikers_input):
    """genereer de prompts
    param
    return: de prompts
    """
    functienaam = dict_gebruikers_input["functienaam"]
    functiegebied = dict_gebruikers_input["functiegebied"]
    contracttype = dict_gebruikers_input["contracttype"]
    opleidingsniveau = dict_gebruikers_input["opleidingsniveau"]
    taken = dict_gebruikers_input["taken"]
    eisen = dict_gebruikers_input["eisen"]
    ufo_profielen = dict_gebruikers_input["ufo_profielen"]
    dienst = dict_gebruikers_input["dienst"]
    afdeling = dict_gebruikers_input["afdeling"]
    fte_min = dict_gebruikers_input["fte_min"]
    fte_max = dict_gebruikers_input["fte_max"]
    salaris_minimum = dict_gebruikers_input["salaris_minimum"]
    salaris_minimum_schaal = dict_gebruikers_input["salaris_minimum_schaal"]
    salaris_maximum = dict_gebruikers_input["salaris_maximum"]
    salaris_maximum_schaal = dict_gebruikers_input["salaris_maximum_schaal"]
    eigenaar = dict_gebruikers_input["eigenaar"]
    eigenaar_functie = dict_gebruikers_input["eigenaar_functie"]
    eigenaar_telefoon = dict_gebruikers_input["eigenaar_telefoon"]
    eigenaar_email = dict_gebruikers_input["eigenaar_email"]

    # (Gen) Intro
    prompt_intro = f"Schrijf een opvallende en uitnodigende introductie van 1 alinea voor een vacature van een {functienaam} bij {bedrijf}."

    # intro = generate(prompt_intro)
    intro = """
    Bent u een ervaren Microsoft Systems Engineer die op zoek is naar een uitdagende rol bij een vooraanstaande universiteit? \n
    Vrije Universiteit Amsterdam zoekt een Senior Microsoft Systems Engineer die de kern van onze IT-infrastructuur zal versterken. \n
    Als Senior Engineer bent u verantwoordelijk voor het beheer en de optimalisatie van onze complexe IT-systemen, die essentieel zijn voor de academische gemeenschap. 
    Met uw expertise in Microsoft-technologieën, zoals Azure, Windows Server en Office 365, draagt u bij aan de betrouwbaarheid en veiligheid van onze IT-omgeving. \n
    Uw werk heeft directe impact op de dagelijkse werkzaamheden van studenten, docenten en onderzoekers.

    In een dynamische omgeving waar u zowel technische uitdagingen aangaat als bijdraagt aan maatschappelijk relevante projecten, krijgt u de kans om te werken aan de toekomst van onderwijs en onderzoek.

    Bent u de innovator die wij zoeken? Iemand die niet alleen technisch sterk is, maar ook een passie heeft voor het ondersteunen van een gemeenschap die zich inzet voor kennis en onderwijs? \n
    Dan nodigen we u van harte uit om te solliciteren en deel uit te maken van ons team dat de toekomst van onderwijs en onderzoek vormgeeft!
            """

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
    # omschrijving = generate(prompt_omschrijving)
    omschrijving = """De functie van Senior Microsoft Systems Engineer bij de afdeling Basic Infrastructure van de Vrije Universiteit Amsterdam (VU) is een sleutelpositie binnen de IT-afdeling, waarbij u verantwoordelijk bent voor het beheer en de optimalisatie van de kritieke IT-infrastructuur die essentieel is voor de dagelijkse operaties van een universiteit met meer dan 30.000 studenten en 5.000 medewerkers. Uw rol omvat het waarborgen van de beschikbaarheid, betrouwbaarheid en veiligheid van de IT-systemen, waaronder netwerken, servers, en cloud-diensten.

    Uw takenpakket omvat het ontwerpen, implementeren en onderhouden van IT-infrastructuren, het uitvoeren van updates en upgrades, het monitoren van prestaties en het oplossen van complexe problemen. U werkt nauw samen met andere IT-professionals en bent een belangrijke schakel in het ondersteunen van de universitaire gemeenschap bij het gebruik van Microsoft-technologieën.

    Uw expertise in Microsoft Azure, Windows Server, en Office 365 is cruciaal voor het ondersteunen van de digitale transformatie binnen de VU. Uw vermogen om te werken in een dynamische omgeving en uw proactieve houding bij het identificeren en aanpakken van potentiële risico's en kansen voor innovatie zijn van onschatbare waarde voor de afdeling.

    De ideale kandidaat voor deze positie is iemand met een sterke achtergrond in IT-beheer en een bewezen track record in het werken met Microsoft-producten. U heeft een passie voor technologie en een diepgaand begrip van IT-infrastructuur. Uw vermogen om zowel zelfstandig als in teamverband te werken, en uw vermogen om complexe technische vraagstukken te vertalen naar praktische oplossingen, maken u een waardevolle aanwinst voor de VU.
                    """

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
    # over = generate(prompt_over)
    # over = "over"

    # Waarden
    # Keuze: standaard riedeltje kopieren of laten genereren
    prompt_waarden = f"Beschrijf binnen 1 alinea de waarde van inclusie en diversiteit binnen de VU en noem dat het kernwaardes van de VU zijn"
    waarden = """
    Diversiteit \n
    Diversiteit is een kernwaarde van de VU. Wij staan voor een inclusieve gemeenschap en geloven dat diversiteit en internationalisering bijdragen aan de kwaliteit van onderwijs en onderzoek. We zijn dan ook voortdurend op zoek naar mensen die door hun achtergrond en ervaring bijdragen aan de diversiteit van onze campus. \n \n
    """
    # waarden = generate(prompt_waarden)
    # waarden = "waarden"

    # (Gen) Dienst
    prompt_dienst = f"Beschrijf binnen twee alinea's wat de dienst {dienst} doet bij {bedrijf}"

    # dienst = generate(prompt_dienst)
    dienst = """De dienst ICT (Informatie- en Communicatietechnologie) van de Vrije Universiteit Amsterdam (VU) speelt een cruciale rol in de ondersteuning van de academische gemeenschap en de bedrijfsvoering van de universiteit. Als een centraal punt voor informatietechnologie, zorgt ICT ervoor dat studenten, docenten, onderzoekers en medewerkers toegang hebben tot betrouwbare en veilige digitale middelen.

    De dienst ICT is verantwoordelijk voor het beheer en de ontwikkeling van de infrastructuur die essentieel is voor het functioneren van de universiteit. Dit omvat het onderhoud van netwerken, servers, en de cloud-diensten die nodig zijn voor het opslaan en delen van data. Daarnaast biedt ICT ondersteuning bij het gebruik van digitale leerplatformen, zoals online cursussen en samenwerkingssoftware, en zorgt het voor de beschikbaarheid van digitale bibliotheken en databases.

    ICT werkt ook aan de beveiliging van de universitaire systemen om de privacy en integriteit van gegevens te waarborgen. Dit is vooral belangrijk in een tijdperk waarin cybersecurity steeds meer aandacht krijgt. Verder speelt ICT een rol in het ondersteunen van onderzoekers door middel van gespecialiseerde software en data-analyse tools die nodig zijn voor hun wetenschappelijke werk.

    In de praktijk betekent dit dat ICT een breed scala aan diensten levert, van het verstrekken van technische ondersteuning bij computerproblemen tot het faciliteren van complexe IT-projecten die de universiteit helpen innoveren en verbeteren. Deze dienst is essentieel voor het ondersteunen van de academische missie van de VU en draagt bij aan de moderne en toekomstbestendige onderwijs- en onderzoeksomgeving.
    """

    # (Gen) Afdeling
    prompt_afdeling = f"Beschrijf binnen 1 alinea wat de afdeling {afdeling} binnen {dienst} doet."

    # afdeling = generate(prompt_afdeling)
    afdeling = "afdeling"

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

    return vacature


# def generate_text(input_text, style_text):
#     # Combine input and style text
#     input_style_text = input_text + " " + style_text

#     # Tokenize the combined text
#     input_ids = tokenizer.encode(input_style_text, return_tensors="pt", max_length=1024, truncation=True)

#     # Generate text based on the combined input and style
#     output = model.generate(input_ids, max_length=200, num_return_sequences=1, temperature=0.8)

#     # Decode the generated text
#     generated_text = tokenizer.decode(output[0], skip_special_tokens=True)

#     return generated_text



def main():
    st.set_page_config(layout="wide")

    dict_gebruikers_input_ = gebruikers_input()
    vacature = prompts(dict_gebruikers_input_)
    print(vacature)
    sidebar = st.sidebar


 



    # with open("Output.txt", "w", encoding="utf-8") as text_file:
    #     text_file.write(vacature)


    with open("Output.txt", "r", encoding="utf-8") as text_file:
        vacature2 = text_file.read()
    if sidebar.button("Genereer!"):
        
        with st.chat_message("assistant"):
            
            st.subheader("Generated Text")
            st.write(vacature2)
            col1, col2 = st.columns([1,1])

            with col1:
                st.button("Download als .txt")
            with col2:
                st.button("Download als .pdf")            
            
    
    
        
        
        # if st.button("Hoogleraar"):
        #     input_prompt = "Wat is de definitie van een hoogleraar?"
        #     input_text = "Wat is de definitie van een hoogleraar?"
        #     style_text = "Ik ben een hoogleraar in de informatica."
        # option = st.selectbox('Om welke functie gaat het?',    ('Hoogleraar', 'IT manager', 'HR adviseur'))


    # st.title("Language Model with Style Transfer")

    # Text input for the user
    # input_text = st.text_area("Input Text", "Enter your text here...")

    # # Style input for the user
    # style_text = st.text_area("Style Text", "Enter your style text here...")




    # # Button to generate text
    # if st.button("Generate Text"):
    #     # Generate text based on the input and style texts
    #     # generated_text = generate_text(input_text, style_text)




if __name__ == "__main__":
    main()
