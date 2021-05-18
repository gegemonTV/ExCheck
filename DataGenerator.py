from wtforms import Form, TextField, Field


class DataItem(Form):
    number = TextField(label="Number")
    correct_answer = TextField(label="Correct answer")
    add_button = Field(label="add", widget="button")