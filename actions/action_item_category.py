from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import requests
from slugify import slugify

url = "http://eshangazi.test/api/item-categories/"


class ActionItemCategory(Action):

    def name(self) -> Text:
        return "action_item_category"

    def run(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        item_category = next(tracker.get_latest_entity_values("item_category_entity"), None)

        if item_category:
            category_url = url + slugify(item_category)

            response = requests.get(url=category_url).json()

            description = response['category']['description']

            buttons = []

            for item in response['items']:
                buttons.append({
                    "title": item['title'],
                    "payload": item['title']
                })

            dispatcher.utter_message(text=description, buttons=buttons)
        else:
            dispatcher.utter_message(text="Sijapata taarifa kwa sasa, jaribu tena")

        return []