from chatterbot import ChatBot
import Translator as tl
import Wit as wit
import CallAndMessage as twilio
import Email as email
import IndividualStock as singleStock
import MostActiveStocks as activeStocks


chatbot = ChatBot('Brandon', trainer = 'chatterbot.trainers.ListTrainer')
services = {"send email":email.main,
            "send message":twilio.sendMessage,
            "call phone":twilio.outgoingCall,
            "search for a stock":singleStock.findStock,
            "search for active stocks":activeStocks.findMostActiveStocks}

def main():
    #print("What language would you like your text translated to?")
    #lang = wit.talk().lower()
    lang = input("Select a language to translate to: \n")
    while True:
        request = input("Human: ")
        if request.lower() in services:
            services[request.lower()]()
            print("Completed Service")
        else:
            response = str(chatbot.get_response(request))
            print("Bot: " + tl.outputTranslation(response,lang))


if __name__ == '__main__':
    try:
        print("Welcome")
        main()

    except KeyboardInterrupt:
        print("Program Interrupted")
