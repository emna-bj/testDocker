# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from os import strerror, urandom
from typing import Any, Text, Dict, List
import requests
import json
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import  SlotSet, AllSlotsReset, UserUtteranceReverted
from datetime import datetime
class FetchProblemNatureAction(Action):
    def name(self) -> Text:
        return "action_check_phone"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        phone_number = tracker.get_slot('phone_number')
        file=open('actions/test.json')
        data=json.load(file)
        for d in data:
            if d["phoneNumber"]==phone_number:
                valide=d["etat"]
                if valide == "non-paiement":
                    dispatcher.utter_message(text="votre numéro a été resilié  pour non paiement")
                    return[]
                else:
                    dispatcher.utter_message(template="utter_ask_nature_prb_technique")   
                    return[]  
            else:
                dispatcher.utter_message(text=" {} est un Numero invalide".format(phone_number))
                dispatcher.utter_message(template="utter_ask_phone")
                return[]

        return []


class TestLenteurAction(Action):
    def name(self) -> Text:
        return "action_check_lenteur"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        number_site = tracker.get_slot('number_site')
        if number_site=="un seul site":
            dispatcher.utter_message(text="Donc le dysfonctionnement vient du site en question.")
            return []
        elif number_site=="plusieurs sites":
            dispatcher.utter_message(template="utter_ask_test_appareil") 
            return []
           

class ConfigAction(Action):
    def name(self) -> Text:
        return "action_config_modem"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        marque = tracker.get_slot('marque')
        if marque=="sagem": 
            url = "https://www.topnet.tn/telechargement/?dir=Modems/sagem"
        elif marque=="huawei":
            url = "https://www.topnet.tn/telechargement/?dir=Modems/huawei"    
        
        hyperlink="veuillez configurer votre modéme: <a 'target='_blank' href='"+url+"'>"+url+"</a>"
        dispatcher.utter_message(hyperlink)
        dispatcher.utter_message(template="utter_ask_prb_regle")

        return[]


class WifiAction(Action):
    def name(self) -> Text:
        return "action_prb_wifi"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        equipement = tracker.get_slot('equipement')
        if equipement=="modem":
            dispatcher.utter_message(template="utter_ask_marque_modem") 
            return []
        elif (equipement=="répéteur wifi" or equipement=="point daccès"):
            dispatcher.utter_message(template="utter_solution_wifi_pointacces")
            dispatcher.utter_message(template="utter_ask_prb_regle")
            return []


class CoupureAction(Action):
    def name(self) -> Text:
        return "action_check_voyant_power"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        etat_voyant_power = tracker.get_slot('etat_voyant_power')
        if etat_voyant_power=="vert":
            dispatcher.utter_message(template="utter_ask_etat_voyant_adsl") 
            return []
            #etat_voyant_adsl = tracker.get_slot('etat_voyant_adsl')
            #if etat_voyant_adsl=="clignote en vert":
                #dispatcher.utter_message(template="utter_ask_tonalite")
                #return []
            #else:
                #dispatcher.utter_message(text="Redémarrez votre modem puis tester la connexion")
               # return []
        elif (etat_voyant_power=="éteint" or etat_voyant_power=="rouge"):
            dispatcher.utter_message(text="Débranchez le modem de la prise électrique puis tester le sur une autre prise sans bloc multiprises ou rallonge.")
            dispatcher.utter_message(template="utter_ask_prb_regle")
            return []

