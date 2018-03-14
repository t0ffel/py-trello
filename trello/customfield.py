# -*- coding: utf-8 -*-
from __future__ import with_statement, print_function, absolute_import

from trello import TrelloBase
from trello.compat import force_str


class CustomField(TrelloBase):
    """
    Class representing a Trello CustomField.
    """
    def __init__(self, client, custom_field_id, name, board_id, field_type="list", options=[]):
        super(CustomField, self).__init__()
        self.client = client
        self.id = custom_field_id
        self.name = name
        self.board_id = board_id
        self.type = field_type
        self.options = options

    @classmethod
    def from_json(cls, board, json_obj):
        """
        Deserialize the label json object to a Label object

        :board: the parent board the label is on
        :json_obj: the label json object
        """
        field = CustomField(board.client,
                            custom_field_id=json_obj['id'],
                            name=json_obj['name'],
                            board_id=board.id,
                            field_type=json_obj['type'],
                            options=json_obj['options'])
        return field

    def __repr__(self):
        return force_str(u'<CustomField %s>' % self.name)

    def fetch(self):
        """Fetch all attributes for this Custom Field"""
        json_obj = self.client.fetch_json('/customField/' + self.id)
        self.name = json_obj['name']
        return self

    def delete(self):
        """Removes this customfield"""
        self.client.fetch_json(
            '/customFields/%s' % self.id,
            http_method='DELETE')

    def add_list_option(self, text, pos="bottom"):
        """Add an option to custom field of type list"""
        body = { 'pos': pos,
                 'value': {
                     'text': text }}
        obj = self.client.fetch_json(
				'/customField/%s/options' % self.id,
				http_method='POST',
				post_args=body)

    def remove_list_option(self, option_id):
         self.client.fetch_json(
            '/customFields/%s/options/%s' % (self.id, option_id),
            http_method='DELETE')
