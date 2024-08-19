from typing import List, Dict
import sqlite3


class OduIfa:
    def __init__(self, odu_name: str, verses: List[str], meanings: List[str], advice: List[str], keys:  List[str]):
        self.odu_name = odu_name
        self.verses = verses
        self.meanings = meanings
        self.advice = advice
        self.keys = keys


odu_ifa = [
    OduIfa(
        odu_name="eji ogbe",
        verses=[
            '''
            Eji Ogbe ni oruko mi, mo ni oruko ajinde, mo ni oruko alafia,
            Mo ni oruko orogun, mo ni oruko agbada.
            Orunmila ti o gba enikan, ti o ni gbogbo ibi si o.
            Orunmila ni ko si ibi, ko si arun, ko si aisan,
            Eyin ti e ba n gbe aye yin ba ni owo orun, 
            Eyin ti e ba ti n gbe aye yin ba ni owo aiye.
            ''',

        ],
        meanings=[
            '''
            This Odu signifies new beginnings, success, enlightenment, and a connection to
            divine wisdom. This verse speaks about overcoming obstacles and achieving peace 
            and resurrection. This odu emphasizes the power of Orunmila, the deity of wisdom
            and divination.
            ''',

        ],
        advice=['''
        Embrace new beginnings, maintain peace and be peaceful with everybody and pay close attention
        to your health and make sure to work hard.
        '''],
        keys=["new beginnings", "prosperity", "success", "prosper","growth", "opportunity", "money", ]
    ),
    OduIfa(
        odu_name="oyeku meji",
        verses=[
            '''
            Oyeku Meji ni gba mi l'owo iku
            Ebo ni o se, ki o le b'alafia ni ile aye
            Adifa fun Oyeku Meji
            Ti nlo sode, ti nlo reru
            Oyeku Meji ni gba mi l'owo iku
            Ebo ni o se, ki o le b'alafia ni ile aye
            '''
        ],
        meanings=[
            '''
            Oyeku Meji represents darkness, death, and transformation. 
            It signifies the importance of rituals and sacrifices to avoid 
            negative outcomes and ensure peace and stability in life. 
            This Odu warns against neglecting spiritual obligations and 
            emphasizes the need for constant spiritual vigilance.
            '''
        ],
        advice=[
            '''
            Perform ritual to avoid negative occurrences, avoid taking unnecessary risks that may lead to harm.
            '''
        ],
        keys=["endings", "transitions", "death", "closure", "finality"]
    ),
    OduIfa(
        odu_name= "iwori meji",
        verses=[
            '''
            Iwori wò ri l’ókè Àgbá, ìránwọ́ à á rí èmi.
            Iwori d’alejo, Àgbá níí sọ l’ójú ológun.
            Iwori wò, wò ni, Ó lọ k’ó tún wò.
            '''
        ],
        meanings=[
            '''
            Iwori Meji suggests that you may face challenges and obstacles that 
            require careful navigation, it warns against trusting people and situations blindly.
            '''
        ],
        advice=[
            '''
            Stay alert!, be vigilant and cautious in dealings, 
            strive for honesty and be transparent and be mindful of your environment.
            '''
        ],
        keys=["conflict", "deception", "struggle", "dishonesty", "challenge"]
    ),
    OduIfa(
        odu_name= "odi meji",
        verses=[
            '''
            Alakara kekere ni mo tan,
            Mo n f'okere ru le mi,
            Bi o ba gbagbe oore ti nse fun o
            Ma gbagbe ofo ti mo se.
            '''
        ],
        meanings=[
            '''
            Odi Meji emphasizes the importance of truth and integrity in overcoming adversaries.
            It suggests that victory achieved through deceit is not lasting or honorable. 
            The focus is on maintaining one's ethical standards even in the face of conflict or opposition.
            '''
        ],
        advice=[
            '''
            Uphold truth and fairness in all dealings. When faced with conflicts or adversaries, 
            it is better to rely on honesty and integrity rather than resoting to deceit or manipulation. 
            '''
        ],
        keys=["truth", "integrity", "ethics", "honor", "conflict resolution"]
    ),
    OduIfa(
        odu_name= "irosun meji",
        verses=[
            '''
            Irosun Meji o dara o,
            A difa fun Iroko tii se igi agbonrire,
            O ni ki o rubo ki awon eniyan ma baa gbe e leyin,
            Irosun Mejio, igi ti o n soro, ti o n rin.
            '''
        ],
        meanings=[
            '''
            Irosun Meji highlights the importance of having your words and actions respected and taken seriously.
            The iroko tree, a powerful and sacred symbol in Yoruba culture, is depicted as having the ability to talk and walk,
            symbolizing wisdom and authority.
            '''
        ],
        advice=[
            '''
            Take the necessary steps to ensure that your voice is heard and respected.
            Make personal sacrifices and commitment to demonstrate seriousness and earn respect.

            '''
        ],
        keys=["authority", "respect", "proactivity", "sacrifice"]
    ),
    OduIfa(
        odu_name= "otura ogbe",
        verses=[
            '''
            Otura igbo, otura igbo,
            A difa fun Orunmila nijo ti n gbon a mo igbo,
            Won ni kiakia lo rubo ki ba a le ri igbo gbo,
            orunmila gbon nigbon,
            O ri igbo gbo.
            '''
        ],
        meanings=[
            '''
            Otura ogbe highlights the importance of sacrifice and preparation in achieving wisdom.
            It underscores the idea that gainig knowledge and insight often requires proactive efforts and
            sometimes making personal sacrifices.
            '''
        ],
        advice=[
            '''
            Be proactive in your pursuit of knowledge and wisdom.
            Understand that achieving great understanding may require sacrifices, whether
            they are in terms of time, resources, or foregoing immediate pleasures.
            Prepare adequately for the challenges you face, as wisdom is crucial in navigating life's complexities.

            '''
        ],
        keys=["understanding", "preparation", "sacrifice", "wisdom", "understand"]
    ),
    OduIfa(
        odu_name= "osa otura",
        verses=[
            '''
            Osa Otura, awo Ilu beere,
            A difa fun ilu beere,
            Tii se olori omo ibu osun,
            Won ni omo araye maa bimo olojogbon,
            Won ni ko rubo ki oun naa le bimo olojogbon,
            O gbebo, o ru'bo,
            Nitori iye o bimo olojogbon.
            '''
        ],
        meanings=[
            '''
            Osa Otura emphasizes the connection between spiritual obedience and the favorable outcomes
            that follow. In the context of health, it highlights the importance of spiritual ruituals and sacrifices in maintaining
            the well-being of the community and ensuring the wisdom and vitality of future generations.
            '''
        ],
        advice=[
            '''
            Engage in preventative health measures.
            consult with traditional healers or knowledgeable elders for advice on herbal remedies.
            Your health can be deeply connected to your community and adherence to collective rituals.

            '''
        ],
        keys=["sick", "health", "well-being", "sacrifice", "wisdom"]
    ),
    OduIfa(
        odu_name= "ika",
        verses=[
            '''
            Ika bere bere
            A difa fun orunmila,
            Nijo ti i se olugbala agba,
            Won ni ki o rubo,
            Orunmila rubo
            O si ri bee.
            '''
        ],
        meanings=[
            '''
            Ika highlights Orunmila's role as a protector and guide, particularly in 
            times of crisis or when guiding those more vulnerable. The mention of "Ika the entangler"
            suggests the complexities and potential traps that might arise, emphasizing the importance
            of strategic sacrifices to navigate through challenges successfully.
            '''
        ],
        advice=[
            '''
            Employ careful and strategic thinking in all your dealings to avoid falling into traps set by others
            Be cautious in your relationships, as not everyone might have your 
            best interests at heart.
            Sometimes, making sacrifices is esstential for overcoming difficulties and protecting oneself from potential harm.
            '''
        ],
        keys=["protection", "caution", "complexity", "vulnerable", "strategy", "trap", "cautious"]
    ),
    OduIfa(
        odu_name= "oturuopon",
        verses=[
            '''
            Oturuopon ti pon omi sile,
            A difa fun Alabahun,
            Nijo ti n torun bo wa'yemoja,
            Won ni o kara n le ebo ni sise,
            Alabahun gbo, o ru ebo,
            Ebo da, omo yemoja o to'wo.
            '''
        ],
        meanings=[
            '''
            Oturuopon highlights the journey of the tortoise, a recurring character in Yoruba folklore
            known for his wisdom. Here, the tortoise prepares to meet Yemoja, the goddess of rivers and motherhood, and is advised to make sacrifices to ensure a successful
            encounter and prosperous outcomes. The spreading of water symbolizes preparation, purification, and the flow of life's energies.
            '''
        ],
        advice=[
            '''
            Be thorough in your preparations and willing to make necessary sacrifices to achieve your goals.
            Use wisdom and insights when approaching significant life changes or important decisions.
            Always seek guidance from more knowledgeable sources/people when dealing with complex issues.

            '''
        ],
        keys=["innovation", "preparation", "insight", "knowledge", "wisdom"]
    ),
]
def create_database():
    conn = sqlite3.connect('ifa_divination.db')
    c = conn.cursor()

    # Odu ifa table
    c.execute('''
        CREATE TABLE IF NOT EXISTS odu_ifa (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            odu_name TEXT NOT NULL,
            verses TEXT NOT NULL,
            meanings TEXT NOT NULL,
            advice TEXT NOT NULL,
            keys TEXT NOT NULL
        )
    ''')

    conn.commit()
    conn.close()


create_database()


def insert_odu_ifa(odu_ifa: OduIfa):
    conn = sqlite3.connect('ifa_divination.db')
    c = conn.cursor()

    c.execute('''
        INSERT INTO odu_ifa (odu_name, verses, meanings, advice, keys)
        VALUES (?, ?, ?, ?, ?)
    ''', (odu_ifa.odu_name, '\n'.join(odu_ifa.verses), '\n'.join(odu_ifa.meanings), '\n'.join(odu_ifa.advice), '\n'.join(odu_ifa.keys)))

    conn.commit()
    conn.close()


for odu in odu_ifa:
    insert_odu_ifa(odu)




