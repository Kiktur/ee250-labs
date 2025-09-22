from typing import Dict, List, Optional
from flask import Flask, request, jsonify
import pathlib
import uuid
import json


app = Flask(__name__)
thisdir = pathlib.Path(__file__).parent.absolute() # path to directory of this file

# Function to load and save the mail to/from the json file

def load_mail() -> List[Dict[str, str]]:
    """
    Loads the mail from the JSON file

    Returns:
        list: A list of dictionaries representing the mail entries
    """
    try:
        return json.loads(thisdir.joinpath('mail_db.json').read_text())
    except FileNotFoundError:
        return []

def save_mail(mail: List[Dict[str, str]]) -> None:
    """Save all mail entries to the JSON database file.

    Args:
        mail: The complete list of mail entry dictionaries to write.
    """
    thisdir.joinpath('mail_db.json').write_text(json.dumps(mail, indent=4))

def add_mail(mail_entry: Dict[str, str]) -> str:
    """Add a new mail entry and return its generated ID.

    Args:
        mail_entry: Dictionary with keys like 'recipient', 'sender', 'subject', 'body'.

    Returns:
        The unique ID assigned to the new mail entry.
    """
    mail = load_mail() # list of dictionaries
    mail.append(mail_entry) # appends a mail entry (Dict[str, str])
    mail_entry['id'] = str(uuid.uuid4()) # generate a unique id for the mail entry
    save_mail(mail)
    return mail_entry['id']

def delete_mail(mail_id: str) -> bool:
    """Delete a mail entry by ID.

    Loads mail entries from the JSON file, searches for the matching ID, 
    removes it from the list, and saves the updated list back to the file.

    Args:
        mail_id: The unique identifier of the mail entry to delete.

    Returns:
        True if the mail entry was found and deleted, False otherwise.
    """
    mail = load_mail()
    for i, entry in enumerate(mail):
        if entry['id'] == mail_id:
            mail.pop(i)
            save_mail(mail)
            return True

    return False

def get_mail(mail_id: str) -> Optional[Dict[str, str]]:
    """Retrieve a mail entry by its ID.

    Args:
        mail_id: The unique identifier of the mail entry to retrieve.

    Returns:
        The mail entry dictionary if found, otherwise None.
    """
    mail = load_mail()
    for entry in mail:
        if entry['id'] == mail_id:
            return entry

    return None

def get_inbox(recipient: str) -> List[Dict[str, str]]:
    """Retrieve all mail entries for a given recipient.

    Args:
        recipient: The recipient's identifier (e.g., username or email).

    Returns:
        A list of mail dictionaries sent to the specified recipient.
    """

    mail = load_mail()
    inbox = []
    for entry in mail:
        if entry['recipient'] == recipient:
            inbox.append(entry)

    return inbox

def get_sent(sender: str) -> List[Dict[str, str]]:
    """Retrieve all mail entries sent by a given sender.

    Loads mail from the JSON file, creates an empty list, and 
    searches through each entry to find those sent by the specified sender. 
    Matching entries are appended to the list, which is then returned.

    Args:
        sender: The identifier (e.g., username or email) of the sender.

    Returns:
        A list of mail entries sent from the specified sender.
    """
    mail = load_mail()
    sent = []
    for entry in mail:
        if entry['sender'] == sender:
            sent.append(entry)

    return sent

# API routes - these are the endpoints that the client can use to interact with the server
@app.route('/mail', methods=['POST'])
def add_mail_route():
    """
    Summary: Adds a new mail entry to the json file

    Returns:
        str: The id of the new mail entry
    """
    mail_entry = request.get_json()
    mail_id = add_mail(mail_entry)
    res = jsonify({'id': mail_id})
    res.status_code = 201 # Status code for "created"
    return res

@app.route('/mail/<mail_id>', methods=['DELETE'])
def delete_mail_route(mail_id: str):
    """
    Summary: Deletes a mail entry from the json file

    Args:
        mail_id (str): The id of the mail entry to delete

    Returns:
        bool: True if the mail was deleted, False otherwise
    """
    delete_attempt = delete_mail(mail_id)
    if delete_attempt == True:
        res_string = "Delete was successful"
        res_code = 200
    else:
        res_string = "Delete was unsuccessful"
        res_code = 404

    res = jsonify({'delete_status': res_string})
    res.status_code = res_code # Status code for "No Content" (successful deletion)
    return res

@app.route('/mail/<mail_id>', methods=['GET'])
def get_mail_route(mail_id: str):
    """
    Summary: Gets a mail entry from the json file

    Args:
        mail_id (str): The id of the mail entry to get

    Returns:
        dict: A dictionary representing the mail entry if it exists, None otherwise
    """
    res = jsonify(get_mail(mail_id))
    res.status_code = 200 # Status code for "ok"
    return res

@app.route('/mail/inbox/<recipient>', methods=['GET'])
def get_inbox_route(recipient: str):
    """
    Summary: Gets all mail entries for a recipient from the json file

    Args:
        recipient (str): The recipient of the mail

    Returns:
        list: A list of dictionaries representing the mail entries
    """
    res = jsonify(get_inbox(recipient))
    res.status_code = 200
    return res

# TODO: implement a rout e to get all mail entries for a sender
# HINT: start with soemthing like this:
@app.route('/mail/sent/<sender>', methods=['GET'])
def get_sender(sender: str):
    """
    Gets mail from a specific sender and returns all said mail entries
    """
    res = jsonify(get_sent(sender))
    res.status_code = 200
    return res


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
