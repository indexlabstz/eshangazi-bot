from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import requests
from slugify import slugify

url = "http://eshangazi.test/api/item-categories"


class ActionItemCategories(Action):

    def name(self) -> Text:
        return "action_item_categories"

    def run(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        categories_url = url

        response = requests.get(url=categories_url).json()

        buttons = []

        for item in response['categories']:
            buttons.append({
                "title": item['name'],
                "payload": item['name']
            })

        dispatcher.utter_message(text="Karibu na hapa chini ndio mambo ninaweza kukusaidia:", buttons=buttons)

        return []