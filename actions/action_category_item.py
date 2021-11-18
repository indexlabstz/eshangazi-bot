from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import requests
from slugify import slugify

url = "https://eshangazi.co.tz/api/items/"


class ActionCategoryItem(Action):

    def name(self) -> Text:
        return "action_category_item"

    def run(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        item_title = next(tracker.get_latest_entity_values("category_item_entity"), None)

        if item_title:
            item_url = url + slugify(item_title)
            response = requests.get(url=item_url).json()

            description = response['item']['description']

            if len(response['items']) > 0:
                buttons = []

                for item in response['items']:

                    buttons.append({
                        "title": item['title'],
                        "payload": item['title']
                    })

                dispatcher.utter_message(text=description, buttons=buttons)
            else:
                dispatcher.utter_message(text=description)
        else:
            dispatcher.utter_message(text="Sijapata taarifa kwa sasa, jaribu tena")

        return []
