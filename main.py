import settings
import chatbot
import openai


if __name__ == "__main__":
    openai.api_key = settings.OPENAI_API_KEY
    my_dict = {
        1: "Wie kann ich eine Aktionsliste anlegen?",
        2: "Kann ich auch eine Aktionsliste für Projekte anlegen?",
        3: "Welche möglichkeiten habe ich für Einstellungen als Administrator beim Löschen und anonymisieren?",
        4: "Wie kann ich eine Anbindung an eine Telefonanlage vornehmen?",
        5: "Wie kann ich die Bewerliste tiefer legen und einen größeren Auspuff verbauen?",
        6: "Wer hat die EM 2016 gewonnen?"
        }

    for key, value in my_dict.items():
        print("Frage: ", value)
        print("##############")
        response = chatbot.get_chat_response(value)
        print("Antwort: ", response)
        print("##############")
    