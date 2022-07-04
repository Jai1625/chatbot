

# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa.shared.core.trackers import DialogueStateTracker
from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet, EventType
from rasa_sdk.executor import CollectingDispatcher
import webbrowser
import logging
from rasa_sdk.forms import FormAction


class ActionVideo(Action):
    def name(self) -> Text:
        return "action_video"

    async def run(
            self,
            dispatcher,
            tracker: Tracker,
            domain: "DomainDict",
    ) -> List[Dict[Text, Any]]:
        video_url = "https://youtu.be/jj4BL9o3Q7o"
        dispatcher.utter_message("wait... Playing your video.")
        webbrowser.open(video_url)
        return []


class ValidateRestaurantForm(Action):
    def name(self) -> Text:
        return "user_details_form"

    @staticmethod
    def required_slots(tracker: "DialogueStateTracker"):
        logging.info(f"545444{tracker}")
        return ["name", "number", "email", "date"]

    def run(
            self, dispatcher: CollectingDispatcher, tracker: DialogueStateTracker, domain: Dict
    ) -> List[EventType]:
        logging.info(f'43403904920920302')
        for slot_name in self.required_slots(tracker):
            logging.info(f'4829820302 {slot_name}')
            if tracker.slots.get(slot_name) is None:
                logging.info(f'4829820302 {slot_name}')
                # The slot is not filled yet. Request the user to fill this slot next.
                return [SlotSet("requested_slot", slot_name)]

        # All slots are filled.
        return [SlotSet("requested_slot", None)]


class ActionSubmit(Action):
    def name(self) -> Text:
        return "action_submit"

    def run(
            self,
            dispatcher,
            tracker: Tracker,
            domain: "DomainDict",
    ) -> List[Dict[Text, Any]]:
        logging.info(f'95094-2-202 {tracker.slots}')
        dispatcher.utter_message(response="utter_details_thanks",
                                 Name=tracker.get_slot("name"),
                                 Mobile_number=tracker.get_slot("number"))

