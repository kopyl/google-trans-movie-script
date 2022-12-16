# coding=utf8

import json
import httplib2
import apiclient.discovery
from oauth2client.service_account import ServiceAccountCredentials

CREDENTIALS_FILE = 'key.json'
google_docs_id = "1hoP4acNyQxKpllDrogAo9SzERKxo5KSysxs3UiLqB1U"

permissions = [
    'https://www.googleapis.com/auth/documents']
credentials = ServiceAccountCredentials.from_json_keyfile_name(
    CREDENTIALS_FILE, permissions
)
httpAuth = credentials.authorize(httplib2.Http())
service = apiclient.discovery.build('docs', 'v1', http=httpAuth)


def update_google_doc(request: list):
    service.documents().batchUpdate(documentId=google_docs_id, body={
        "requests": request
    }).execute()


example_translations = [
    {
        "translatedText": "PROPERTY RIGHT",
        "detectedSourceLanguage": "uk",
        "input": "ПРАВО ВЛАСНОСТІ"
    },
    {
        "translatedText": "Nazar Kolomiets",
        "detectedSourceLanguage": "uk",
        "input": "Назар Коломієць"
    },
    {
        "translatedText": "Logline: \"The witch from the picture hunts for the soul of the young driver Bohdan, whose family is expecting a new addition\"",
        "detectedSourceLanguage": "uk",
        "input": "Лоґлайн: «Відьма з картини полює на душу молодого водія Богдана, у сім'ї якого очікується поповнення»"
    },
    {
        "translatedText": "\"In general, a person shows freedom only in the choice of dependence\" - Hermann Hesse.",
        "detectedSourceLanguage": "uk",
        "input": "«Загалом, людина проявляє свободу лише у виборі залежності», - Герман Гессе."
    },
    {
        "translatedText": "A TRUCK is parked near the gate leading to the grounds of the estate, from whose trailer TRUCKERS 1,2 take turns removing stacks of paintings wrapped in protective film and stacking them in a nearby four-wheeled cart. Trucker 2 climbs into the darkness of the trailer behind the last picture. After some time, Tired of waiting for his partner, Trucker1, who remained next to the cart, impatiently knocks on the trailer.",
        "detectedSourceLanguage": "uk",
        "input": "Біля воріт, що ведуть на територію маєтку, припаркована ВАНТАЖІВКА, з причепу якої ВАНТАЖНИКИ1,2 по черзі дістають стопки обгорнутих захисною плівкою картин та складають їх у чотирьохколісний вантажний візок поблизу. Вантажник2 залазить у темряву причепу за останньою картиною. Через деякий час, втомившись очікувати напарника, Вантажник1, що залишився поруч із візком, нетерпляче стукає по причепу."
    },
    {
        "translatedText": "Without waiting for an answer, Trucker 1 begins to walk along the truck, dragging a cart behind him. He had to approach the semi-open door of the trailer, and with a terrible metallic clang, Trucker 2 jumps out (horribly pleased with the frightened appearance of Trucker 1) with the last picture in his hands, which, unlike the others, was wrapped in a dark, opaque film.",
        "detectedSourceLanguage": "uk",
        "input": "Не дочекавшись відповіді Вантажник1 починає крокувати поздовж вантажівки, тягнучи за собою візок. Варто було йому наблизитися до напіввідчинених дверей причепу, звідти зі страшним металевим гуркотом вистрибує (страшно задоволений наляканим виглядом Вантажника1) Вантажник2 з останньою картиною в руках, котра на відміну від інших була загорнута у темну, непрозору плівку."
    },
    {
        "translatedText": "(hacking away)",
        "detectedSourceLanguage": "uk",
        "input": "(відхекуючись)"
    },
    {
        "translatedText": "I'm too old for such a fool, Alyosha...",
        "detectedSourceLanguage": "uk",
        "input": "Я занадто старий для такої дурні, Альош…"
    },
    {
        "translatedText": "That's why I fool around. So that the heart does not grow old.",
        "detectedSourceLanguage": "uk",
        "input": "Я для того й дуркую. Аби серцем не старіти."
    },
    {
        "translatedText": "By heart? Mine will not thank you. Well, even though I got the picture...",
        "detectedSourceLanguage": "uk",
        "input": "Серцем? Моє тобі не подякує. Ну, хоч картину дістав…"
    },
    {
        "translatedText": "It's her! The same one that has never been exposed to the public before. It is said to be an unsuccessful version of Leonardo's Gioconda. Let's see, this happens only once in a lifetime.",
        "detectedSourceLanguage": "uk",
        "input": "Це вона! Та сама, яку ніколи іще не виставляли на публіку. Кажуть то невдала версія Джоконди Леонардо. Давай глянемо, таке буває лиш раз у житті."
    },
    {
        "translatedText": "And violate the customer's request. No, I'm not interested in going unpaid for this kind of pleasure.",
        "detectedSourceLanguage": "uk",
        "input": "І порушити прохання замовника. Ні, мені не цікаво залишитися без оплати заради такого задоволення."
    },
    {
        "translatedText": "You are Soviet, Peter, practical to the bone.",
        "detectedSourceLanguage": "uk",
        "input": "Радянський ти, Петре, до мозку кісток практичний."
    },
    {
        "translatedText": "(shrugging)",
        "detectedSourceLanguage": "uk",
        "input": "(знизуючи плечима)"
    },
    {
        "translatedText": "Put already...",
        "detectedSourceLanguage": "uk",
        "input": "Клади вже…"
    },
    {
        "translatedText": "Trucker 2 obediently puts the picture on the cart. Both (Truckmen 1, 2) silently pinch closer to the entrance gate (Truckman 1 – pulling a cart).",
        "detectedSourceLanguage": "uk",
        "input": "Вантажник2 слухняно кладе картину на візок. Обидва (Вантажники1,2) мовчки чимчикують поближче до в’їзних воріт (Вантажник1 – тягнучи візок)."
    },
    {
        "translatedText": "These are the carriers... We are at the gate. The cargo was delivered without damage. Open, can arrange for pickup at the gate and all over…",
        "detectedSourceLanguage": "uk",
        "input": "Це перевізники… Ми біля воріт. Вантаж доставлено без ушкоджень. Відчиніть, чи може розпишіться про отримання вантажу біля воріт та й по всьому…"
    },
    {
        "translatedText": "Only hissing is heard in response.",
        "detectedSourceLanguage": "uk",
        "input": "У відповідь чутно лише шипіння."
    },
    {
        "translatedText": "Konstantin?",
        "detectedSourceLanguage": "uk",
        "input": "Костянтине?"
    },
    {
        "translatedText": "I'm here guys.",
        "detectedSourceLanguage": "uk",
        "input": "Я вже тут, хлопці."
    },
    {
        "translatedText": "Shuddering synchronously, Vantazhniki 1,2 turn to the voice of KOSTYANKIN VLASNOY (a rich man, a philanthropist, quite fat for his age, but still a young man), who somehow ended up behind them. Leaning on the trailer, he smokes a cigarette.",
        "detectedSourceLanguage": "uk",
        "input": "Синхронно здригнувшись, Вантажники1,2 обертаються на голос КОСТЯНКИНА ВЛАСНОГО (багатій, меценат, доволі огрядна на свій вік, та все ж молода людина), що якимось чином опинився позаду них. Спершись на причеп, він курить цигарку."
    },
    {
        "translatedText": "Don't be surprised. There are too many exits in this house.",
        "detectedSourceLanguage": "uk",
        "input": "Не дивуйтесь. У цьому домі занадто багато виходів."
    },
    {
        "translatedText": "Trucker 1 approaches Kostyantyn Vlasny holding a ballpoint pen and a receipt for receiving the cargo at the ready.",
        "detectedSourceLanguage": "uk",
        "input": "Вантажник1 підходить до Костянтина Власного тримаючи кулькову ручку та квитанцію про отримання вантажу наготові."
    },
    {
        "translatedText": "(with a cigarette in his teeth, holding a pen)",
        "detectedSourceLanguage": "uk",
        "input": "(з цигаркою в зубах, взявши до рук ручку)"
    },
    {
        "translatedText": "Where to sign?",
        "detectedSourceLanguage": "uk",
        "input": "Де поставити підпис?"
    },
    {
        "translatedText": "Trucker1 indicates a place for a signature. Konstantin Vlasny begins to type out his signature, but stops halfway.",
        "detectedSourceLanguage": "uk",
        "input": "Вантажник1 вказує на місце для підпису. Костянтин Власний починає виводити підпис, але зупиняється на півдорозі."
    },
    {
        "translatedText": "(with clenched teeth because of a cigarette)",
        "detectedSourceLanguage": "uk",
        "input": "(зі стиснутими через цигарку зубами)"
    },
    {
        "translatedText": "Wait... I need to check something.",
        "detectedSourceLanguage": "uk",
        "input": "Чекайте… Треба дещо перевірити."
    },
    {
        "translatedText": "Konstantin Vlasny goes to the cart left by Trucker 1 at the gate.",
        "detectedSourceLanguage": "uk",
        "input": "Костянтин Власний іде до залишеного Вантажником1 біля воріт візка."
    },
    {
        "translatedText": "(after Konstantin)",
        "detectedSourceLanguage": "uk",
        "input": "(услід Костянтину)"
    },
    {
        "translatedText": "I tell you, everything is in perfect condition. Your right…",
        "detectedSourceLanguage": "uk",
        "input": "Кажу ж вам, усе в ідеальному стані. Ваше право…"
    },
    {
        "translatedText": "(To trucker 2, who remained next to the cart)",
        "detectedSourceLanguage": "uk",
        "input": "(Вантажнику2, що зостався поруч із візком)"
    },
    {
        "translatedText": "Show him, Alyosha. For certainty. The cargo is still delicate.",
        "detectedSourceLanguage": "uk",
        "input": "Покажи йому, Альош. Для певності. Вантаж таки делікатний."
    },
    {
        "translatedText": "Trucker 1 takes one of the paintings in a transparent film and shows it to Konstantin Vlasny, who just happened to come up.",
        "detectedSourceLanguage": "uk",
        "input": "Вантажник1 бере одну із картин у прозорій плівці та демонструє її Костянтину Власному, що якраз підійшов."
    },
    {
        "translatedText": "Not this one. I am not interested in this one.",
        "detectedSourceLanguage": "uk",
        "input": "Не цю. Ця мене не цікавить."
    },
    {
        "translatedText": "Konstantin Vlasny picks up a single picture wrapped in an opaque film.",
        "detectedSourceLanguage": "uk",
        "input": "Костянтин Власний бере до рук єдину картину обгорнуту непрозорою плівкою."
    },
    {
        "translatedText": "(To Trucker 2, carefully inspecting the film for damage)",
        "detectedSourceLanguage": "uk",
        "input": "(Вантажнику2, пильно оглядаючи плівку на наявність пошкоджень)"
    },
    {
        "translatedText": "Be honest, boy...",
        "detectedSourceLanguage": "uk",
        "input": "Кажи чесно, хлопче…"
    },
    {
        "translatedText": "Konstantin Vlasny notices a barely noticeable hole made in the film.",
        "detectedSourceLanguage": "uk",
        "input": "Костянтин Власний помічає зроблену у плівці ледь помітну дірочку."
    },
    {
        "translatedText": "Did she smile at you?",
        "detectedSourceLanguage": "uk",
        "input": "Вона тобі посміхнулася?"
    },
    {
        "translatedText": "(confused)",
        "detectedSourceLanguage": "uk",
        "input": "(збентежено)"
    },
    {
        "translatedText": "You have strange questions, sir... It is not for nothing that they say that the rich have their quirks.",
        "detectedSourceLanguage": "uk",
        "input": "Чудернацькі у Вас питання, пане… Недарма кажуть – у багатих свої причуди."
    },
    {
        "translatedText": "(menacingly, ignoring the unwanted cigarette falling down)",
        "detectedSourceLanguage": "uk",
        "input": "(грізно, ігноруючи небажане падіння цигарки додолу)"
    },
    {
        "translatedText": "Answer! Was she smiling or not? Yes or no?!",
        "detectedSourceLanguage": "uk",
        "input": "Відповідай! Посміхалася чи ні? Так чи ні?!"
    },
    {
        "translatedText": "INT. TRUCK TRAILER NIGHT",
        "detectedSourceLanguage": "uk",
        "input": "ІНТ. ПРИЧЕП ВАНТАЖІВКИ НІЧ"
    },
    {
        "translatedText": "Trucker2, with a flashlight in his teeth, carefully, layer by layer, removes the dark film from the painting, which depicts a tired-looking middle-aged woman, whose unconditional beauty was marred either by general exhaustion or simply by something indescribably eerie in her features. Taking a flashlight in his hands, Vantazhnyk2 illuminates the details of the canvas, looking at each one as if he wants to imprint a memory of the depicted for the rest of his life. When the woman's face finally appeared in the light of the flashlight, there was a knock on the side of the trailer, which, of course, distracted Trucker 2 from looking around.",
        "detectedSourceLanguage": "uk",
        "input": "Вантажник2 із кишеньковим ліхтариком у зубах обережно, шар за шаром, знімає темну плівку з картини, на якій зображена змучена на вигляд жінка середнього віку, чию безумовну вроду псувала чи то загальна змученість, чи просто щось невимовно моторошне у рисах її обличчя. Взявши ліхтарика до рук, Вантажник2 висвітлює деталі полотна, вдивляючись у кожну так, ніби хоче закарбувати згадку про зображуване до кінця життя. Коли у світлі ліхтарика нарешті опинилося обличчя жінки, у стінку причепу постукали, що, ну звісно ж, відволікає Вантажника2 від оглядин."
    },
    {
        "translatedText": "TRUCK1 (Z.K.)",
        "detectedSourceLanguage": "uk",
        "input": "ВАНТАЖНИК1 (З.К.)"
    },
    {
        "translatedText": "After a second, Trucker2 directs his gaze back to the canvas. The woman's face is again in the light of the flashlight, but now she is smiling faintly, like the Gioconda herself. While Vantazhnyk2 wipes his eyes, a terrifying female silhouette visible only to the viewer appears from the darkness directly in front of him.",
        "detectedSourceLanguage": "uk",
        "input": "Через секунду Вантажник2 спрямовує свій погляд назад на полотно. Обличчя жінки знову у світлі ліхтарика, проте тепер вона ледь помітно посміхається, як та сама Джоконда. Доки Вантажник2 протирає очі, із темряви прямісінько перед ним з'являється видимий лише глядачеві жахливий жіночий силует."
    },
    {
        "translatedText": "TRUCK2 (Z.K.)",
        "detectedSourceLanguage": "uk",
        "input": "ВАНТАЖНИК2 (З.К.)"
    },
    {
        "translatedText": "And you…",
        "detectedSourceLanguage": "ru",
        "input": "А вам…"
    },
    {
        "translatedText": "While speed-rewinding the picture back into the film, Trucker2 accidentally damages the film with his little finger.",
        "detectedSourceLanguage": "uk",
        "input": "Під час прискореної перемоткою упаковки картини назад у плівку, Вантажник2 ненавмисне пошкоджує плівку мізинцем."
    },
    {
        "translatedText": "Konstantin Vlasny raises a butt and threatens the blinded Trucker2 with it.",
        "detectedSourceLanguage": "uk",
        "input": "Костянтин Власний піднімає недопалок, погрожує ним закляклому Вантажнику2."
    },
    {
        "translatedText": "...isn't it?",
        "detectedSourceLanguage": "uk",
        "input": "…хіба ні?"
    },
    {
        "translatedText": "Throwing away the butt, Kostyantyn Vlasny instantly pulls out a pistol hidden in his belt and without hesitation shoots Vantazhnik2 in the face. Seeing this, Trucker 1 runs to the cab of the truck.",
        "detectedSourceLanguage": "uk",
        "input": "Відкинувши недопалок, Костянтин Власний миттю дістає схований за поясом пістолет і без вагань стріляє Вантажнику2 в обличчя. Побачивши це, Вантажник1 кидається навтіки до кабіни вантажівки."
    }
]


def transform_to_replaceAllText(translations: list):
    return list(map(lambda x: {
        "replaceAllText": {
            "containsText": {
                "text": x["input"],
                "matchCase": True
            },
            "replaceText": f'{x["input"]}\n{x["translatedText"]}'
        }
    }, translations))


update_google_doc(transform_to_replaceAllText(example_translations))
