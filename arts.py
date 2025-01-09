from owlready2 import *

# Create a new ontology
onto = get_ontology("http://example.org/art_ontology.owl")

onto.label = "Major Art Styles and Their Iconic Paintings"
onto.comment = "This ontology describes various concepts related to art, including major historical ages and typical styles in them. The ontology focuses also on artworks that represent the styles, the artists who created them and the museums that host them. "

with onto:
    # Define Concepts
    class Artwork(Thing): pass
    class Age(Thing): pass
    class Style(Thing): pass
    class Artist(Thing): pass
    class Region(Thing): pass
    class Medium(Thing): pass
    class Paint(Medium): pass
    class Depiction(Thing): pass
    class Landscape(Depiction): pass
    class Museum(Thing): pass

   # Define roles (object properties)
    class belongsTo(ObjectProperty):
        domain = [Style]
        range = [Age]
        is_functional = True

    class represents(ObjectProperty):
        domain = [Artwork]
        range = [Style]

    class createdBy(ObjectProperty):
        domain = [Artwork]
        range = [Artist]

    class housedIn(ObjectProperty):
        domain = [Artwork]
        range = [Museum]
        is_functional = True

    class locatedIn(ObjectProperty):
        domain = [Museum]
        range = [Region]
        us_functional = True

    class negativeReactionTo(ObjectProperty):
        domain = [Style]
        range = [Style]

    class positiveReactionTo(ObjectProperty):
        domain = [Style]
        range = [Style]

    class depicts(ObjectProperty):
        domain = [Artwork]
        range = [Depiction]

    class usesMedium(ObjectProperty):
        domain = [Artwork]
        range = [Medium]

    class livedIn(ObjectProperty):
        domain = [Artist]
        range = [Region]

    class precededBy(ObjectProperty):
        domain = [Age]
        range = [Age]
        is_transitive = True

    class succeededBy(ObjectProperty):
        domain = [Age]
        range = [Age]
        is_transitive = True
        inverse_property = precededBy

    # Define Individuals and assign properties
    #Medium
    chalk = Medium("Chalk")
    graphite = Medium("Graphite")
    acrylic_paint = Paint("AcrylicPaint")
    oil_paint = Paint("OilPaint")
    
    #Depiction
    historic_event = Depiction("HistoricalEvent")
    portrait = Depiction("Portrait")
    group_scene = Depiction("GroupScene")
    abstract_depiction = Depiction("AbstractDepiction")
    natural_landscape = Landscape("NaturalLandscape")
    urban_landscape = Landscape("UrbanLandscape")
    
    # Ages
    prehistoric_age = Age("PrehistoricAge")
    antiquity = Age("Antiquity")
    middle_ages = Age("MiddleAges")
    gothic_age = Age("GothicAge")
    renaissance = Age("Renaissance")
    new_age = Age("NewAge")
    modern_age = Age("ModernAge")
    contemporary_age = Age("ContemporaryAge")
    
    # Age relationships
    antiquity.precededBy = [prehistoric_age]
    antiquity.succeededBy = [middle_ages]
    middle_ages.precededBy = [antiquity]
    middle_ages.succeededBy = [gothic_age]
    gothic_age.precededBy = [middle_ages]
    gothic_age.succeededBy = [renaissance]
    renaissance.precededBy = [gothic_age]
    renaissance.succeededBy = [new_age]
    new_age.precededBy = [renaissance]
    new_age.succeededBy = [modern_age]
    modern_age.precededBy = [new_age]
    modern_age.succeededBy = [contemporary_age]
    contemporary_age.precededBy = [modern_age]
    
    # Regions
    western_europe = Region("WesternEurope")
    eastern_europe = Region("EasternEurope")
    north_america = Region("NorthAmerica")
    south_america = Region("SouthAmerica")
    asia = Region("Asia")
    africa = Region("Africa")
    australia = Region("Australia")

    # Styles
    paleolithic = Style("Paleolithic")
    neolithic = Style("Neolithic")
    ancient_egyptian = Style("AncientEgyptian")
    ancient_greek = Style("AncientGreek")
    roman = Style("Roman")
    byzantine = Style("Byzantine")
    romanesque = Style("Romanesque")
    gothic = Style("Gothic")
    italian_renaissance = Style("ItalianRenaissance")
    nordic_renaissance = Style("NordicRenaissance")
    baroque = Style("Baroque")
    rococo = Style("Rococo")
    classicism = Style("Classicism")
    romanticism = Style("Romanticism")
    realism = Style("Realism")
    impressionism = Style("Impressionism")
    post_impressionism = Style("PostImpressionism")
    expressionism = Style("Expressionism")
    cubism = Style("Cubism")
    futurism = Style("Futurism")
    dadaism = Style("Dadaism")
    surrealism = Style("Surrealism")
    pop_art = Style("PopArt")
    conceptual_art = Style("ConceptualArt")

    # Assign belongsTo relationships
    paleolithic.belongsTo = [prehistoric_age]
    neolithic.belongsTo = [prehistoric_age]
    ancient_egyptian.belongsTo = [antiquity]
    ancient_greek.belongsTo = [antiquity]
    roman.belongsTo = [antiquity]
    byzantine.belongsTo = [middle_ages]
    romanesque.belongsTo = [middle_ages]
    gothic.belongsTo = [gothic_age]
    italian_renaissance.belongsTo = [renaissance]
    nordic_renaissance.belongsTo = [renaissance]
    baroque.belongsTo = [new_age]
    rococo.belongsTo = [new_age]
    classicism.belongsTo = [new_age]
    realism.belongsTo = [modern_age]
    impressionism.belongsTo = [modern_age]
    post_impressionism.belongsTo = [modern_age]
    expressionism.belongsTo = [modern_age]
    cubism.belongsTo = [modern_age]
    futurism.belongsTo = [modern_age]
    dadaism.belongsTo = [modern_age]
    surrealism.belongsTo = [modern_age]
    pop_art.belongsTo = [contemporary_age]
    conceptual_art.belongsTo = [contemporary_age]

    # Assign reactions
    ancient_greek.positiveReactionTo = [ancient_egyptian]
    roman.positiveReactionTo = [ancient_greek]
    gothic.positiveReactionTo = [romanesque]
    italian_renaissance.negativeReactionTo = [gothic]
    baroque.negativeReactionTo = [renaissance]
    rococo.negativeReactionTo = [baroque]
    classicism.negativeReactionTo = [rococo]
    realism.negativeReactionTo = [romanticism]
    impressionism.negativeReactionTo = [realism]
    post_impressionism.positiveReactionTo = [impressionism]
    expressionism.negativeReactionTo = [realism]
    cubism.negativeReactionTo = [impressionism]
    surrealism.positiveReactionTo = [dadaism]
    conceptual_art.positiveReactionTo = [pop_art]

    # Non-atomic concepts
    class Painting(Artwork):
        equivalent_to = [
            Artwork & 
            (depicts.some(Depiction)) & 
            (usesMedium.some(Medium))
        ]

    class OilPainting(Painting):
        equivalent_to = [
            Painting & 
            (usesMedium.value(oil_paint))
        ]

    class AcrylicPainting(Painting):
        equivalent_to = [
            Painting & 
            (usesMedium.value(acrylic_paint))
        ]

    class HistoricalEventOilPainting(Painting):
        equivalent_to = [
            OilPainting & 
            (depicts.value(historic_event))
        ]

    class PortraitPainting(Painting):
        equivalent_to = [
            Painting & 
            (depicts.value(portrait))
        ]

    class LandscapePainting(Painting):
        equivalent_to = [
            Painting & 
            (depicts.only(Landscape))
        ]

    class PortraitOilPainting(OilPainting, PortraitPainting):
        pass
    
    # Artists
    michelangelo = Artist("Michelangelo")
    vincent_van_gogh = Artist("VincentVanGogh")
    johannes_vermeer = Artist("JohannesVermeer")
    leonardo_da_vinci = Artist("LeonardoDaVinci")
    francisco_goya = Artist("FranciscoGoya")
    andy_warhol = Artist("AndyWarhol")
    claude_monet = Artist("ClaudeMonet")
    
    vincent_van_gogh.livedIn = [western_europe]
    johannes_vermeer.livedIn = [western_europe]
    leonardo_da_vinci.livedIn = [western_europe]
    francisco_goya.livedIn = [western_europe]
    andy_warhol.livedIn = [north_america]
    claude_monet.livedIn = [western_europe]

    # Museums
    galleria_dell_accademia = Museum("GalleriaDellAccademia")
    louvre_museum = Museum("LouvreMuseum")
    moma = Museum("MoMA")
    prado_museum = Museum("PradoMuseum")
    kathe_kollwitz_museum = Museum("KatheKollwitzMuseum")
    biblioteca_reale_turin = Museum("BibliotecaRealeTurin")
    mauritshuis = Museum("Mauritshuis")
    
    galleria_dell_accademia.locatedIn = [western_europe]
    louvre_museum.locatedIn = [western_europe]
    moma.locatedIn = [north_america]
    prado_museum.locatedIn = [western_europe]
    kathe_kollwitz_museum.locatedIn = [western_europe]
    biblioteca_reale_turin.locatedIn = [western_europe]
    mauritshuis.locatedIn = [western_europe]
    
    # Artwork
    david = Artwork("David")
    david.createdBy = [michelangelo]
    david.represents = [italian_renaissance]
    david.housedIn = [galleria_dell_accademia]

    # Paintings
    mona_lisa = PortraitOilPainting("MonaLisa")
    portrait_of_a_man_in_red_chalk = PortraitPainting("PortraitOfAManInRedChalk")
    girl_with_a_pearl_earring = PortraitOilPainting("GirlWithAPearlEarring")
    campbells_soup_cans = AcrylicPainting("CampbellsSoupCans")
    third_of_may_1808 = HistoricalEventOilPainting("ThirdOfMay1808")
    haystacks = LandscapePainting("Haystacks")
    starry_night_over_the_rhone = LandscapePainting("StarryNightOverTheRhone")
    
    mona_lisa.createdBy = [leonardo_da_vinci]
    mona_lisa.depicts = [portrait]
    mona_lisa.usesMedium = [oil_paint]
    mona_lisa.represents = [italian_renaissance]
    mona_lisa.housedIn = [louvre_museum]

    portrait_of_a_man_in_red_chalk.createdBy = [leonardo_da_vinci]
    portrait_of_a_man_in_red_chalk.depicts = [portrait]
    portrait_of_a_man_in_red_chalk.usesMedium = [chalk]
    portrait_of_a_man_in_red_chalk.represents = [italian_renaissance]
    portrait_of_a_man_in_red_chalk.housedIn = [biblioteca_reale_turin]

    girl_with_a_pearl_earring.createdBy = [johannes_vermeer]
    girl_with_a_pearl_earring.depicts = [portrait]
    girl_with_a_pearl_earring.usesMedium = [oil_paint]
    girl_with_a_pearl_earring.represents = [baroque]
    girl_with_a_pearl_earring.housedIn = [mauritshuis]

    campbells_soup_cans.createdBy = [andy_warhol]
    campbells_soup_cans.depicts = [abstract_depiction]
    campbells_soup_cans.usesMedium = [acrylic_paint]
    campbells_soup_cans.represents = [pop_art]
    campbells_soup_cans.housedIn = [moma]

    third_of_may_1808.createdBy = [francisco_goya]
    third_of_may_1808.depicts = [historic_event]
    third_of_may_1808.usesMedium = [oil_paint]
    third_of_may_1808.represents = [romanticism]
    third_of_may_1808.housedIn = [prado_museum]

    haystacks.createdBy = [claude_monet]
    haystacks.housedIn = [kathe_kollwitz_museum]
    haystacks.depicts = [natural_landscape]
    haystacks.represents = [impressionism]
    haystacks.usesMedium = [oil_paint]

    starry_night_over_the_rhone.createdBy = [vincent_van_gogh]
    starry_night_over_the_rhone.depicts = [natural_landscape]
    starry_night_over_the_rhone.usesMedium = [oil_paint]
    starry_night_over_the_rhone.represents = [post_impressionism]
    starry_night_over_the_rhone.housedIn = [moma]

with onto:
    sync_reasoner()
    
inconsistent_classes = onto.inconsistent_classes()
if inconsistent_classes:
    print("Inconsistent classes:")
    for cls in inconsistent_classes:
        print(cls)
        for individual in cls.instances():
            print(f"  Inconsistent individual: {individual}")
else:
    print("The ontology is consistent.")

list(default_world.inconsistent_classes())
list(onto.inconsistent_classes())

# with onto:
#     sync_reasoner_pellet(infer_property_values = True, infer_data_property_values = True, debug = 2)

# Save ontology
onto.save(file = "art.owl")